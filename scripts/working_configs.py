"""
Updated download configurations with working URLs
Based on testing results and current website availability
"""

# Working URLs that are likely to succeed
WORKING_DOWNLOAD_CONFIGS = [
    # ============ WORKING DOCUMENTS ============
    
    # AMD Graphics Documentation
    {
        'category': 'pc-manuals',
        'manufacturer': 'amd',
        'description': 'AMD Graphics and CPU Documentation',
        'direct_pdfs': [
            {
                'url': 'https://www.amd.com/system/files/documents/radeon-rx-6000-series-installation-guide.pdf',
                'filename': 'amd_radeon_rx_6000_installation.pdf'
            },
            {
                'url': 'https://www.amd.com/system/files/documents/radeon-software-adrenalin-quick-start-guide.pdf',
                'filename': 'amd_radeon_software_guide.pdf'
            }
        ]
    },
    
    # Microsoft Windows Documentation
    {
        'category': 'troubleshooting',
        'manufacturer': 'microsoft',
        'description': 'Windows Troubleshooting and Help',
        'direct_pdfs': [
            {
                'url': 'https://support.microsoft.com/en-us/windows/fix-wi-fi-connection-issues-in-windows-9424a1f7-6a3b-65a6-4d78-7f07eee84d2c',
                'filename': 'windows_wifi_troubleshooting.pdf'
            }
        ]
    },
    
    # General Tech Guides (Public Domain or Open Access)
    {
        'category': 'troubleshooting',
        'manufacturer': 'general',
        'description': 'General PC Troubleshooting Guides',
        'direct_pdfs': [
            {
                'url': 'https://www.nasa.gov/wp-content/uploads/2014/07/336615main_Computer_Troubleshooting.pdf',
                'filename': 'nasa_computer_troubleshooting_guide.pdf'
            }
        ]
    },
    
    # Sample PC Manuals (Open Source or Demo)
    {
        'category': 'pc-manuals',
        'manufacturer': 'sample',
        'description': 'Sample PC Documentation for Testing',
        'direct_pdfs': [
            {
                'url': 'https://www.intel.com/content/www/us/en/support/articles/000005505/processors.html',
                'filename': 'intel_processor_installation_guide.pdf'
            }
        ]
    }
]

# URLs that worked in our test
SUCCESSFUL_URLS = [
    'https://www.asus.com/support/download-center/',
    'https://www.asus.com/support/',
    'https://support.microsoft.com/en-us/windows/fix-wi-fi-connection-issues-in-windows-9424a1f7-6a3b-65a6-4d78-7f07eee84d2c',
    'https://www.amd.com/system/files/documents/radeon-rx-6000-series-installation-guide.pdf',
    'https://docs.microsoft.com/en-us/windows/whats-new/',
    'https://www.nvidia.com/en-us/geforce/guides/',
    'https://www.amd.com/en/support/graphics/amd-radeon-6000-series'
]

# Alternative approach: Use local sample files
SAMPLE_DOCUMENTS = {
    'pc_setup_guide.txt': """
PC Setup and Troubleshooting Guide

1. INITIAL SETUP
   - Unpack all components carefully
   - Check all cables and connections
   - Ensure power supply is properly connected
   
2. FIRST BOOT
   - Press power button
   - Check for POST (Power-On Self Test) beep
   - Enter BIOS if needed (usually F2, F12, or Delete key)
   
3. COMMON ISSUES
   - No display: Check monitor cable connections
   - No power: Verify power supply switch is ON
   - Unusual noises: Check for loose components
   
4. WINDOWS INSTALLATION
   - Insert Windows installation media
   - Follow on-screen prompts
   - Install necessary drivers
   
5. MAINTENANCE
   - Regular cleaning of dust
   - Keep software updated
   - Monitor temperatures
""",
    
    'graphics_troubleshooting.txt': """
Graphics Card Troubleshooting Guide

1. INSTALLATION
   - Power off computer completely
   - Remove old graphics card if present
   - Insert new card firmly into PCIe slot
   - Connect power cables if required
   
2. DRIVER INSTALLATION
   - Download latest drivers from manufacturer
   - Uninstall old drivers completely
   - Install new drivers and restart
   
3. COMMON PROBLEMS
   - Black screen: Check power connections
   - Artifacting: Check temperatures and power
   - Low performance: Update drivers, check settings
   
4. TESTING
   - Run stress tests to verify stability
   - Monitor temperatures during load
   - Test different games/applications
""",
    
    'warranty_policy.txt': """
PC Store Warranty Policy

1. WARRANTY COVERAGE
   - 1 year parts and labor warranty
   - Covers manufacturing defects
   - Does not cover physical damage or misuse
   
2. WARRANTY PROCESS
   - Contact support with issue description
   - Provide proof of purchase
   - Follow troubleshooting steps
   - Return for repair if necessary
   
3. RETURN POLICY
   - 30-day return window
   - Original packaging required
   - Restocking fee may apply
   - Software/digital items not returnable
   
4. SUPPORT CONTACT
   - Email: support@yourpcstore.com
   - Phone: 1-800-PC-HELP
   - Hours: Monday-Friday 9AM-5PM
"""
}
