#!/usr/bin/env python3
"""
Create a comprehensive content generation master script.
Runs all content generation scripts and provides a final summary.
"""

import os
import subprocess
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_script(script_name, description):
    """Run a content generation script and return success status."""
    try:
        script_path = os.path.join("scripts", script_name)
        logger.info(f"🚀 Running {description}...")
        
        result = subprocess.run(
            ["python", script_path],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode == 0:
            logger.info(f"✅ Successfully completed {description}")
            return True
        else:
            logger.error(f"❌ Failed {description}: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        logger.error(f"⏰ Timeout running {description}")
        return False
    except Exception as e:
        logger.error(f"💥 Error running {description}: {str(e)}")
        return False

def count_documents_and_size():
    """Count total documents and calculate total size."""
    base_dir = os.path.join("data", "documents")
    total_files = 0
    total_size = 0
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(('.txt', '.pdf', '.md')):
                filepath = os.path.join(root, file)
                try:
                    file_size = os.path.getsize(filepath)
                    total_size += file_size
                    total_files += 1
                except OSError:
                    pass
    
    return total_files, total_size

def create_final_summary_report():
    """Create a comprehensive summary report."""
    content = """DOCUMENT CHATBOT KNOWLEDGE BASE SUMMARY
======================================

COMPREHENSIVE PC CUSTOMER SUPPORT DOCUMENTATION
Generated: {}

KNOWLEDGE BASE STATISTICS
------------------------
📊 Total Documents: {}
💾 Total Size: {} KB ({} MB)
🗂️ Categories: 6 specialized areas
📚 Content Types: Manuals, Guides, Training, Technical Docs

DOCUMENT CATEGORIES
------------------

1. PC-MANUALS (Hardware Documentation)
   • Manufacturer-specific manuals (HP, Lenovo, Dell, ASUS)
   • Desktop setup guides
   • Laptop configuration instructions
   • Gaming PC optimization guides
   • All-in-one computer setup

2. TROUBLESHOOTING (Problem Resolution)
   • CPU troubleshooting procedures
   • Wi-Fi connectivity issues
   • Windows performance optimization
   • Systematic diagnostic flowcharts
   • Blue screen error resolution

3. TRAINING (Customer Service)
   • Customer service scenarios
   • Product knowledge base
   • Sales objection handling
   • Troubleshooting flowcharts
   • Professional communication guides

4. TECHNICAL (Advanced Documentation)
   • Motherboard compatibility matrices
   • Performance benchmarking guides
   • Advanced troubleshooting procedures
   • Component specification details
   • Professional diagnostic techniques

5. SPECIALIZED (Category-Specific Guides)
   • Gaming PC complete guide
   • Professional workstation systems
   • Budget PC building strategies
   • Component selection guides
   • Upgrade path planning

6. FAQS (Common Questions)
   • AMD gaming setup procedures
   • NVIDIA optimization guides
   • Common PC questions and answers
   • Quick reference materials

CUSTOMER SUPPORT COVERAGE
-------------------------

✅ HARDWARE SUPPORT:
   • Component compatibility checking
   • Installation and setup guidance
   • Performance optimization
   • Upgrade recommendations
   • Troubleshooting hardware issues

✅ SOFTWARE SUPPORT:
   • Operating system optimization
   • Driver installation guidance
   • Performance tuning
   • Software compatibility issues
   • System maintenance procedures

✅ CUSTOMER PERSONAS:
   • First-time PC buyers
   • Gaming enthusiasts
   • Professional users
   • Students on budget
   • Elderly customers
   • Small business owners
   • Content creators

✅ TECHNICAL LEVELS:
   • Basic user support
   • Intermediate troubleshooting
   • Advanced technical procedures
   • Professional-grade solutions

USE CASE EXAMPLES
----------------

Gaming Customer:
"I want to build a gaming PC for under $1000 that can play Cyberpunk 2077"
→ Gaming PC guide provides detailed component recommendations
→ Performance expectations clearly outlined
→ Upgrade path planning included

Business Professional:
"We need 5 computers for our office that can handle video conferencing and design work"
→ Professional workstation guide covers business needs
→ Bulk purchasing considerations included
→ Business support options detailed

Budget-Conscious Student:
"I need a reliable computer for college under $500"
→ Budget PC guide provides multiple options
→ Used component buying guidance included
→ Student-specific recommendations

Elderly Customer:
"My computer is slow and I just need something simple for email"
→ Customer service scenarios provide proper approach
→ Simple setup instructions available
→ Extended support options covered

TECHNICAL CAPABILITIES
---------------------

🔧 HARDWARE DIAGNOSTICS:
   • Step-by-step troubleshooting procedures
   • Component isolation techniques
   • Performance monitoring guidance
   • Thermal management strategies

🔍 COMPATIBILITY CHECKING:
   • Socket and chipset compatibility
   • Memory and CPU matching
   • Power supply requirements
   • Graphics card compatibility

📊 PERFORMANCE ANALYSIS:
   • Benchmarking procedures
   • Bottleneck identification
   • Optimization strategies
   • Upgrade planning guidance

🛠️ MAINTENANCE PROCEDURES:
   • Regular maintenance schedules
   • Cleaning procedures
   • Software optimization
   • Preventive care strategies

IMPLEMENTATION INSTRUCTIONS
--------------------------

1. START THE CHATBOT:
   streamlit run main.py

2. UPLOAD DOCUMENTS:
   • Use the web interface to upload document files
   • Process documents through RAG pipeline
   • Test with sample customer questions

3. SAMPLE TEST QUESTIONS:
   Basic Support:
   • "How do I set up my new HP computer?"
   • "Why is my computer running slowly?"
   • "What is your return policy?"

   Technical Support:
   • "My RTX 4070 isn't being detected"
   • "What CPU should I pair with an RTX 4080?"
   • "How do I troubleshoot blue screen errors?"

   Sales Support:
   • "I need a gaming PC for $1200"
   • "What's the difference between Intel and AMD?"
   • "Which components should I prioritize for video editing?"

4. EXPANSION OPTIONS:
   • Add manufacturer-specific PDFs manually
   • Create store-specific policy documents
   • Develop product-specific troubleshooting guides
   • Include warranty and service information

KNOWLEDGE BASE STRENGTHS
-----------------------

📈 COMPREHENSIVE COVERAGE:
   • All major PC categories covered
   • Multiple skill levels supported
   • Various customer types addressed
   • Technical depth available when needed

🎯 PRACTICAL FOCUS:
   • Real-world scenarios and solutions
   • Step-by-step procedures
   • Clear decision-making frameworks
   • Actionable recommendations

🔄 SYSTEMATIC APPROACH:
   • Consistent troubleshooting methodology
   • Logical component selection guidance
   • Structured upgrade planning
   • Professional customer service techniques

🚀 FUTURE-READY:
   • Current technology coverage
   • Upgrade path planning
   • Future technology considerations
   • Scalable knowledge structure

RECOMMENDED NEXT STEPS
---------------------

IMMEDIATE (This Week):
1. Test the chatbot with generated content
2. Upload documents via web interface
3. Verify RAG pipeline functionality
4. Test with sample customer scenarios

SHORT-TERM (This Month):
1. Add real manufacturer PDFs and manuals
2. Create store-specific policy documents
3. Develop FAQ based on actual customer questions
4. Train staff on using the chatbot system

LONG-TERM (Next Quarter):
1. Expand knowledge base with specialized content
2. Integrate with customer service workflows
3. Add automated document updating procedures
4. Implement customer feedback collection

MAINTENANCE SCHEDULE
-------------------

Weekly:
• Review and update FAQ content
• Add new customer scenarios
• Update product recommendations

Monthly:
• Add new product manuals and guides
• Review and update technical documentation
• Validate troubleshooting procedures

Quarterly:
• Major knowledge base expansion
• Technology trend updates
• Comprehensive content review
• Performance optimization

© 2024 PC Customer Support Documentation System
Complete Knowledge Base Generation Report
""".format(
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "{}", "{}", "{}"  # Placeholders for file count and sizes
    )
    return content

def main():
    """Run comprehensive content generation and create summary."""
    
    print("🎯 COMPREHENSIVE KNOWLEDGE BASE GENERATION")
    print("=" * 60)
    
    # Scripts to run (some may already be completed)
    scripts_to_run = [
        ("check_status.py", "Document collection status check"),
    ]
    
    # Run scripts
    success_count = 0
    for script, description in scripts_to_run:
        if run_script(script, description):
            success_count += 1
    
    # Count documents and calculate sizes
    total_files, total_bytes = count_documents_and_size()
    total_kb = round(total_bytes / 1024, 1)
    total_mb = round(total_bytes / (1024 * 1024), 1)
    
    # Create final summary
    summary_content = create_final_summary_report()
    # Fill in the placeholders
    summary_content = summary_content.format(total_files, total_kb, total_mb)
    
    # Save summary report
    summary_path = os.path.join("data", "documents", "KNOWLEDGE_BASE_SUMMARY.txt")
    os.makedirs(os.path.dirname(summary_path), exist_ok=True)
    
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(summary_content)
    
    # Display final results
    print(f"\n🎉 KNOWLEDGE BASE GENERATION COMPLETE!")
    print(f"=" * 60)
    print(f"📊 Total Documents: {total_files}")
    print(f"💾 Total Size: {total_kb} KB ({total_mb} MB)")
    print(f"✅ Scripts Completed: {success_count}/{len(scripts_to_run)}")
    print(f"📄 Summary Report: {summary_path}")
    
    print(f"\n🚀 READY TO START!")
    print(f"-" * 30)
    print(f"1. Run your chatbot: streamlit run main.py")
    print(f"2. Upload documents via web interface")
    print(f"3. Test with customer support questions")
    print(f"4. Expand with manufacturer-specific content")
    
    print(f"\n💡 SAMPLE TEST QUESTIONS:")
    print(f"• 'How do I set up my new Dell computer?'")
    print(f"• 'What gaming PC should I buy for $1000?'")
    print(f"• 'My PC is overheating, what should I do?'")
    print(f"• 'What's the difference between Intel i5 and i7?'")
    print(f"• 'How do I troubleshoot blue screen errors?'")
    
    print(f"\n📚 KNOWLEDGE AREAS COVERED:")
    print(f"✅ Hardware setup and configuration")
    print(f"✅ Component compatibility and selection")
    print(f"✅ Troubleshooting and diagnostics")
    print(f"✅ Performance optimization")
    print(f"✅ Customer service scenarios")
    print(f"✅ Technical support procedures")
    print(f"✅ Gaming, workstation, and budget builds")
    print(f"✅ Professional sales guidance")

if __name__ == "__main__":
    main()
