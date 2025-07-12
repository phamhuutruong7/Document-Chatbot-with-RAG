"""
Generate sample PC documentation for testing the RAG system
This creates realistic sample documents that you can use immediately
"""

import os
from pathlib import Path

def create_sample_documents():
    """Create sample PC documentation files."""
    
    # Ensure directories exist
    base_dir = Path("data/documents")
    
    # Sample documents with realistic PC support content
    documents = {
        # PC Manuals
        "pc-manuals/dell/dell_optiplex_setup_guide.txt": """
Dell OptiPlex Desktop Setup Guide

PACKAGE CONTENTS:
- OptiPlex desktop computer
- Power cable
- Keyboard and mouse
- Quick setup guide
- Warranty information

INITIAL SETUP:
1. Connect monitor cable to graphics port
2. Connect keyboard and mouse to USB ports
3. Connect power cable to computer and wall outlet
4. Press power button to start

FIRST BOOT:
- System will perform initial setup
- Follow Windows configuration wizard
- Create user account and password
- Connect to Wi-Fi if needed

SPECIFICATIONS:
- Processor: Intel Core i5
- Memory: 8GB DDR4 RAM
- Storage: 256GB SSD
- Graphics: Intel UHD Graphics
- Ports: 6x USB, 2x DisplayPort, 1x HDMI

TROUBLESHOOTING:
- No display: Check monitor cable connections
- Won't turn on: Verify power cable connections
- Slow performance: Close unnecessary programs
- No internet: Check network cable or Wi-Fi settings

SUPPORT:
For technical support, visit dell.com/support or call 1-800-DELL-HELP
Warranty covers parts and labor for 1 year from purchase date.
""",

        "pc-manuals/hp/hp_pavilion_gaming_setup.txt": """
HP Pavilion Gaming Desktop Setup

GAMING FEATURES:
- NVIDIA GTX graphics card
- RGB LED lighting effects
- Enhanced cooling system
- Gaming keyboard and mouse included

SETUP INSTRUCTIONS:
1. Remove all packaging materials carefully
2. Place computer on stable, ventilated surface
3. Connect monitor to graphics card (NOT motherboard)
4. Connect all USB peripherals
5. Connect power and press power button

GRAPHICS CARD SETUP:
- Download NVIDIA GeForce Experience
- Install latest graphics drivers
- Optimize game settings automatically
- Enable G-SYNC for compatible monitors

PERFORMANCE OPTIMIZATION:
- Enable Game Mode in Windows settings
- Close background applications while gaming
- Monitor CPU and GPU temperatures
- Keep drivers updated regularly

COOLING SYSTEM:
- Three intake fans and one exhaust fan
- CPU liquid cooling system included
- Monitor temperatures with HP Command Center
- Clean dust filters monthly

COMMON GAMING ISSUES:
- Low FPS: Update graphics drivers
- Game crashes: Check for overheating
- Audio issues: Update audio drivers
- Controller not working: Install controller software

RGB LIGHTING:
- Use HP Omen Gaming Hub to control lighting
- Customize colors and effects
- Sync with compatible peripherals
- Create profiles for different games
""",

        # Troubleshooting Guides
        "troubleshooting/hardware/cpu_troubleshooting.txt": """
CPU Troubleshooting Guide

COMMON CPU PROBLEMS:

1. OVERHEATING:
Symptoms: Random shutdowns, blue screens, throttling
Solutions:
- Check CPU cooler mounting
- Replace thermal paste
- Verify fan operation
- Improve case airflow
- Check ambient temperature

2. HIGH CPU USAGE:
Symptoms: Slow performance, fan noise, heat
Solutions:
- Check Task Manager for running processes
- End unnecessary background tasks
- Scan for malware/viruses
- Update device drivers
- Check for Windows updates

3. CPU NOT DETECTED:
Symptoms: No boot, no display, diagnostic beeps
Solutions:
- Reseat CPU in socket
- Check for bent pins (Intel)
- Verify power connections
- Clear CMOS/BIOS settings
- Test with known good CPU

4. BLUE SCREEN ERRORS:
Symptoms: System crashes with blue screen
Solutions:
- Check CPU temperatures
- Test system memory
- Update BIOS firmware
- Reset to default settings
- Run hardware diagnostics

5. POOR PERFORMANCE:
Symptoms: Slow system response
Solutions:
- Check CPU utilization in Task Manager
- Verify correct CPU speed in BIOS
- Update chipset drivers
- Check for thermal throttling
- Disable power saving modes

TEMPERATURE MONITORING:
- Normal idle: 30-50°C
- Normal load: 60-80°C
- Dangerous: Above 85°C
- Use HWMonitor or Core Temp software

PREVENTIVE MAINTENANCE:
- Clean dust from cooler monthly
- Replace thermal paste annually
- Monitor temperatures regularly
- Keep BIOS updated
- Ensure adequate case ventilation
""",

        "troubleshooting/software/windows_performance.txt": """
Windows Performance Troubleshooting

SLOW STARTUP ISSUES:

1. DISABLE STARTUP PROGRAMS:
- Press Ctrl+Shift+Esc to open Task Manager
- Click Startup tab
- Disable unnecessary programs
- Focus on high impact items

2. RUN DISK CLEANUP:
- Type 'Disk Cleanup' in Start menu
- Select system drive (usually C:)
- Check all boxes and click OK
- Run 'Clean up system files' for more options

3. CHECK FOR MALWARE:
- Run Windows Defender full scan
- Use Malwarebytes for additional scanning
- Keep antivirus definitions updated
- Avoid suspicious downloads and emails

SYSTEM RESPONSIVENESS:

1. OPTIMIZE VISUAL EFFECTS:
- Right-click This PC > Properties
- Click Advanced system settings
- Under Performance, click Settings
- Select 'Adjust for best performance'

2. MANAGE VIRTUAL MEMORY:
- Same Advanced system settings window
- Click Change under Virtual memory
- Set custom size: Initial = RAM size, Maximum = 2x RAM
- Apply changes and restart

3. UPDATE DRIVERS:
- Right-click Start button > Device Manager
- Look for devices with warning icons
- Right-click and select 'Update driver'
- Use Windows Update or manufacturer websites

STORAGE OPTIMIZATION:

1. FREE UP DISK SPACE:
- Delete temporary files
- Empty Recycle Bin
- Remove old downloads
- Uninstall unused programs

2. DEFRAGMENT HARD DRIVES:
- Type 'Defragment' in Start menu
- Select drive and click Optimize
- Note: Don't defragment SSDs

3. CHECK DISK ERRORS:
- Open Command Prompt as administrator
- Type: chkdsk C: /f /r
- Press Y when prompted
- Restart computer to run check

NETWORK PERFORMANCE:
- Reset network adapters
- Update network drivers
- Check for interference
- Use Ethernet instead of Wi-Fi when possible
""",

        # FAQs
        "faqs/general/common_pc_questions.txt": """
Frequently Asked Questions - PC Support

Q: My computer won't turn on. What should I check?
A: First, verify the power cable is securely connected to both the computer and wall outlet. Check if the power supply switch (if present) is in the ON position. Try a different power outlet. If using a power strip, ensure it's turned on. Look for any LED lights on the motherboard or power button.

Q: Why is my computer running slowly?
A: Common causes include too many startup programs, insufficient RAM, full hard drive, malware infection, or outdated drivers. Try restarting, running disk cleanup, checking for viruses, and updating Windows and drivers.

Q: How often should I clean my computer?
A: Clean dust from your computer every 3-6 months, or more frequently in dusty environments. Use compressed air to blow out dust from fans, heat sinks, and vents. Always power off and unplug before cleaning.

Q: What's the difference between sleep mode and hibernate?
A: Sleep mode keeps your session in RAM and uses minimal power, allowing quick wake-up. Hibernate saves your session to the hard drive and uses no power, but takes longer to resume. Use sleep for short breaks, hibernate for longer periods.

Q: How do I know if I need more RAM?
A: Check Task Manager's Performance tab. If memory usage is consistently above 80%, you may benefit from more RAM. Signs include slow performance, long loading times, and frequent hard drive activity.

Q: Why does my computer get hot?
A: Heat is normal during operation, but excessive heat indicates problems. Check that fans are working, vents aren't blocked, and thermal paste on the CPU is adequate. High CPU usage from running programs also generates heat.

Q: What should I do if I spill liquid on my computer?
A: Immediately power off and unplug the computer. Remove the battery if it's a laptop. Don't turn it on until completely dry (24-48 hours). For keyboards, remove keys and clean underneath. Consider professional cleaning for motherboards.

Q: How do I back up my important files?
A: Use external drives, cloud storage (OneDrive, Google Drive), or Windows backup features. The 3-2-1 rule: 3 copies of important data, 2 different storage types, 1 offsite backup.

Q: When should I replace my computer?
A: Consider replacement when repair costs exceed 50% of a new computer's price, when it can't run required software, or when it's over 5-7 years old and experiencing frequent problems.

Q: How do I choose between repair and replacement?
A: Factors include age of computer, cost of repair, availability of parts, your budget, and current performance needs. Generally, repairs are cost-effective for computers under 4 years old.
""",

        # Policies
        "policies/general/warranty_and_returns.txt": """
PC Store Warranty and Return Policy

WARRANTY COVERAGE:

Standard Warranty:
- Parts and labor: 1 year from purchase date
- Covers manufacturing defects and component failures
- Includes free diagnostic services
- Covers replacement parts and installation labor

Extended Warranty Available:
- 2-year or 3-year options
- Covers accidental damage (additional cost)
- Includes annual maintenance check
- Priority repair service

What's NOT Covered:
- Physical damage from drops, spills, or misuse
- Damage from power surges (unless surge protector was purchased)
- Software issues or virus infections
- Cosmetic damage that doesn't affect function
- Normal wear and tear

RETURN POLICY:

30-Day Return Window:
- Full refund if returned within 30 days
- Original packaging and accessories required
- Must be in like-new condition
- Receipt or proof of purchase required

Restocking Fees:
- Custom-built systems: 15% restocking fee
- Opened software: Not returnable
- Special order items: 25% restocking fee
- No restocking fee for defective items

Return Process:
1. Contact customer service for return authorization
2. Pack item securely in original packaging
3. Include all accessories and documentation
4. Return to store or ship with provided label
5. Refund processed within 5-7 business days

SUPPORT SERVICES:

Free Services:
- Hardware diagnostic testing
- Basic software troubleshooting
- Driver installation assistance
- Warranty claim processing

Paid Services:
- Data recovery: $50-200 depending on complexity
- Virus removal: $75
- Operating system installation: $100
- Hardware upgrades: $50 labor + parts cost
- House calls: $150 + mileage

CONTACT INFORMATION:

Customer Service:
- Phone: 1-800-PC-STORE (1-800-727-8673)
- Email: support@pcstore.com
- Live chat: Available on website 9AM-6PM EST

Store Hours:
- Monday-Friday: 9:00 AM - 8:00 PM
- Saturday: 10:00 AM - 6:00 PM
- Sunday: 12:00 PM - 5:00 PM

Technical Support:
- Phone support: Available during store hours
- Remote assistance: By appointment
- In-store consultations: Free with purchase

This warranty is in addition to any manufacturer warranties and does not affect your statutory rights.
"""
    }
    
    # Create all sample documents
    created_files = []
    
    for file_path, content in documents.items():
        full_path = base_dir / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        created_files.append(full_path)
        print(f"✅ Created: {file_path}")
    
    return created_files

def main():
    """Main function to create sample documents."""
    
    print("🗂️  Creating Sample PC Documentation")
    print("=" * 50)
    
    try:
        created_files = create_sample_documents()
        
        print(f"\n✅ Successfully created {len(created_files)} sample documents!")
        print(f"\n📁 Files created in: data/documents/")
        print(f"\n📋 Document categories:")
        print(f"   - PC Manuals (Dell, HP)")
        print(f"   - Troubleshooting Guides (Hardware, Software)")
        print(f"   - FAQs (Common Questions)")
        print(f"   - Policies (Warranty, Returns)")
        
        print(f"\n🔄 Next steps:")
        print(f"   1. Run your main app: streamlit run main.py")
        print(f"   2. Upload these documents through the interface")
        print(f"   3. Test with questions like:")
        print(f"      - 'How do I set up a Dell OptiPlex?'")
        print(f"      - 'My computer is running slowly, what should I do?'")
        print(f"      - 'What is your warranty policy?'")
        print(f"      - 'How do I troubleshoot CPU overheating?'")
        
    except Exception as e:
        print(f"❌ Error creating documents: {e}")

if __name__ == "__main__":
    main()
