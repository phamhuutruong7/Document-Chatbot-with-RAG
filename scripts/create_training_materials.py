#!/usr/bin/env python3
"""
Create customer service scenarios and training materials for PC support.
Generates realistic customer interactions, common problems, and solutions.
"""

import os
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def ensure_directory(path):
    """Ensure directory exists, create if it doesn't."""
    os.makedirs(path, exist_ok=True)

def create_customer_scenarios():
    """Create realistic customer service scenarios."""
    content = """CUSTOMER SERVICE SCENARIOS FOR PC SUPPORT
========================================

SCENARIO 1: FIRST-TIME BUYER
---------------------------
Customer Profile: Sarah, 28, work-from-home professional
Issue: Needs help choosing and setting up first desktop PC

Customer: "Hi, I work from home and need a reliable computer for video calls, 
document editing, and light photo editing. I've never bought a desktop before. 
What would you recommend?"

Support Response Strategy:
• Ask about budget range ($500-1500+ categories)
• Determine workspace constraints (desk size, monitor needs)
• Assess technical comfort level
• Recommend appropriate specs:
  - Intel i5 or AMD Ryzen 5 for productivity
  - 16GB RAM for multitasking
  - 256GB+ SSD for speed
  - Integrated graphics sufficient
• Offer setup service or detailed setup guide
• Explain warranty and support options

Follow-up Questions:
• "What's your budget range?"
• "Do you have a monitor, keyboard, and mouse?"
• "How comfortable are you with technology?"
• "Do you prefer pre-built or need help assembling?"

SCENARIO 2: GAMING ENTHUSIAST
----------------------------
Customer Profile: Mike, 22, college student and gamer
Issue: Wants high-performance gaming PC within budget

Customer: "I want to play the latest games at high settings, maybe do some 
streaming. I have about $1200 to spend. What can I get?"

Support Response Strategy:
• Focus on GPU as primary gaming component
• Balance CPU to avoid bottlenecks
• Emphasize upgradability for future
• Recommend:
  - RTX 4060 Ti or RX 7600 XT graphics
  - Intel i5-13400F or AMD Ryzen 5 7600X
  - 16GB DDR4/DDR5 RAM
  - 1TB NVMe SSD
  - Quality PSU for stability
• Discuss monitor requirements (1080p vs 1440p)
• Explain Ray Tracing and DLSS benefits

Gaming-Specific Advice:
• "What games do you play most?"
• "What monitor resolution do you prefer?"
• "Are you interested in streaming or content creation?"
• "Do you plan to upgrade components later?"

SCENARIO 3: ELDERLY CUSTOMER
---------------------------
Customer Profile: Robert, 68, retired, basic computer needs
Issue: Current PC is slow, needs simple replacement

Customer: "My computer takes forever to start up and crashes a lot. I just 
need something simple for email, web browsing, and storing photos."

Support Response Strategy:
• Emphasize simplicity and reliability
• Focus on ease of use over performance
• Recommend:
  - Intel i3 or AMD Ryzen 3 (adequate power)
  - 8GB RAM (sufficient for basic tasks)
  - 256GB SSD (fast boot times)
  - Integrated graphics (cost-effective)
  - Pre-installed Windows with setup service
• Offer extended warranty and support
• Provide clear, simple setup instructions

Elderly-Friendly Approach:
• Speak slowly and clearly
• Avoid technical jargon
• Offer hands-on demonstrations
• Provide written instructions
• Schedule follow-up check-ins

SCENARIO 4: SMALL BUSINESS OWNER
-------------------------------
Customer Profile: Lisa, 35, runs small marketing agency
Issue: Needs multiple PCs for office, budget-conscious

Customer: "I need 4 computers for my office. My employees do graphic design, 
web development, and video editing. What's the most cost-effective solution?"

Support Response Strategy:
• Discuss bulk pricing and business accounts
• Assess individual vs. shared resource needs
• Recommend tiered approach:
  - Workstation for video editing (high-end)
  - Mid-range for graphic design
  - Basic for admin tasks
• Consider warranty and business support
• Suggest network setup and shared storage

Business Considerations:
• "What's your total budget for all systems?"
• "Do you need immediate deployment or phased?"
• "What software will you be running?"
• "Do you need on-site support services?"

SCENARIO 5: STUDENT WITH BUDGET CONSTRAINTS
------------------------------------------
Customer Profile: Emma, 19, college student
Issue: Needs reliable PC for school, very limited budget

Customer: "I'm starting college and need a computer for writing papers, 
research, and online classes. I only have $400 to spend."

Support Response Strategy:
• Focus on essential functionality
• Consider refurbished options
• Recommend:
  - Budget AMD or Intel processor
  - 8GB RAM minimum
  - 256GB SSD (speed over capacity)
  - Integrated graphics adequate
  - Reliable brand with warranty
• Suggest student discounts
• Offer payment plan options

Budget-Friendly Options:
• Refurbished business computers
• Last-generation components
• Student pricing programs
• Extended payment plans
• Basic warranty coverage

SCENARIO 6: CREATIVE PROFESSIONAL
--------------------------------
Customer Profile: David, 30, freelance video editor
Issue: Needs powerful workstation for 4K video editing

Customer: "I edit 4K videos and do motion graphics. My current PC can't 
handle the workload. I need something that won't slow me down."

Support Response Strategy:
• Prioritize CPU and GPU for rendering
• Emphasize large, fast storage
• Recommend:
  - Intel i7/i9 or AMD Ryzen 7/9
  - 32GB+ RAM for large projects
  - Professional GPU (RTX 4070+)
  - Multiple NVMe SSDs for workflow
  - High-quality monitor support
• Discuss workflow optimization
• Consider RAID storage for backup

Creative Workflow Needs:
• "What video editing software do you use?"
• "What's your typical project file size?"
• "Do you work with multiple monitors?"
• "How important is color accuracy?"

SCENARIO 7: FAMILY COMPUTER
--------------------------
Customer Profile: Jennifer, 42, mother of three
Issue: Needs family-friendly PC for household use

Customer: "We need a computer the whole family can use. The kids do homework, 
my husband works on spreadsheets, and I manage our finances online."

Support Response Strategy:
• Balance performance with cost
• Emphasize durability and reliability
• Recommend:
  - Mid-range processor for multitasking
  - 16GB RAM for multiple users
  - Large storage for family files
  - Parental controls and security
  - Extended warranty for peace of mind
• Discuss user account setup
• Provide family-friendly software recommendations

Family-Specific Considerations:
• "How many people will use it regularly?"
• "What age range for the children?"
• "Do you need parental control software?"
• "What's your biggest concern about shared use?"

COMMON CUSTOMER OBJECTIONS
-------------------------

"It's too expensive"
Response: "I understand budget is important. Let me show you some alternatives 
that still meet your core needs. We also offer financing options and can 
prioritize the most important features for your situation."

"I don't understand the technical specs"
Response: "That's completely normal! Let me explain this in simple terms. 
Think of RAM as your desk space - more space means you can work on more 
things at once. The processor is like your brain speed - faster means 
everything happens quicker."

"I'm worried about it becoming outdated"
Response: "That's a valid concern. I'll recommend components that will stay 
relevant for 3-5 years for your use case. We can also discuss upgrade 
paths so you can improve performance later without replacing everything."

"I had bad experiences with computers before"
Response: "I'm sorry to hear that. Many issues come from not having the 
right specs for your needs. Let's make sure we get exactly what you need, 
and I'll explain our support options so you have help if anything comes up."

CUSTOMER SUCCESS METRICS
-----------------------

Satisfaction Indicators:
• Customer completes purchase confidently
• Understands product capabilities and limitations  
• Knows how to get support when needed
• Feels purchase meets their specific needs
• Would recommend store to others

Follow-up Checklist:
• Call within 48 hours of purchase
• Verify setup went smoothly
• Address any initial questions
• Remind about warranty terms
• Ask for feedback on sales process

© 2024 PC Customer Support Training Materials
"""
    return content

def create_troubleshooting_flowcharts():
    """Create systematic troubleshooting guides."""
    content = """PC TROUBLESHOOTING FLOWCHARTS
============================

FLOWCHART 1: PC WON'T START
---------------------------
START: Customer reports PC won't turn on

Step 1: Power Supply Check
├─ Is power cable connected? 
│  ├─ NO → Connect power cable → Try power button
│  └─ YES → Continue to Step 2
│
Step 2: Power Source Verification  
├─ Is outlet working?
│  ├─ NO → Try different outlet → Test again
│  └─ YES → Continue to Step 3
│
Step 3: Power Button Response
├─ Any lights/fans when pressing power?
│  ├─ NO → Continue to Step 4
│  └─ YES → Continue to Step 6
│
Step 4: Power Supply Unit (PSU) Test
├─ Try different power cable
├─ Check PSU switch (I/O position)
├─ Listen for PSU fan
│  ├─ No response → Replace PSU
│  └─ Some response → Continue to Step 5
│
Step 5: Motherboard Power Connections
├─ Check 24-pin motherboard connector
├─ Check 8-pin CPU power connector
├─ Reseat both connections firmly
│  └─ Test again → If still no response → Replace motherboard
│
Step 6: POST (Power-On Self-Test) Issues
├─ Fans spin but no display?
│  ├─ YES → Continue to Display Troubleshooting
│  └─ NO → Continue to Memory Test
│
Memory Test Procedure:
├─ Remove all RAM modules
├─ Install one module in slot 1
├─ Test boot → If successful, add modules one by one
├─ If single module fails → Try different module
└─ If all modules fail → Test different RAM slots

RESOLUTION PATHS:
• Power cable issue → 5 minutes, $0
• Outlet problem → Immediate, $0  
• PSU failure → 30 minutes, $80-150
• Motherboard failure → 45 minutes, $100-200
• RAM issue → 15 minutes, $50-150

FLOWCHART 2: SLOW PERFORMANCE
-----------------------------
START: Customer reports slow computer

Step 1: Startup Time Assessment
├─ How long to reach desktop?
│  ├─ >5 minutes → Critical issue, continue Step 2
│  ├─ 2-5 minutes → Moderate issue, continue Step 3  
│  └─ <2 minutes → Minor optimization, continue Step 4

Step 2: Critical Performance Issues
├─ Check hard drive health
│  ├─ Use CrystalDiskInfo or similar
│  ├─ Bad sectors/SMART errors? → Replace HDD/SSD
│  └─ Drive healthy → Continue Step 3
│
├─ Check memory usage
│  ├─ >80% usage at idle → Add more RAM
│  └─ Normal usage → Continue malware scan

Step 3: Moderate Performance Issues  
├─ Check startup programs
│  ├─ Task Manager → Startup tab
│  ├─ Disable unnecessary programs
│  └─ Restart and test improvement
│
├─ Run disk cleanup
│  ├─ Delete temporary files
│  ├─ Empty recycle bin
│  ├─ Clear browser cache
│  └─ Test performance

Step 4: General Optimization
├─ Windows Updates
│  ├─ Install pending updates
│  ├─ Update drivers
│  └─ Restart system
│
├─ Antivirus full scan
│  ├─ Run complete system scan
│  ├─ Remove detected threats
│  └─ Configure real-time protection

PERFORMANCE IMPROVEMENT TIMELINE:
• Startup program cleanup → 15 minutes, immediate improvement
• Disk cleanup → 30 minutes, moderate improvement  
• SSD upgrade → 45 minutes, dramatic improvement
• RAM upgrade → 20 minutes, significant improvement
• Fresh Windows install → 2-3 hours, maximum improvement

FLOWCHART 3: INTERNET CONNECTION ISSUES
--------------------------------------
START: Customer can't connect to internet

Step 1: Connection Type Identification
├─ Ethernet (wired) connection?
│  ├─ YES → Continue Ethernet troubleshooting
│  └─ NO → Continue Wi-Fi troubleshooting

ETHERNET TROUBLESHOOTING:
Step 2E: Physical Connection Check
├─ Cable firmly connected to PC and router?
│  ├─ NO → Reconnect both ends → Test
│  └─ YES → Continue Step 3E
│
Step 3E: Cable and Port Testing
├─ Try different ethernet cable
├─ Try different port on router  
├─ Check cable for damage
│  ├─ Problem resolved → Replace cable
│  └─ Still no connection → Continue Step 4E
│
Step 4E: Network Adapter Status
├─ Device Manager → Network Adapters
├─ Is ethernet adapter listed and enabled?
│  ├─ NO → Install/update drivers
│  └─ YES → Continue IP configuration
│
Step 5E: IP Configuration Reset
├─ Command Prompt (Admin)
├─ ipconfig /release
├─ ipconfig /flushdns
├─ ipconfig /renew
└─ Test connection

WI-FI TROUBLESHOOTING:
Step 2W: Wi-Fi Adapter Status  
├─ Is Wi-Fi turned on in Windows?
│  ├─ NO → Enable Wi-Fi → Continue Step 3W
│  └─ YES → Continue Step 3W
│
Step 3W: Network Visibility
├─ Can you see your network name?
│  ├─ NO → Router issue → Restart router
│  └─ YES → Continue Step 4W
│
Step 4W: Connection Authentication
├─ Enter correct Wi-Fi password
├─ Try "Forget" and reconnect to network
├─ Check for typing errors (case sensitive)
│  ├─ Connects but no internet → Continue Step 5W
│  └─ Won't connect → Continue Router troubleshooting

Step 5W: Internet Access Test
├─ Connected to Wi-Fi but no websites load?
├─ Try different websites (google.com, facebook.com)  
├─ Check DNS settings
│  ├─ Set DNS to 8.8.8.8 and 8.8.4.4
│  └─ Test again

ROUTER TROUBLESHOOTING:
├─ Unplug router for 30 seconds
├─ Plug back in, wait 2 minutes
├─ Test other devices (phone, tablet)
├─ If other devices work → PC network problem
└─ If no devices work → Contact ISP

FLOWCHART 4: BLUE SCREEN ERRORS (BSOD)
-------------------------------------
START: Customer gets blue screen crashes

Step 1: Error Information Collection
├─ Note the STOP code (e.g., 0x0000007E)
├─ Note any file names mentioned
├─ Record when crashes occur (startup, specific programs)
└─ Continue Step 2

Step 2: Recent Changes Assessment
├─ New hardware installed recently?
│  ├─ YES → Remove new hardware → Test stability
│  └─ NO → Continue Step 3
│
├─ New software/drivers installed?
│  ├─ YES → Uninstall recent software → Test
│  └─ NO → Continue Step 3

Step 3: Memory Test
├─ Boot from Windows Memory Diagnostic
├─ Run complete memory test (may take hours)
│  ├─ Errors found → Replace RAM modules
│  └─ No errors → Continue Step 4

Step 4: Driver Issues
├─ Boot into Safe Mode
├─ Check Device Manager for warning symbols
├─ Update all drivers, especially:
│  ├─ Graphics drivers
│  ├─ Network drivers  
│  ├─ Storage drivers
│  └─ Test stability in normal mode

Step 5: System File Check
├─ Command Prompt (Admin)
├─ sfc /scannow
├─ Wait for completion
│  ├─ Errors found and fixed → Restart and test
│  └─ Cannot fix some files → Continue Step 6

Step 6: Advanced Troubleshooting
├─ Check Event Viewer for detailed errors
├─ Run chkdsk /f on system drive
├─ Consider hardware testing:
│  ├─ CPU stress test
│  ├─ GPU stress test
│  └─ Hard drive health check

COMMON BSOD CAUSES:
• Faulty RAM → 40% of cases
• Driver conflicts → 30% of cases  
• Overheating → 15% of cases
• Hardware failure → 10% of cases
• Corrupt Windows files → 5% of cases

ESCALATION CRITERIA
==================

When to Escalate to Senior Technician:
├─ Hardware replacement needed >$200
├─ Customer requests manager
├─ Multiple failed troubleshooting attempts
├─ Suspected motherboard/CPU failure
└─ Data recovery situation

When to Schedule On-Site Visit:
├─ Customer uncomfortable with phone support
├─ Complex network setup required  
├─ Multiple computer setup
├─ Senior customer requesting assistance
└─ Business customer with downtime concerns

When to Recommend Replacement:
├─ Repair cost >60% of replacement cost
├─ Multiple component failures
├─ Computer >5 years old with major issues
├─ Customer expresses interest in upgrade
└─ Performance no longer meets needs

© 2024 PC Support Flowchart System
"""
    return content

def create_product_knowledge_base():
    """Create comprehensive product knowledge for customer service."""
    content = """PRODUCT KNOWLEDGE BASE FOR PC SALES
==================================

PROCESSOR GUIDE FOR CUSTOMERS
-----------------------------

INTEL PROCESSOR LINEUP:
Intel i3 Series (Budget-Friendly):
• Target: Basic computing, office work, web browsing
• Cores: 4-6 cores
• Speed: 3.0-4.0 GHz
• Best for: Students, elderly users, basic business
• Price range: $100-200
• Customer explanation: "Like a reliable economy car - gets the job done efficiently for everyday tasks"

Intel i5 Series (Mainstream):
• Target: Gaming, productivity, multitasking
• Cores: 6-10 cores  
• Speed: 3.0-4.5 GHz
• Best for: Most home users, gamers, professionals
• Price range: $200-400
• Customer explanation: "Like a well-rounded sedan - powerful enough for most anything you'll need"

Intel i7 Series (High Performance):
• Target: Content creation, heavy multitasking, high-end gaming
• Cores: 8-12 cores
• Speed: 3.0-5.0 GHz
• Best for: Video editors, streamers, power users
• Price range: $300-600
• Customer explanation: "Like a sports car - built for performance and handling demanding tasks"

Intel i9 Series (Enthusiast):
• Target: Professional workstations, extreme gaming
• Cores: 12-24 cores
• Speed: 3.0-5.5 GHz
• Best for: 3D rendering, professional video editing, extreme multitasking
• Price range: $500-1500
• Customer explanation: "Like a high-end sports car - maximum power for the most demanding users"

AMD PROCESSOR LINEUP:
AMD Ryzen 3 (Budget):
• Equivalent to Intel i3
• Great value proposition
• Lower power consumption
• Integrated graphics available

AMD Ryzen 5 (Mainstream):
• Equivalent to Intel i5
• Often better multitasking than Intel
• Popular for gaming builds
• Excellent price-performance ratio

AMD Ryzen 7 (High Performance):
• Equivalent to Intel i7
• Strong content creation performance
• Good for streaming while gaming
• Competitive pricing vs Intel

AMD Ryzen 9 (Enthusiast):
• Equivalent to Intel i9
• Excellent for workstation tasks
• High core counts
• Professional content creation

GRAPHICS CARD GUIDE
------------------

INTEGRATED GRAPHICS:
Intel UHD/Iris Xe:
• Built into Intel processors
• Good for: Office work, web browsing, light gaming
• Cannot play: Modern AAA games at high settings
• Cost: $0 (included with processor)
• Customer explanation: "Like having a basic camera on your phone - fine for everyday use"

AMD Radeon (Integrated):
• Built into AMD processors
• Slightly better gaming than Intel integrated
• Good for: Casual gaming, productivity
• 1080p gaming on older/less demanding titles

DEDICATED GRAPHICS CARDS:

Budget Gaming ($150-300):
• NVIDIA GTX 1660 / RTX 3050
• AMD RX 6500 XT / RX 6600
• Good for: 1080p gaming at medium-high settings
• Can play: Most modern games at 60fps
• Customer explanation: "Like upgrading from a basic camera to a good smartphone camera"

Mid-Range Gaming ($300-600):
• NVIDIA RTX 4060 / RTX 4060 Ti
• AMD RX 7600 / RX 7700 XT  
• Good for: 1080p high settings, 1440p medium settings
• Features: Ray tracing, DLSS/FSR support
• Customer explanation: "Like getting a professional camera - great quality for most uses"

High-End Gaming ($600-1000):
• NVIDIA RTX 4070 / RTX 4070 Ti
• AMD RX 7800 XT / RX 7900 GRE
• Good for: 1440p high settings, 4K medium settings
• Features: Advanced ray tracing, high refresh rate gaming

Enthusiast Gaming ($1000+):
• NVIDIA RTX 4080 / RTX 4090
• AMD RX 7900 XTX
• Good for: 4K gaming, VR, content creation
• Customer explanation: "Like professional studio equipment - top performance for serious users"

MEMORY (RAM) GUIDE
-----------------

8GB RAM:
• Minimum for Windows 11
• Good for: Basic computing, light multitasking
• Limitations: May slow down with many browser tabs
• Price: $40-60
• Customer explanation: "Like having a small desk - fine for simple tasks"

16GB RAM:
• Sweet spot for most users
• Good for: Gaming, productivity, moderate multitasking
• Handles: Multiple apps, many browser tabs, light content creation
• Price: $60-100
• Customer explanation: "Like having a properly sized desk - room for everything you need"

32GB RAM:
• Power user territory
• Good for: Content creation, heavy multitasking, professional work
• Handles: Video editing, 3D rendering, virtual machines
• Price: $120-200
• Customer explanation: "Like having a huge desk - space for any project"

64GB+ RAM:
• Professional workstations only
• Good for: Server applications, extreme content creation
• Price: $300+
• Customer explanation: "Like having an entire office - for specialized professional needs"

STORAGE GUIDE
------------

HARD DISK DRIVES (HDD):
• Capacity: 1TB-8TB+
• Speed: Slower (mechanical)
• Price: $50-200
• Best for: Mass storage, backup, older files
• Customer explanation: "Like a large filing cabinet - lots of space but takes time to find things"

SOLID STATE DRIVES (SSD):
• Capacity: 256GB-4TB
• Speed: Very fast (no moving parts)
• Price: $30-400
• Best for: Operating system, programs, frequently used files
• Customer explanation: "Like having everything organized on your desk - instant access"

NVME SSD (High-Speed SSD):
• Capacity: 256GB-2TB
• Speed: Extremely fast
• Price: $40-300
• Best for: Gaming, content creation, professional work
• Customer explanation: "Like having a super-organized assistant - everything appears instantly"

STORAGE RECOMMENDATIONS:
Basic User: 256GB SSD + 1TB HDD
Gamer: 512GB NVMe SSD + 2TB HDD
Content Creator: 1TB NVMe SSD + 4TB HDD
Professional: 2TB NVMe SSD (primary) + additional storage as needed

CUSTOMER CONVERSATION STARTERS
-----------------------------

"What will you primarily use the computer for?"
• Work/productivity → i5 processor, 16GB RAM, SSD
• Gaming → i5/i7, dedicated graphics, NVMe SSD
• Basic use → i3, 8GB RAM, SSD + HDD
• Content creation → i7/i9, 32GB RAM, high-end graphics

"What's your budget range?"
• Under $500 → Refurbished or basic new system
• $500-800 → Solid mainstream system
• $800-1200 → Good gaming or professional system
• $1200+ → High-end gaming or workstation

"Do you have any brand preferences?"
• "I like Dell" → Show Dell options first, compare with others
• "I heard AMD is good" → Explain AMD advantages, show Intel alternatives
• "I want the best" → Focus on high-end options, explain value

"How long do you want this computer to last?"
• 2-3 years → Budget build, plan for replacement
• 4-5 years → Mainstream build with upgrade potential
• 5+ years → High-end build, future-proofing investment

HANDLING PRICE OBJECTIONS
------------------------

"That's more than I wanted to spend":
• "I understand budget is important. Let me show you how we can prioritize the features most important to you."
• Break down cost by component value
• Offer financing options
• Show refurbished alternatives
• Explain cost per day over lifespan

"I can build it cheaper myself":
• "You're right that individual parts might cost less. Our systems include assembly, testing, warranty, and support."
• Explain time value and technical expertise required
• Highlight warranty coverage and support
• Offer competitive pricing on custom builds

"My old computer was only $300":
• "Computer prices have changed due to improved performance and inflation."
• Compare capabilities: "Your old computer couldn't do [specific modern task]"
• Show value in terms of productivity and frustration savings
• Explain technology improvements

VALUE PROPOSITIONS
-----------------

For Students:
• "This system will handle all your coursework and last through graduation"
• Emphasize reliability and support
• Mention student discounts
• Focus on multitasking for research and assignments

For Gamers:
• "You'll get smooth frame rates in current games and be ready for new releases"
• Emphasize graphics performance and upgradability
• Mention VR readiness if applicable
• Focus on competitive advantage

For Professionals:
• "This system will increase your productivity and pay for itself"
• Emphasize time savings and reliability
• Focus on professional software compatibility
• Highlight business support options

For Families:
• "This system will handle everyone's needs and grow with your family"
• Emphasize durability and multiple user support
• Focus on educational value for children
• Highlight parental controls and security

© 2024 PC Sales Product Knowledge System
"""
    return content

def main():
    """Create all customer service training materials."""
    # Set up directories
    base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "documents")
    training_dir = os.path.join(base_dir, "training")
    
    ensure_directory(training_dir)
    
    # Create training documents
    documents = [
        ("customer_scenarios.txt", create_customer_scenarios()),
        ("troubleshooting_flowcharts.txt", create_troubleshooting_flowcharts()),
        ("product_knowledge_base.txt", create_product_knowledge_base()),
    ]
    
    logger.info("👥 Creating customer service training materials...")
    
    for filename, content in documents:
        filepath = os.path.join(training_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        file_size = len(content.encode('utf-8'))
        logger.info(f"✅ Created {filename} ({file_size:,} bytes)")
    
    logger.info(f"🎉 Successfully created {len(documents)} training documents!")
    logger.info("📍 Documents saved to: data/documents/training/")
    
    # Create summary
    total_size = sum(len(content.encode('utf-8')) for _, content in documents)
    print(f"\n📊 CUSTOMER SERVICE TRAINING SUMMARY")
    print(f"=" * 50)
    print(f"📁 Documents Created: {len(documents)}")
    print(f"💾 Total Size: {total_size:,} bytes ({total_size/1024:.1f} KB)")
    print(f"👥 Training Areas: Customer Scenarios, Troubleshooting, Product Knowledge")
    
    print(f"\n🎯 TRAINING COVERAGE:")
    print(f"   ✅ Customer persona handling")
    print(f"   ✅ Systematic troubleshooting")
    print(f"   ✅ Product specifications guide")
    print(f"   ✅ Sales objection handling")
    print(f"   ✅ Technical support workflows")
    print(f"   ✅ Value proposition strategies")
    
    print(f"\n📚 CUSTOMER SCENARIOS INCLUDED:")
    print(f"   • First-time buyer guidance")
    print(f"   • Gaming enthusiast consultation")
    print(f"   • Elderly customer support")
    print(f"   • Small business solutions")
    print(f"   • Student budget options")
    print(f"   • Creative professional needs")
    print(f"   • Family computer selection")
    
    print(f"\n🔧 TROUBLESHOOTING FLOWCHARTS:")
    print(f"   • PC won't start diagnosis")
    print(f"   • Slow performance analysis")
    print(f"   • Internet connection issues")
    print(f"   • Blue screen error handling")
    print(f"   • Escalation procedures")
    
    print(f"\n💡 PRODUCT KNOWLEDGE AREAS:")
    print(f"   • Processor comparison (Intel/AMD)")
    print(f"   • Graphics card recommendations")
    print(f"   • Memory (RAM) guidance")
    print(f"   • Storage options explanation")
    print(f"   • Price objection handling")

if __name__ == "__main__":
    main()
