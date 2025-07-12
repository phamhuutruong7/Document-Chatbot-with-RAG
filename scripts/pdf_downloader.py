"""
PDF Downloader for PC Documentation
Downloads manuals, troubleshooting guides, and other documents from manufacturer websites
"""

import requests
import os
import time
import logging
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, quote
from typing import List, Dict, Optional, Tuple
import json
from pathlib import Path
import re

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/pdf_downloader.log'),
        logging.StreamHandler()
    ]
)

class PDFDownloader:
    """Enhanced PDF downloader with retry logic and better error handling."""
    
    def __init__(self, base_dir: str = "data/documents/"):
        self.base_dir = Path(base_dir)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })
        self.downloaded_files = []
        self.failed_downloads = []
        
        # Create logs directory
        os.makedirs('logs', exist_ok=True)
        
    def download_from_config(self, config: Dict) -> Dict[str, List[str]]:
        """Download PDFs based on configuration."""
        results = {
            'downloaded': [],
            'failed': [],
            'skipped': []
        }
        
        category = config['category']
        manufacturer = config.get('manufacturer', 'general')
        
        # Create target directory
        target_dir = self.base_dir / category / manufacturer
        target_dir.mkdir(parents=True, exist_ok=True)
        
        logging.info(f"Starting downloads for {category}/{manufacturer}")
        
        # Process direct PDF URLs
        if 'direct_pdfs' in config:
            for pdf_info in config['direct_pdfs']:
                try:
                    result = self._download_direct_pdf(pdf_info, target_dir)
                    if result:
                        results['downloaded'].append(result)
                    else:
                        results['failed'].append(pdf_info['url'])
                except Exception as e:
                    logging.error(f"Error downloading {pdf_info['url']}: {e}")
                    results['failed'].append(pdf_info['url'])
                
                # Be respectful to servers
                time.sleep(2)
        
        # Process search URLs (for future enhancement)
        if 'search_urls' in config:
            for search_config in config['search_urls']:
                try:
                    found_pdfs = self._search_for_pdfs(search_config)
                    for pdf_url, filename in found_pdfs:
                        result = self._download_pdf(pdf_url, target_dir / filename)
                        if result:
                            results['downloaded'].append(result)
                        else:
                            results['failed'].append(pdf_url)
                        time.sleep(2)
                except Exception as e:
                    logging.error(f"Error in search download: {e}")
        
        return results
    
    def _download_direct_pdf(self, pdf_info: Dict, target_dir: Path) -> Optional[str]:
        """Download a PDF from direct URL."""
        url = pdf_info['url']
        filename = pdf_info.get('filename')
        
        if not filename:
            # Extract filename from URL
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            if not filename.endswith('.pdf'):
                filename += '.pdf'
        
        # Clean filename
        filename = self._clean_filename(filename)
        filepath = target_dir / filename
        
        # Check if already exists
        if filepath.exists():
            logging.info(f"File already exists: {filename}")
            return str(filepath)
        
        return self._download_pdf(url, filepath)
    
    def _download_pdf(self, url: str, filepath: Path, max_retries: int = 3) -> Optional[str]:
        """Download a single PDF with retry logic."""
        for attempt in range(max_retries):
            try:
                logging.info(f"Downloading: {url} -> {filepath.name}")
                
                response = self.session.get(url, stream=True, timeout=30)
                response.raise_for_status()
                
                # Check if it's actually a PDF
                content_type = response.headers.get('content-type', '').lower()
                if 'pdf' not in content_type and not url.lower().endswith('.pdf'):
                    logging.warning(f"URL may not be a PDF: {url} (Content-Type: {content_type})")
                
                # Download the file
                with open(filepath, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                
                # Verify the file was downloaded
                if filepath.exists() and filepath.stat().st_size > 0:
                    logging.info(f"Successfully downloaded: {filepath.name} ({filepath.stat().st_size} bytes)")
                    return str(filepath)
                else:
                    logging.error(f"Downloaded file is empty or doesn't exist: {filepath}")
                    
            except requests.RequestException as e:
                logging.error(f"Attempt {attempt + 1} failed for {url}: {e}")
                if attempt < max_retries - 1:
                    time.sleep(5 * (attempt + 1))  # Exponential backoff
                
            except Exception as e:
                logging.error(f"Unexpected error downloading {url}: {e}")
                break
        
        return None
    
    def _search_for_pdfs(self, search_config: Dict) -> List[Tuple[str, str]]:
        """Search for PDFs on a webpage (basic implementation)."""
        url = search_config['url']
        search_terms = search_config.get('search_terms', [])
        
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            pdf_links = []
            for link in soup.find_all('a', href=True):
                href = link['href']
                
                # Check if it's a PDF link
                if href.lower().endswith('.pdf') or 'pdf' in href.lower():
                    # Check if link text contains search terms
                    link_text = link.get_text().lower()
                    if not search_terms or any(term.lower() in link_text for term in search_terms):
                        full_url = urljoin(url, href)
                        filename = os.path.basename(urlparse(href).path)
                        if not filename:
                            filename = f"document_{len(pdf_links)}.pdf"
                        pdf_links.append((full_url, filename))
            
            logging.info(f"Found {len(pdf_links)} PDF links on {url}")
            return pdf_links
            
        except Exception as e:
            logging.error(f"Error searching for PDFs on {url}: {e}")
            return []
    
    def _clean_filename(self, filename: str) -> str:
        """Clean filename for filesystem compatibility."""
        # Remove invalid characters
        filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
        # Limit length
        if len(filename) > 200:
            name, ext = os.path.splitext(filename)
            filename = name[:190] + ext
        return filename
    
    def get_download_summary(self) -> Dict:
        """Get summary of download session."""
        return {
            'total_downloaded': len(self.downloaded_files),
            'total_failed': len(self.failed_downloads),
            'downloaded_files': self.downloaded_files,
            'failed_downloads': self.failed_downloads
        }


def load_download_configs() -> List[Dict]:
    """Load download configurations."""
    # This will be loaded from the config file we'll create next
    from scripts.download_configs import DOWNLOAD_CONFIGS
    return DOWNLOAD_CONFIGS


def main():
    """Main download execution."""
    print("🤖 Starting PDF Download Process...")
    
    downloader = PDFDownloader()
    configs = load_download_configs()
    
    total_results = {
        'downloaded': [],
        'failed': [],
        'skipped': []
    }
    
    for config in configs:
        print(f"\n📁 Processing: {config['category']}/{config.get('manufacturer', 'general')}")
        results = downloader.download_from_config(config)
        
        # Merge results
        for key in total_results:
            total_results[key].extend(results[key])
        
        print(f"   ✅ Downloaded: {len(results['downloaded'])}")
        print(f"   ❌ Failed: {len(results['failed'])}")
    
    print(f"\n📊 Final Summary:")
    print(f"   Total Downloaded: {len(total_results['downloaded'])}")
    print(f"   Total Failed: {len(total_results['failed'])}")
    print(f"   Total Skipped: {len(total_results['skipped'])}")
    
    # Save summary
    summary = downloader.get_download_summary()
    with open('logs/download_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"\n📄 Download summary saved to: logs/download_summary.json")


if __name__ == "__main__":
    main()
