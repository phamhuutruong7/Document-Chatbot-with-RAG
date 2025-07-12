#!/usr/bin/env python3
"""
Create manufacturer-specific PC documentation for customer support.
Generates realistic manuals, troubleshooting guides, and product information.
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

def create_hp_pavilion_manual():
    """Create HP Pavilion desktop manual."""
    content = """HP PAVILION DESKTOP PC MANUAL
Model: HP Pavilion Desktop TP01-3000
===========================================

QUICK START GUIDE
-----------------
1. Connect power cable to back of PC
2. Connect monitor cable (HDMI/DisplayPort)
3. Connect keyboard and mouse (USB)
4. Press power button (front panel)
5. Follow Windows 11 setup wizard

HARDWARE SPECIFICATIONS
----------------------
• Processor: AMD Ryzen 5 5600G (6-core, 3.9GHz)
• Memory: 8GB DDR4-3200 (expandable to 32GB)
• Storage: 256GB PCIe NVMe SSD
• Graphics: AMD Radeon RX 6400 (4GB GDDR6)
• USB Ports: 6x USB-A 3.0, 2x USB-C
• Audio: Realtek ALC3601 codec
• Network: Realtek RTL8111 Ethernet + Wi-Fi 6

SETUP INSTRUCTIONS
-----------------
Initial Setup:
1. Remove all protective materials and cable ties
2. Position PC on stable, ventilated surface
3. Connect external devices before first power-on
4. Ensure all connections are secure

Display Connection:
• Primary: HDMI 2.1 port (graphics card)
• Secondary: DisplayPort 1.4 (graphics card)
• Integrated: HDMI 1.4 (motherboard)

Network Setup:
• Ethernet: Auto-detected, no drivers needed
• Wi-Fi: Settings > Network > Wi-Fi > Add network
• Bluetooth: Settings > Devices > Add Bluetooth device

COMMON ISSUES & SOLUTIONS
------------------------
PC Won't Start:
• Check power cable connection
• Verify power strip/outlet is working
• Hold power button 10 seconds, try again
• Check RAM seating (remove/reinstall)

No Display:
• Verify monitor cable connected to graphics card
• Try different video cable (HDMI/DisplayPort)
• Reseat graphics card if problem persists
• Test with different monitor/TV

Slow Performance:
• Check available storage (need 15% free)
• Run Windows Update for latest drivers
• Restart PC weekly to clear memory
• Check for malware with Windows Defender

Wi-Fi Issues:
• Restart router and PC
• Forget and reconnect to network
• Update Wi-Fi drivers via Device Manager
• Move closer to router or use ethernet

MAINTENANCE
-----------
Weekly:
• Restart PC to clear memory
• Run Windows Update
• Empty Recycle Bin

Monthly:
• Clean air vents with compressed air
• Check for Windows security updates
• Update graphics drivers

Quarterly:
• Full system backup
• Check cable connections
• Clean inside case (if comfortable)

WARRANTY & SUPPORT
------------------
• 1-year limited hardware warranty
• 90-day technical support included
• Extended warranty available
• Contact: hp.com/support or 1-800-HP-INVENT

TECHNICAL SUPPORT
----------------
Before calling support, please have:
• Model number: HP Pavilion TP01-3000
• Serial number (back of PC)
• Description of problem
• Error messages (if any)
• Recent changes to system

For fastest service:
• Try basic troubleshooting first
• Update all drivers
• Run Windows built-in diagnostics
• Document when problem started

© 2024 HP Inc. All rights reserved.
"""
    return content

def create_lenovo_thinkpad_manual():
    """Create Lenovo ThinkPad laptop manual."""
    content = """LENOVO THINKPAD E15 GEN 4 MANUAL
Model: ThinkPad E15 Gen 4 (21E6)
=====================================

QUICK START GUIDE
-----------------
1. Connect AC adapter to laptop
2. Press power button (top-right corner)
3. Open lid to wake from sleep
4. Follow Windows 11 setup wizard
5. Create user account and password

HARDWARE OVERVIEW
-----------------
• Processor: Intel Core i5-1235U (10-core, up to 4.4GHz)
• Memory: 16GB DDR4-3200 (soldered, not upgradeable)
• Storage: 512GB PCIe Gen4 NVMe SSD
• Display: 15.6" FHD (1920x1080) IPS, Anti-glare
• Graphics: Intel Iris Xe integrated
• Battery: 57Wh, up to 10 hours usage
• Weight: 3.9 lbs (1.77 kg)

PORT CONFIGURATION
-----------------
Left Side:
• 1x USB-C 3.2 Gen 1 (Power Delivery)
• 1x USB-A 3.2 Gen 1
• 1x HDMI 1.4b
• 1x 3.5mm headphone/microphone combo

Right Side:
• 1x USB-A 3.2 Gen 1
• 1x RJ45 Ethernet
• 1x MicroSD card reader
• 1x Security lock slot

FIRST TIME SETUP
----------------
Power On:
1. Connect 65W USB-C charger
2. Press power button (1 second)
3. Wait for Lenovo logo (30-60 seconds)
4. Follow Windows setup prompts

Network Configuration:
• Wi-Fi: Click network icon in taskbar
• Ethernet: Plug cable for automatic connection
• Bluetooth: Settings > Devices > Bluetooth

Display Settings:
• Resolution: Automatically set to 1920x1080
• Scaling: 125% (recommended for 15.6" screen)
• External monitor: HDMI or USB-C to DisplayPort

KEYBOARD SHORTCUTS
-----------------
Function Keys (Fn + F1-F12):
• Fn + F1: Mute/unmute audio
• Fn + F2: Lower volume
• Fn + F3: Raise volume
• Fn + F4: Mute microphone
• Fn + F5: Darken screen
• Fn + F6: Brighten screen
• Fn + F7: External display toggle
• Fn + F8: Airplane mode toggle
• Fn + F9: Settings app
• Fn + F10: Search
• Fn + F11: Open apps menu
• Fn + F12: Wi-Fi toggle

ThinkPad Shortcuts:
• Ctrl + Alt + Shift + R: Reboot
• Fn + Space: Zoom toggle
• Fn + 4: Sleep mode

BATTERY MANAGEMENT
-----------------
Charging:
• Use included 65W USB-C adapter
• Charge time: 0-80% in 1 hour
• Full charge: 1.5 hours
• Can use USB-C Power Delivery chargers (45W+)

Battery Life Optimization:
• Use balanced power mode for daily work
• Enable battery saver at 20%
• Adjust screen brightness (major power user)
• Close unused applications
• Disable background apps in Settings

TROUBLESHOOTING
--------------
Laptop Won't Start:
• Connect charger and wait 10 minutes
• Hold power button 15 seconds (hard reset)
• Remove battery (if removable), reconnect
• Contact support if still no power

Screen Issues:
• Adjust brightness (Fn + F5/F6)
• Update display drivers via Device Manager
• Connect external monitor to test graphics
• Reset display settings in Windows

Performance Issues:
• Check available storage (20GB+ recommended)
• Close browser tabs (memory usage)
• Restart weekly to clear memory leaks
• Check for Windows updates
• Run Disk Cleanup utility

Keyboard Problems:
• Check Fn lock status (Fn + Esc)
• Update keyboard drivers
• Test in safe mode
• Check for stuck keys or debris

MAINTENANCE
----------
Daily:
• Close laptop lid when not in use
• Use soft, dry cloth for screen cleaning
• Keep vents clear of dust/debris

Weekly:
• Restart to install updates
• Clean keyboard with compressed air
• Check battery level and charge as needed

Monthly:
• Update Lenovo Vantage software
• Run Windows security scan
• Check for BIOS updates
• Clean vents thoroughly

WARRANTY & SUPPORT
------------------
• 1-year limited warranty
• 24/7 technical support
• On-site service available
• Premium Care upgrades available
• Support: support.lenovo.com

CONTACT INFORMATION
------------------
Technical Support: 1-855-253-5696
Business Support: 1-866-426-0911
Parts & Accessories: lenovo.com/accessories
Online Support: support.lenovo.com/thinkpad

© 2024 Lenovo. All rights reserved.
"""
    return content

def create_dell_inspiron_guide():
    """Create Dell Inspiron all-in-one setup guide."""
    content = """DELL INSPIRON 24 5000 ALL-IN-ONE SETUP GUIDE
Model: Inspiron 5415 AIO (24-inch)
===============================================

UNBOXING & INITIAL SETUP
------------------------
Box Contents:
✓ Dell Inspiron 24 5000 All-in-One PC
✓ Wireless keyboard and mouse
✓ 90W AC adapter and power cord
✓ Quick Setup Guide
✓ Regulatory information

Setup Steps:
1. Remove PC from box carefully (support base)
2. Place on stable surface near power outlet
3. Connect power adapter to back of PC
4. Insert batteries in keyboard/mouse (AA included)
5. Press power button (bottom right of screen)

HARDWARE SPECIFICATIONS
----------------------
Display:
• 23.8" Full HD (1920 x 1080) Touch Screen
• IPS technology, wide viewing angles
• Edge-to-edge glass with anti-glare coating
• 10-point multi-touch support

Performance:
• AMD Ryzen 5 5500U processor (6-core, 2.1GHz)
• 8GB DDR4-3200 RAM (upgradeable to 32GB)
• 256GB PCIe NVMe SSD + 1TB HDD
• AMD Radeon graphics (integrated)

Connectivity:
• Wi-Fi 6 (802.11ax) + Bluetooth 5.1
• 2x USB 3.2 Gen 1 Type-A ports
• 1x USB 3.2 Gen 1 Type-C port
• 1x HDMI 1.4 output
• 1x RJ45 Ethernet port
• 1x 3.5mm headphone/microphone combo
• SD card reader (side access)

FIRST BOOT CONFIGURATION
------------------------
Power On Process:
1. Press power button (bottom-right bezel)
2. Dell logo appears (30-45 seconds)
3. Windows 11 Welcome screen
4. Follow on-screen setup wizard

Windows 11 Setup:
• Select region and language
• Connect to Wi-Fi network
• Sign in with Microsoft account (recommended)
• Set up PIN for quick sign-in
• Configure privacy settings
• Install initial Windows updates

Wireless Peripherals:
• Keyboard/mouse auto-pair on first boot
• If not working: press Connect button (bottom)
• Low battery: replace AA batteries
• Range: up to 30 feet from PC

DISPLAY CONFIGURATION
--------------------
Touch Screen Calibration:
1. Settings > System > Display
2. Click "Advanced display settings"
3. Select "Display adapter properties"
4. Click "Calibrate" tab
5. Follow calibration wizard

External Monitor Setup:
• Connect via HDMI port (back panel)
• Windows + P to select display mode:
  - PC screen only
  - Duplicate (mirror)
  - Extend (dual monitor)
  - Second screen only

Resolution Settings:
• Native: 1920 x 1080 (recommended)
• Scaling: 100% (default for 24" screen)
• Refresh rate: 60Hz (standard)

PERFORMANCE OPTIMIZATION
-----------------------
Storage Management:
• SSD (C:): Windows and programs (256GB)
• HDD (D:): Documents, media files (1TB)
• Move large files to D: drive for best performance
• Keep 20% free space on C: drive

Memory & Performance:
• 8GB RAM sufficient for basic tasks
• Upgrade to 16GB for heavy multitasking
• RAM slots: 1 occupied, 1 available
• Maximum supported: 32GB (2x16GB)

Startup Optimization:
• Disable unnecessary startup programs
• Task Manager > Startup tab
• Disable programs you don't need immediately
• Keep antivirus and system tools enabled

NETWORKING SETUP
---------------
Wi-Fi Configuration:
1. Click Wi-Fi icon in system tray
2. Select your network from list
3. Enter password when prompted
4. Check "Connect automatically"
5. Test connection with web browser

Ethernet Connection:
• Plug cable into RJ45 port (back)
• Windows automatically detects connection
• Ethernet takes priority over Wi-Fi
• Faster speeds for streaming/downloads

Bluetooth Devices:
1. Settings > Devices > Bluetooth
2. Click "Add Bluetooth or other device"
3. Select device type (mouse, headphones, etc.)
4. Follow pairing instructions
5. Device appears in connected list

COMMON ISSUES & SOLUTIONS
-------------------------
Touch Screen Not Responding:
• Clean screen with microfiber cloth
• Restart PC to reset touch drivers
• Check Windows Update for driver updates
• Calibrate touch screen in display settings

Poor Wi-Fi Performance:
• Move closer to router (within 30 feet)
• Restart router and PC
• Update Wi-Fi drivers in Device Manager
• Check for interference (microwaves, phones)
• Use 5GHz band if available

Slow Performance:
• Check available storage on C: drive
• Close unused browser tabs
• Restart PC to clear memory
• Run Disk Cleanup utility
• Check for malware with Windows Defender

Keyboard/Mouse Issues:
• Replace batteries (low battery indicator)
• Re-pair devices using Connect button
• Check for obstructions between device and PC
• Update drivers via Windows Update

MAINTENANCE & CARE
-----------------
Screen Cleaning:
• Use microfiber cloth, slightly damp
• Clean in circular motions, no pressure
• Avoid harsh chemicals or abrasives
• Turn off PC before cleaning

Ventilation:
• Keep rear vents clear (6 inches minimum)
• Use compressed air monthly on vents
• Don't block side ventilation slots
• Ensure ambient temperature under 80°F

Software Updates:
• Enable automatic Windows updates
• Update Dell applications monthly
• Check for BIOS updates quarterly
• Keep antivirus definitions current

WARRANTY & SUPPORT
------------------
Standard Warranty:
• 1 year limited hardware warranty
• 1 year technical support
• Mail-in service for repairs
• Advanced exchange available

Support Options:
• Dell SupportAssist (pre-installed)
• Online chat: dell.com/support
• Phone: 1-800-WWW-DELL (1-800-999-3355)
• Email support available
• Video tutorials: dell.com/learn

Extended Support:
• Premium Support Plus available
• ProSupport for business users
• Accidental damage protection
• On-site service options

SPECIFICATIONS SUMMARY
---------------------
Model: Dell Inspiron 24 5000 (5415)
Processor: AMD Ryzen 5 5500U
RAM: 8GB DDR4 (expandable)
Storage: 256GB SSD + 1TB HDD
Display: 23.8" FHD Touch
Operating System: Windows 11 Home
Warranty: 1 year limited

© 2024 Dell Inc. All rights reserved.
"""
    return content

def create_asus_rog_gaming_guide():
    """Create ASUS ROG gaming PC guide."""
    content = """ASUS ROG STRIX GT15 GAMING DESKTOP GUIDE
Model: G15CF-DB766 ROG Strix GT15
=====================================

GAMING SETUP QUICKSTART
-----------------------
Unboxing Priority:
1. Remove PC from packaging (keep upright)
2. Remove all protective foam/plastic
3. Connect power cable (750W PSU)
4. Connect gaming monitor (DisplayPort recommended)
5. Connect gaming peripherals (USB)
6. First boot and driver installation

Essential First Steps:
• Download ROG Armoury Crate software
• Install latest NVIDIA GeForce drivers
• Configure gaming monitor settings
• Set up RGB lighting preferences
• Create system restore point

HIGH-PERFORMANCE SPECIFICATIONS
------------------------------
Processing Power:
• Intel Core i7-12700F (12-core, up to 4.9GHz)
• 16GB DDR4-3200 RAM (2x8GB, 4 slots total)
• Supports up to 128GB memory

Graphics Performance:
• NVIDIA GeForce RTX 4060 Ti (16GB GDDR6)
• Ray tracing and DLSS 3.0 support
• 4K gaming capable at high settings
• VR ready (Oculus, Steam VR compatible)

Storage Configuration:
• 1TB PCIe Gen4 NVMe SSD (primary)
• 2TB HDD (7200 RPM, secondary storage)
• M.2 slots: 2 total (1 occupied)
• SATA ports: 4 available

Cooling System:
• ROG custom air cooling
• 3x case fans (intake/exhaust)
• CPU cooler: Tower-style with heatpipes
• GPU: Triple-fan custom cooling
• Thermal monitoring via Armoury Crate

GAMING OPTIMIZATION
------------------
Graphics Settings:
• NVIDIA Control Panel configuration
• Set performance mode for gaming
• Enable G-SYNC (compatible monitors)
• Configure per-game profiles
• Ray tracing settings per title

Memory & Performance:
• Enable XMP profile in BIOS (DDR4-3200)
• Set Windows to High Performance mode
• Disable unnecessary startup programs
• Configure virtual memory (pagefile)
• Regular driver updates critical

Storage Optimization:
• Install games on SSD for fast loading
• Move older games to HDD storage
• Keep 20% free space on system drive
• Enable Windows Storage Sense
• Regular disk cleanup and defrag

Network Gaming:
• Ethernet preferred over Wi-Fi
• Enable Windows Game Mode
• Configure router QoS for gaming
• Use DNS servers: 8.8.8.8, 1.1.1.1
• Monitor ping and latency

RGB LIGHTING CONTROL
--------------------
Armoury Crate Setup:
1. Download from ASUS website
2. Install and restart PC
3. Access Aura Sync for lighting
4. Sync with compatible peripherals
5. Create custom lighting profiles

Lighting Zones:
• Front panel ROG logo
• Internal case lighting
• Memory module RGB (if equipped)
• Graphics card RGB accents
• Motherboard RGB headers

Popular Effects:
• Static (solid color)
• Breathing (fade in/out)
• Rainbow (color cycle)
• Reactive (responds to system activity)
• Music mode (responds to audio)

GAME PERFORMANCE MONITORING
---------------------------
Built-in Tools:
• ROG GameVisual for display optimization
• PerformanceGuard for FPS monitoring
• CPU and GPU temperature monitoring
• Memory usage tracking
• Network performance stats

Third-Party Tools:
• MSI Afterburner (GPU monitoring)
• HWiNFO64 (detailed system info)
• Steam Overlay (FPS counter)
• Discord Overlay (voice while gaming)
• OBS (streaming/recording)

COOLING & THERMAL MANAGEMENT
---------------------------
Temperature Monitoring:
• CPU: Target under 80°C gaming
• GPU: Target under 83°C gaming
• System: Monitor via Armoury Crate
• Fan curves: Auto or custom settings
• Thermal throttling prevention

Maintenance Schedule:
• Monthly: Clean dust filters
• Quarterly: Internal dust removal
• Annually: Thermal paste replacement
• Check fan operation regularly
• Monitor temperatures during gaming

Airflow Optimization:
• Front: 2x intake fans (cool air in)
• Rear: 1x exhaust fan (hot air out)
• Keep case vents unobstructed
• Maintain positive air pressure
• Cable management for airflow

COMMON GAMING ISSUES
-------------------
Low Frame Rates:
• Update graphics drivers (NVIDIA GeForce)
• Lower game settings (shadows, effects)
• Close background applications
• Check thermal throttling
• Verify game installed on SSD

Game Crashes:
• Update game and launcher
• Verify game files integrity
• Check system temperature
• Update DirectX and Visual C++
• Disable overclocking temporarily

Online Gaming Lag:
• Use wired ethernet connection
• Close bandwidth-heavy applications
• Configure router QoS settings
• Check for Windows updates
• Test with different servers

Hardware Issues:
• Reseat RAM modules
• Check all cable connections
• Update BIOS firmware
• Test components individually
• Monitor system stability

OVERCLOCKING GUIDANCE
--------------------
Safe Overclocking:
• Use Armoury Crate auto-tuning
• Start with memory (XMP profiles)
• Monitor temperatures closely
• Test stability with stress tests
• Create restore points before changes

CPU Overclocking:
• Intel K-series processors only
• Gradual frequency increases
• Monitor voltage and temperature
• Stress test with Prime95
• 24-hour stability testing recommended

GPU Overclocking:
• Use MSI Afterburner or ASUS tools
• Increase power limit first
• Small memory clock increases
• Test with games or 3DMark
• Watch for artifacts or crashes

MAINTENANCE & UPDATES
--------------------
Weekly Tasks:
• Restart PC to clear memory
• Check for Windows updates
• Update game launchers
• Clear temporary files
• Monitor storage space

Monthly Tasks:
• Clean dust filters
• Update graphics drivers
• Check BIOS updates
• Run full antivirus scan
• Backup important game saves

Quarterly Tasks:
• Deep clean internal components
• Update all hardware drivers
• Check for firmware updates
• Performance benchmark testing
• Review and update software

TECHNICAL SUPPORT
-----------------
ASUS Support:
• Website: asus.com/support
• Phone: 1-812-282-2787
• Live chat available
• Email support
• Community forums

Warranty Coverage:
• 2-year global warranty
• Advanced replacement available
• International warranty valid
• Extended warranty options
• Gaming-specific support team

Before Contacting Support:
• Note exact error messages
• Document when issue started
• List recent hardware/software changes
• Have model/serial number ready
• Try basic troubleshooting steps

© 2024 ASUS. All rights reserved.
ROG logo is a trademark of ASUS.
"""
    return content

def main():
    """Create all manufacturer-specific documentation."""
    # Set up directories
    base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "documents")
    manuals_dir = os.path.join(base_dir, "pc-manuals")
    
    ensure_directory(manuals_dir)
    
    # Create manufacturer documents
    documents = [
        ("hp_pavilion_desktop_manual.txt", create_hp_pavilion_manual()),
        ("lenovo_thinkpad_e15_manual.txt", create_lenovo_thinkpad_manual()),
        ("dell_inspiron_aio_setup.txt", create_dell_inspiron_guide()),
        ("asus_rog_gaming_guide.txt", create_asus_rog_gaming_guide()),
    ]
    
    logger.info("🏭 Creating manufacturer-specific PC documentation...")
    
    for filename, content in documents:
        filepath = os.path.join(manuals_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        file_size = len(content.encode('utf-8'))
        logger.info(f"✅ Created {filename} ({file_size:,} bytes)")
    
    logger.info(f"🎉 Successfully created {len(documents)} manufacturer documents!")
    logger.info("📍 Documents saved to: data/documents/pc-manuals/")
    
    # Create summary
    total_size = sum(len(content.encode('utf-8')) for _, content in documents)
    print(f"\n📊 MANUFACTURER DOCUMENTATION SUMMARY")
    print(f"=" * 50)
    print(f"📁 Documents Created: {len(documents)}")
    print(f"💾 Total Size: {total_size:,} bytes ({total_size/1024:.1f} KB)")
    print(f"🏭 Manufacturers Covered: HP, Lenovo, Dell, ASUS")
    print(f"📱 Product Types: Desktop, Laptop, AIO, Gaming PC")
    
    print(f"\n🎯 COVERAGE AREAS:")
    print(f"   ✅ Hardware specifications")
    print(f"   ✅ Setup and configuration")
    print(f"   ✅ Troubleshooting guides")
    print(f"   ✅ Performance optimization")
    print(f"   ✅ Maintenance procedures")
    print(f"   ✅ Warranty information")
    
    print(f"\n🚀 NEXT STEPS:")
    print(f"   1. Run 'python scripts/check_status.py' to see updated stats")
    print(f"   2. Start your chatbot: 'streamlit run main.py'")
    print(f"   3. Test with manufacturer-specific questions")
    print(f"   4. Upload these documents via the web interface")

if __name__ == "__main__":
    main()
