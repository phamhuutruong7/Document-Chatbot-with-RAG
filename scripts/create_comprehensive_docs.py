"""
Enhanced PC Documentation Generator
Creates comprehensive technical documentation for PC customer support
"""

import os
from pathlib import Path
from datetime import datetime

def create_comprehensive_documentation():
    """Create extensive PC support documentation."""
    
    base_dir = Path("data/documents")
    
    # Comprehensive documentation structure
    documents = {
        
        # ============ DETAILED PC MANUALS ============
        
        "pc-manuals/dell/dell_inspiron_complete_guide.txt": """
Dell Inspiron Desktop Complete Setup and Troubleshooting Guide

TABLE OF CONTENTS:
1. Unboxing and Initial Setup
2. Hardware Overview
3. Software Installation
4. Performance Optimization
5. Troubleshooting Common Issues
6. Maintenance and Care
7. Upgrade Options
8. Technical Specifications

1. UNBOXING AND INITIAL SETUP

Package Contents Checklist:
□ Dell Inspiron Desktop Computer
□ Power Cable (6ft, 3-prong)
□ Keyboard (USB, Dell branded)
□ Mouse (USB optical, Dell branded)
□ Quick Setup Guide
□ Warranty and Service Tag information
□ Windows License Documentation
□ Driver and Utilities CD/USB (if included)

Step-by-Step Setup:
1. Choose proper location:
   - Flat, stable surface
   - Adequate ventilation (6+ inches clearance)
   - Away from heat sources
   - Near power outlet

2. Connect peripherals:
   - Monitor cable to rear VGA/HDMI/DisplayPort
   - Keyboard to rear USB port
   - Mouse to rear USB port
   - Ethernet cable (if using wired internet)

3. Power connection:
   - Connect power cable to computer
   - Plug into surge protector (recommended)
   - Press power button once

4. Initial Windows setup:
   - Follow Windows Setup Wizard
   - Create user account with strong password
   - Connect to Wi-Fi network
   - Accept license agreements
   - Set privacy preferences

2. HARDWARE OVERVIEW

Front Panel Features:
- Power button with LED indicator
- 2x USB 3.0 ports for quick access
- Headphone jack (3.5mm)
- Microphone jack (3.5mm)
- Optional: DVD/Blu-ray drive

Rear Panel Connections:
- Power connector
- 4x USB 2.0 ports
- 2x USB 3.0 ports
- Ethernet port (RJ45)
- Audio jacks (line in, line out, microphone)
- VGA port (analog video)
- HDMI port (digital video/audio)
- Optional: DisplayPort

Internal Components:
- Intel Core i3/i5/i7 processor
- 4GB-16GB DDR4 RAM
- 500GB-1TB SATA hard drive or SSD
- Integrated Intel HD Graphics
- 300W power supply
- Wi-Fi adapter (802.11ac)

3. SOFTWARE INSTALLATION

Pre-installed Software:
- Windows 10/11 Home Edition
- Microsoft Office Trial (30 days)
- Dell SupportAssist
- McAfee Antivirus (subscription required)
- Dell Update utility

Recommended Additional Software:
- Web browsers: Chrome, Firefox, Edge
- Media: VLC Media Player, iTunes
- Productivity: LibreOffice (free Office alternative)
- Security: Windows Defender (built-in)
- Utilities: 7-Zip, Adobe Reader

Driver Installation Priority:
1. Windows Updates (automatic)
2. Chipset drivers
3. Graphics drivers
4. Network adapter drivers
5. Audio drivers
6. USB drivers

4. PERFORMANCE OPTIMIZATION

Startup Optimization:
- Disable unnecessary startup programs
- Use Task Manager > Startup tab
- Keep only essential programs enabled
- Recommended: Windows Security, Audio drivers

Storage Management:
- Run Disk Cleanup monthly
- Delete temporary files and downloads
- Uninstall unused programs
- Keep 15% of disk space free for optimal performance

Memory Management:
- Monitor RAM usage in Task Manager
- Close unused applications
- Restart computer weekly
- Consider RAM upgrade if consistently above 80%

5. TROUBLESHOOTING COMMON ISSUES

Won't Turn On:
- Check power cable connections
- Verify power outlet works
- Try different power cable
- Check for LED lights on motherboard
- Contact support if no lights visible

No Display:
- Verify monitor is on and connected
- Check monitor cable connections
- Try different video port (HDMI vs VGA)
- Test with different monitor if available
- Reseat RAM if comfortable doing so

Slow Performance:
- Check available disk space (needs 15% free)
- Run antivirus scan
- Update Windows and drivers
- Check for overheating (clean vents)
- Consider SSD upgrade for significant improvement

Internet Issues:
- Check cable connections
- Restart router and modem
- Update network drivers
- Reset network settings in Windows
- Contact ISP if other devices also affected

6. MAINTENANCE AND CARE

Weekly Tasks:
- Restart computer to clear memory
- Empty recycle bin
- Check for Windows updates

Monthly Tasks:
- Run full antivirus scan
- Clean dust from vents using compressed air
- Check available disk space
- Review and uninstall unused programs

Quarterly Tasks:
- Back up important files
- Check all cable connections
- Update BIOS if needed (advanced users)
- Review startup programs

7. UPGRADE OPTIONS

RAM Upgrade:
- Maximum: 16GB (2x 8GB modules)
- Type: DDR4-2400 or DDR4-2666
- Installation: Insert into empty slots
- Cost: $50-100 for 8GB upgrade

Storage Upgrade:
- SSD replacement: Significant speed improvement
- External drive: Additional storage space
- Professional installation recommended
- Cost: $100-300 depending on capacity

8. TECHNICAL SPECIFICATIONS

Processor Options:
- Intel Core i3-10100 (4 cores, 3.6GHz)
- Intel Core i5-10400 (6 cores, 2.9GHz)
- Intel Core i7-10700 (8 cores, 2.9GHz)

Memory:
- Standard: 4GB DDR4-2666
- Expandable to: 16GB
- Slots: 2x DIMM slots

Storage:
- 500GB 7200 RPM SATA HDD
- 1TB 7200 RPM SATA HDD
- Optional: 256GB/512GB SSD

Graphics:
- Intel UHD Graphics 630
- Shared video memory
- Maximum resolution: 4K (3840x2160)

Connectivity:
- Wi-Fi 802.11ac
- Bluetooth 4.2
- Gigabit Ethernet
- 6x USB ports total

Power:
- 300W external power adapter
- Energy Star certified
- Sleep mode: <5W power consumption

Warranty Information:
- Standard: 1 year parts and labor
- Service Tag location: Side panel sticker
- Support: dell.com/support
- Phone: 1-800-DELL-HELP
""",

        "pc-manuals/hp/hp_envy_gaming_comprehensive.txt": """
HP ENVY Gaming Desktop - Complete User Manual

GAMING PERFORMANCE GUIDE

What Makes This a Gaming PC:
- Dedicated NVIDIA GeForce GTX/RTX graphics card
- High-speed DDR4 RAM (16GB standard)
- Fast SSD storage for quick game loading
- Advanced cooling system with multiple fans
- Gaming-optimized BIOS settings
- RGB lighting with customizable effects

INITIAL GAMING SETUP

1. Graphics Driver Installation:
   - Download GeForce Experience from nvidia.com
   - Install latest graphics drivers
   - Enable automatic driver updates
   - Register for GeForce Now cloud gaming

2. Game Performance Optimization:
   - Set Windows to Game Mode
   - Disable Windows updates during gaming
   - Close background applications
   - Set power plan to High Performance

3. Monitor Setup for Gaming:
   - Connect monitor to graphics card (NOT motherboard)
   - Use DisplayPort for best performance
   - Enable G-SYNC if monitor supports it
   - Set refresh rate to maximum (120Hz/144Hz)

GAMING SOFTWARE SETUP

Essential Gaming Software:
- Steam (game library and store)
- Epic Games Launcher (free games monthly)
- Discord (voice chat with friends)
- MSI Afterburner (GPU monitoring)
- NVIDIA GeForce Experience (driver updates)

Performance Monitoring:
- MSI Afterburner: GPU temperature and usage
- Task Manager: CPU and RAM usage
- Steam overlay: FPS counter
- Windows Game Bar: Built-in recording

GRAPHICS CARD OPTIMIZATION

Temperature Management:
- Normal gaming temps: 60-80°C
- Concerning temps: Above 85°C
- Use custom fan curves in MSI Afterburner
- Ensure case fans are working properly

Performance Tuning:
- Increase GPU power limit to maximum
- Gradual memory clock increases (+100MHz steps)
- Test stability with each change
- Monitor for artifacts or crashes

GAME-SPECIFIC SETTINGS

High-FPS Competitive Games (CS:GO, Valorant):
- Lower graphics settings for higher FPS
- Disable V-Sync for reduced input lag
- Use 144Hz+ monitor if available
- Prioritize frame rate over visual quality

AAA Single-Player Games (Cyberpunk, Witcher):
- Balance graphics quality and performance
- Enable DLSS for NVIDIA cards
- Use High settings as starting point
- Adjust based on target FPS (60/120/144)

VR Gaming Setup:
- Ensure minimum GTX 1060 or better
- Download SteamVR or Oculus software
- Clear 6x6 foot play area
- Update to latest graphics drivers

COOLING AND MAINTENANCE

Case Fan Configuration:
- Front fans: Intake (2x 120mm)
- Rear fan: Exhaust (1x 120mm)
- Top fans: Exhaust (optional)
- Positive air pressure preferred

Cleaning Schedule:
- Monthly: Blow out dust filters
- Quarterly: Full internal cleaning
- Annually: Thermal paste replacement (advanced)

Temperature Monitoring:
- CPU: Should stay under 80°C while gaming
- GPU: Should stay under 85°C while gaming
- Use HWMonitor or Core Temp software

NETWORK OPTIMIZATION FOR GAMING

Wired Connection Setup:
- Use Cat 6 Ethernet cable
- Connect directly to router/modem
- Disable Wi-Fi when using Ethernet
- Test speed with fast.com or speedtest.net

Router Settings:
- Enable Gaming Mode or QoS
- Set gaming PC as priority device
- Use 5GHz Wi-Fi band if wireless
- Consider gaming router for serious competitive play

Ping Optimization:
- Choose game servers closest to location
- Close bandwidth-heavy applications
- Use gaming VPN for server routing
- Contact ISP about gaming packages

RGB LIGHTING CUSTOMIZATION

HP Omen Gaming Hub:
- Download from Microsoft Store
- Control all RGB lighting effects
- Create custom color profiles
- Sync lighting with compatible peripherals

Lighting Effects:
- Static: Single color, always on
- Breathing: Slow fade in/out effect
- Color cycle: Smooth color transitions
- Game sync: React to in-game events

STORAGE OPTIMIZATION

SSD for Gaming:
- Install frequently played games on SSD
- Keep Windows and drivers on SSD
- Use HDD for large, rarely played games
- Enable Windows Storage Spaces if needed

Game Installation Tips:
- Install competitive games on fastest drive
- Monitor available space (keep 20% free)
- Use Steam's move installation feature
- Consider external SSD for additional games

UPGRADE PATHWAY

GPU Upgrade Priority:
- Most impactful gaming improvement
- Consider power supply requirements
- Verify physical clearance in case
- Factor in CPU bottlenecking

RAM Upgrade:
- 16GB minimum for modern gaming
- 32GB for streaming/content creation
- Match existing RAM speed and brand
- Install in pairs for dual-channel

CPU Upgrade Considerations:
- Check motherboard compatibility
- Usually not needed for 3-5 years
- More important for streaming/productivity
- Consider platform upgrade instead

TROUBLESHOOTING GAMING ISSUES

Low FPS Solutions:
1. Update graphics drivers
2. Lower in-game settings
3. Close background applications
4. Check for overheating
5. Verify power plan is set to High Performance

Game Crashes:
1. Verify game files in Steam/launcher
2. Update Windows and drivers
3. Check RAM with MemTest86
4. Monitor temperatures during gaming
5. Disable overclocks temporarily

Audio Issues:
1. Set correct default audio device
2. Update audio drivers
3. Check game audio settings
4. Test with different headphones/speakers
5. Disable audio enhancements

COMPETITIVE GAMING SETUP

Input Lag Reduction:
- Use wired gaming mouse and keyboard
- Disable mouse acceleration
- Set polling rate to 1000Hz
- Use gaming monitor with low input lag

Display Settings:
- Disable Windows full-screen optimizations
- Use exclusive full-screen mode in games
- Disable Windows Game Bar if not needed
- Set monitor to native resolution

Network Settings:
- Use wired connection
- Enable gaming mode on router
- Disable background downloads
- Consider gaming VPN for consistency

CONTENT CREATION FEATURES

Game Recording:
- Windows Game Bar (Win + G)
- NVIDIA ShadowPlay (GeForce Experience)
- OBS Studio for advanced features
- AMD ReLive for AMD graphics cards

Streaming Setup:
- OBS Studio or Streamlabs OBS
- Dedicated microphone recommended
- Good lighting for webcam
- Dual monitor setup helpful

Video Editing:
- DaVinci Resolve (free)
- Adobe Premiere Pro (subscription)
- Utilize GPU acceleration
- Plenty of storage space needed

WARRANTY AND SUPPORT

Gaming-Specific Coverage:
- Graphics card: Manufacturer warranty
- System warranty: 1 year parts/labor
- Gaming peripherals: Separate warranties
- Overclocking: May void certain warranties

Support Resources:
- HP Gaming Hub software
- NVIDIA GeForce forums
- Steam community forums
- Reddit gaming communities

Performance Baseline:
Document your system's performance in key games for future troubleshooting reference.
""",

        # ============ ADVANCED TROUBLESHOOTING ============
        
        "troubleshooting/hardware/advanced_diagnostics.txt": """
Advanced PC Hardware Diagnostics and Repair Guide

COMPREHENSIVE DIAGNOSTIC PROCEDURES

STEP 1: VISUAL INSPECTION CHECKLIST

External Inspection:
□ Check all cable connections (power, data, peripheral)
□ Inspect for physical damage, cracks, or burn marks
□ Verify fans are spinning freely
□ Look for loose components or screws
□ Check for dust buildup in vents
□ Examine power adapter/cable for damage

Internal Inspection (Power Off):
□ Remove side panel and ground yourself
□ Check for loose internal cables
□ Verify RAM modules are seated properly
□ Inspect expansion cards for proper seating
□ Look for blown capacitors (bulging/leaking)
□ Check for foreign objects or debris
□ Verify all power connectors are secure

STEP 2: POWER SYSTEM DIAGNOSTICS

Power Supply Testing:
1. Paperclip Test:
   - Unplug PSU from wall and components
   - Insert paperclip into 24-pin connector (Green to any Black)
   - Plug PSU back in and flip switch
   - Fan should spin = PSU has basic functionality

2. Voltage Testing (Multimeter Required):
   - +12V rail: Should read 11.4V - 12.6V
   - +5V rail: Should read 4.75V - 5.25V
   - +3.3V rail: Should read 3.14V - 3.47V
   - -12V rail: Should read -10.8V to -13.2V

3. Load Testing:
   - Use PSU tester or known good system
   - Check voltage stability under load
   - Monitor for voltage fluctuations

Power Issues Troubleshooting:
- No power: Check outlet, cable, PSU switch, motherboard power button
- Intermittent power: Loose connections, failing PSU, overheating
- Power but no boot: Motherboard, RAM, or CPU issues

STEP 3: MOTHERBOARD DIAGNOSTICS

POST (Power-On Self-Test) Codes:
- Listen for beep patterns during startup
- Count beeps and pauses carefully
- Refer to motherboard manual for code meanings
- No beeps may indicate speaker issue or critical failure

Common Beep Patterns:
- 1 beep: Normal boot
- 2 beeps: RAM error
- 3 beeps: RAM error
- 4 beeps: Timer failure
- 5 beeps: CPU failure
- 6 beeps: Keyboard controller error
- 7 beeps: Virtual mode exception error
- 8 beeps: Display memory error

LED Diagnostic Indicators:
- CPU LED: Processor not detected or failed
- DRAM LED: Memory not detected or failed
- VGA LED: Graphics card issue
- BOOT LED: Storage device not found

STEP 4: MEMORY (RAM) TESTING

Physical Testing:
1. Reseat all RAM modules
2. Test with one module at a time
3. Try modules in different slots
4. Clean contacts with isopropyl alcohol
5. Check for bent pins in memory slots

Software Testing:
1. Windows Memory Diagnostic:
   - Type "mdsched" in Start menu
   - Restart and test on next boot
   - Check results in Event Viewer

2. MemTest86:
   - Download from memtest86.com
   - Create bootable USB drive
   - Run for at least 4 complete passes
   - Any errors indicate faulty RAM

Memory Error Symptoms:
- Random blue screens or crashes
- Applications closing unexpectedly
- Corrupted files or data
- System freezes during operation
- Unusual error messages

STEP 5: STORAGE DIAGNOSTICS

Hard Drive Health Check:
1. Check SMART Data:
   - Use CrystalDiskInfo or HD Tune
   - Look for reallocated sectors
   - Check drive temperature
   - Monitor read error rate

2. Surface Scan:
   - Windows: chkdsk /r command
   - Third-party: HD Tune error scan
   - Look for bad sectors or read errors
   - Backup data if errors found

SSD Health Check:
- Monitor wear leveling count
- Check program/erase cycles
- Verify firmware is current
- Use manufacturer's diagnostic tools

Storage Connection Testing:
- Try different SATA cables
- Test on different SATA ports
- Check power connector seating
- Verify BIOS detects drive

STEP 6: GRAPHICS DIAGNOSTICS

Integrated Graphics Testing:
- Remove discrete graphics card
- Connect monitor to motherboard
- Test for display output
- Helps isolate GPU vs system issues

Discrete Graphics Testing:
1. Physical Inspection:
   - Check power connector seating
   - Verify card is fully seated in slot
   - Look for dust on heatsink/fans
   - Check for artifacts on screen

2. Driver Testing:
   - Boot in Safe Mode
   - Uninstall graphics drivers completely
   - Install latest drivers from manufacturer
   - Test for stability

3. Stress Testing:
   - Use FurMark or Unigine Heaven
   - Monitor temperatures during test
   - Look for artifacts or crashes
   - Check fan behavior under load

STEP 7: COOLING SYSTEM ANALYSIS

Temperature Monitoring:
- CPU: Idle <50°C, Load <80°C
- GPU: Idle <40°C, Load <85°C
- System: Case temperature <40°C
- Storage: HDDs <50°C, SSDs <70°C

Thermal Testing Procedure:
1. Monitor idle temperatures for 10 minutes
2. Run stress test (Prime95 + FurMark)
3. Monitor peak temperatures
4. Check for thermal throttling
5. Verify fan speed increases with temperature

Cooling Issues Diagnosis:
- Overheating: Clean heatsinks, replace thermal paste
- Loud fans: Bearing wear, dust buildup, high temperatures
- No fan operation: Check connections, replace fans
- Inconsistent cooling: Poor airflow, thermal paste issues

STEP 8: ADVANCED COMPONENT TESTING

CPU Testing:
1. Prime95 Stress Test:
   - Run Small FFTs test for 30 minutes
   - Monitor for errors or crashes
   - Check temperature stability
   - Verify clock speeds under load

2. CPU-Z Validation:
   - Check CPU identification
   - Verify clock speeds and voltages
   - Compare against manufacturer specs
   - Look for unusual readings

Motherboard Testing:
- Test all USB ports with devices
- Check all audio jacks
- Verify network connectivity
- Test expansion slots if available
- Check BIOS settings and stability

STEP 9: BIOS/UEFI DIAGNOSTICS

Accessing Diagnostics:
- Enter BIOS during startup (usually F2, F12, or Delete)
- Look for Hardware Monitor section
- Check System Information
- Review error logs if available

BIOS Issues:
- Won't enter BIOS: Keyboard issue, corrupted BIOS
- Settings don't save: Dead CMOS battery
- Boot loop: Incorrect settings, hardware failure
- Corrupted BIOS: May require professional repair

CMOS Reset Procedure:
1. Power off and unplug system
2. Remove CMOS battery for 5 minutes
3. Replace battery and power on
4. Reconfigure BIOS settings
5. Test system stability

STEP 10: DOCUMENTATION AND REPORTING

Testing Log Template:
- Date and time of testing
- Symptoms observed
- Tests performed and results
- Components tested and findings
- Actions taken and outcomes
- Remaining issues or concerns

Professional Referral Criteria:
- Multiple component failures
- Motherboard or CPU issues
- BIOS corruption requiring recovery
- Physical damage beyond cleaning
- Warranty considerations
- Customer comfort level with repairs

SAFETY REMINDERS:
- Always disconnect power before internal work
- Use anti-static wrist strap when handling components
- Never force components into place
- Keep workspace clean and organized
- Have adequate lighting for detailed work
- Take photos before disconnecting cables
""",

        # ============ NETWORKING GUIDES ============
        
        "troubleshooting/networking/complete_network_guide.txt": """
Complete PC Networking Troubleshooting Guide

NETWORK CONNECTIVITY FUNDAMENTALS

Understanding Network Types:
1. Ethernet (Wired):
   - Most reliable connection type
   - Speeds: 100 Mbps, 1 Gbps, 10 Gbps
   - Uses RJ45 connectors and Cat5e/Cat6 cables
   - Not affected by interference

2. Wi-Fi (Wireless):
   - Convenient but can be unstable
   - Standards: 802.11n (up to 150 Mbps), 802.11ac (up to 1.3 Gbps), 802.11ax (Wi-Fi 6)
   - Affected by distance, walls, and interference
   - Security protocols: WPA2, WPA3

BASIC NETWORK TROUBLESHOOTING STEPS

Step 1: Check Physical Connections
- Verify Ethernet cable is fully inserted
- Check for cable damage (kinks, cuts, bent connectors)
- Try a different Ethernet cable
- Test different ports on router/switch
- Ensure router/modem has power and is functioning

Step 2: Check Network Adapter Status
1. Open Device Manager (devmgmt.msc)
2. Expand "Network adapters"
3. Look for:
   - Yellow warning triangles (driver issues)
   - Red X marks (disabled devices)
   - Missing network adapters

4. Right-click adapter and select:
   - "Enable device" if disabled
   - "Update driver" if issues present
   - "Uninstall device" then restart (Windows will reinstall)

Step 3: Network Configuration Check
1. Open Command Prompt as Administrator
2. Run these commands in order:
   - ipconfig /all (view current configuration)
   - ping 127.0.0.1 (test network stack)
   - ping [gateway IP] (test local network)
   - ping 8.8.8.8 (test internet connectivity)
   - nslookup google.com (test DNS resolution)

ETHERNET CONNECTION TROUBLESHOOTING

Common Ethernet Issues:

1. No Link/Cable Unplugged:
   - Check cable connections at both ends
   - Test with known good cable
   - Try different port on router/switch
   - Check for damaged cable (visual inspection)
   - Verify network adapter is enabled

2. Limited or No Connectivity:
   - Usually an IP address assignment issue
   - Try ipconfig /release then ipconfig /renew
   - Check DHCP settings on router
   - Manually assign IP if DHCP fails
   - Restart router/modem

3. Slow Ethernet Speeds:
   - Check for cable category (Cat5e minimum for Gigabit)
   - Test with speed test (fast.com, speedtest.net)
   - Check for background downloads
   - Verify full-duplex operation
   - Update network adapter drivers

Ethernet Cable Testing:
- Use cable tester if available
- Check for bent pins in connectors
- Ensure proper crimping on custom cables
- Maximum cable length: 100 meters (328 feet)
- Avoid running near power lines or fluorescent lights

WI-FI CONNECTION TROUBLESHOOTING

Wi-Fi Connection Process:
1. Scan for available networks
2. Select correct network (SSID)
3. Enter password (case-sensitive)
4. Authenticate with router
5. Receive IP address via DHCP
6. Establish internet connection

Common Wi-Fi Issues:

1. Can't See Network:
   - Network may be hidden (broadcast disabled)
   - Router may be too far away
   - Wi-Fi adapter may be disabled
   - Check 2.4GHz vs 5GHz bands
   - Restart router and computer

2. Wrong Password Error:
   - Verify password case-sensitivity
   - Check for special characters
   - Confirm network security type (WPA2/WPA3)
   - Try forgetting and reconnecting
   - Reset router to factory defaults if needed

3. Connected but No Internet:
   - Check router internet connection
   - Try different DNS servers (8.8.8.8, 1.1.1.1)
   - Restart router and modem
   - Check for MAC address filtering
   - Contact ISP for service issues

Wi-Fi Signal Optimization:
- Move closer to router for testing
- Remove obstacles between devices
- Change Wi-Fi channel (1, 6, or 11 for 2.4GHz)
- Update router firmware
- Consider Wi-Fi extender or mesh system

ADVANCED NETWORK DIAGNOSTICS

Network Command Line Tools:

1. ipconfig Commands:
   - ipconfig /all: Show detailed network configuration
   - ipconfig /release: Release current IP address
   - ipconfig /renew: Request new IP from DHCP
   - ipconfig /flushdns: Clear DNS cache
   - ipconfig /registerdns: Re-register DNS entries

2. ping Command:
   - ping [IP/hostname]: Test connectivity
   - ping -t [address]: Continuous ping
   - ping -n [count] [address]: Specific number of pings
   - ping -l [size] [address]: Test with larger packets

3. tracert Command:
   - tracert [destination]: Show path to destination
   - Identifies where connection failures occur
   - Shows latency at each hop
   - Useful for ISP-related issues

4. netstat Command:
   - netstat -an: Show all connections and listening ports
   - netstat -b: Show executable associated with each connection
   - netstat -r: Display routing table

DNS TROUBLESHOOTING

DNS (Domain Name System) Issues:
- Websites load slowly or not at all
- Can access sites by IP address but not domain names
- Some sites work while others don't
- Browser shows "DNS server not responding"

DNS Troubleshooting Steps:
1. Flush DNS cache: ipconfig /flushdns
2. Try different DNS servers:
   - Google DNS: 8.8.8.8, 8.8.4.4
   - Cloudflare DNS: 1.1.1.1, 1.0.0.1
   - OpenDNS: 208.67.222.222, 208.67.220.220

3. Test DNS resolution: nslookup google.com
4. Check router DNS settings
5. Restart router and modem
6. Contact ISP if issues persist

FIREWALL AND SECURITY ISSUES

Windows Firewall Troubleshooting:
1. Check if Windows Firewall is blocking connections
2. Temporarily disable firewall for testing
3. Add exceptions for specific programs
4. Check third-party firewall software
5. Review antivirus network protection settings

Common Security-Related Network Issues:
- VPN software interfering with connections
- Antivirus blocking network access
- Proxy settings causing connection problems
- Parental controls blocking websites
- Corporate network restrictions

ROUTER AND MODEM TROUBLESHOOTING

Router Issues:
- Overheating (feel for excessive heat)
- Firmware bugs (check for updates)
- Configuration problems (reset to defaults)
- Hardware failure (replace if old)
- Power supply issues (check adapter voltage)

Modem Issues:
- Signal problems from ISP
- Coaxial/phone line connection issues
- Overheating or age-related failure
- Configuration problems
- Service outages in area

Power Cycle Procedure:
1. Unplug modem and router power
2. Wait 30 seconds
3. Plug in modem first, wait for full boot (2-3 minutes)
4. Plug in router, wait for full boot (2-3 minutes)
5. Test connection on computers/devices

NETWORK PERFORMANCE OPTIMIZATION

Speed Test Procedures:
1. Use wired connection for accurate results
2. Close all other applications and devices
3. Test at different times of day
4. Use multiple speed test sites
5. Compare results to ISP promised speeds

Improving Network Performance:
- Use wired connections for stationary devices
- Update network adapter drivers
- Optimize router placement
- Upgrade to newer Wi-Fi standards
- Consider mesh networking for large homes
- Upgrade internet plan if consistently slow

Quality of Service (QoS) Configuration:
- Prioritize important traffic (video calls, gaming)
- Limit bandwidth for certain devices/applications
- Configure in router settings
- Use gaming mode if available
- Monitor bandwidth usage by device

NETWORK SECURITY BEST PRACTICES

Securing Your Network:
1. Change default router passwords
2. Use WPA3 or WPA2 security
3. Disable WPS (Wi-Fi Protected Setup)
4. Hide network name (SSID) if desired
5. Enable MAC address filtering for sensitive networks
6. Regularly update router firmware
7. Use guest network for visitors
8. Monitor connected devices regularly

Detecting Network Intrusions:
- Unknown devices in connected device list
- Slower than normal internet speeds
- High data usage without explanation
- Strange network activity in router logs
- Unexpected pop-ups or redirects

MOBILE DEVICE CONNECTIVITY

Smartphone/Tablet Issues:
- Forget and reconnect to Wi-Fi network
- Reset network settings (will remove all saved networks)
- Check for iOS/Android updates
- Try different frequency bands (2.4GHz vs 5GHz)
- Restart device and router

Common Mobile-Specific Problems:
- Wi-Fi sleep settings causing disconnections
- Data saver modes limiting connectivity
- VPN apps interfering with connections
- Outdated network settings
- Interference from phone cases or accessories

NETWORK DOCUMENTATION

Creating Network Maps:
- Document all connected devices
- Note IP addresses and MAC addresses
- Record router configuration settings
- Keep list of network passwords
- Document any port forwarding rules
- Track device locations and purposes

Troubleshooting Documentation:
- Keep log of network issues and solutions
- Note any recurring problems
- Document what works for your specific setup
- Record ISP contact information and account details
- Keep receipt/warranty info for network equipment

When to Call Professional Help:
- ISP-side connectivity issues
- Physical cable installation needs
- Business network setup requirements
- Persistent issues after trying all troubleshooting steps
- Hardware replacement beyond comfort level
""",

        # ============ SOFTWARE GUIDES ============
        
        "troubleshooting/software/complete_windows_guide.txt": """
Complete Windows Operating System Troubleshooting Guide

WINDOWS STARTUP ISSUES

Boot Process Understanding:
1. Power-On Self Test (POST)
2. BIOS/UEFI initialization
3. Boot loader activation
4. Windows kernel loading
5. Service and driver initialization
6. User login process

Common Startup Problems:

1. Computer Won't Start:
   - No display, no Windows logo
   - Hardware issue (see hardware troubleshooting guide)
   - Check power connections and basic hardware

2. Blue Screen on Startup:
   - BSOD (Blue Screen of Death) appears during boot
   - Note error code (e.g., INACCESSIBLE_BOOT_DEVICE)
   - Often indicates driver or hardware issues
   - Try Safe Mode boot

3. Endless Boot Loop:
   - Windows starts loading but restarts repeatedly
   - Can be caused by corrupted system files
   - Hardware instability
   - Recent driver installations

4. Black Screen with Cursor:
   - Windows loads but desktop doesn't appear
   - Explorer.exe process may have failed
   - Graphics driver issues
   - Malware interference

Safe Mode Access Methods:
- Hold Shift while clicking Restart in Windows
- Interrupt boot process 3 times to trigger recovery
- Use Windows installation media
- F8 key during startup (older systems)

WINDOWS STARTUP REPAIR

Automatic Startup Repair:
1. Boot from Windows installation media
2. Select "Repair your computer"
3. Choose "Troubleshoot" > "Startup Repair"
4. Follow on-screen instructions
5. Restart and test normal boot

Manual Boot Repair:
1. Boot from Windows installation media
2. Open Command Prompt from repair options
3. Run these commands:
   - bootrec /fixmbr
   - bootrec /fixboot
   - bootrec /scanos
   - bootrec /rebuildbcd
4. Restart system

System File Checker (SFC):
1. Boot to Command Prompt (recovery or Safe Mode)
2. Run: sfc /scannow
3. Wait for scan completion (can take 30+ minutes)
4. If issues found, run: DISM /online /cleanup-image /restorehealth
5. Run sfc /scannow again
6. Restart system

PERFORMANCE TROUBLESHOOTING

Identifying Performance Issues:
- Slow startup/shutdown times
- Applications taking long to load
- System freezing or becoming unresponsive
- High CPU, memory, or disk usage
- Excessive fan noise

Task Manager Analysis:
1. Press Ctrl+Shift+Esc to open Task Manager
2. Click "More details" if needed
3. Analyze each tab:
   - Processes: Sort by CPU, Memory, Disk usage
   - Performance: Check overall system health
   - Startup: Identify slow-starting programs
   - Users: Check for multiple active sessions

CPU Usage Troubleshooting:
High CPU usage causes:
- Malware or viruses
- Background Windows updates
- Indexing services
- Antivirus scanning
- Runaway processes

Solutions:
- Identify high-usage processes in Task Manager
- End unnecessary processes (research first)
- Update drivers and Windows
- Run malware scans
- Disable Windows Search if needed

Memory (RAM) Issues:
High memory usage symptoms:
- System slowdown with multiple applications
- Out of memory errors
- Applications closing unexpectedly
- Virtual memory warnings

Solutions:
- Close unnecessary applications
- Check for memory leaks in specific programs
- Increase virtual memory (page file)
- Add more physical RAM
- Run memory diagnostic tools

Disk Usage Problems:
100% disk usage causes:
- Windows Update downloading/installing
- Antivirus scanning
- Disk fragmentation
- Failing hard drive
- Insufficient free space

Solutions:
- Check available disk space (needs 15% free)
- Run Disk Cleanup utility
- Defragment hard drives (not SSDs)
- Check for disk errors: chkdsk /f
- Consider SSD upgrade

WINDOWS UPDATE ISSUES

Update Problems:
- Updates fail to download
- Installation errors
- System becomes unstable after updates
- Updates take extremely long time
- Automatic updates disabled

Windows Update Troubleshooter:
1. Settings > Update & Security > Troubleshoot
2. Run "Windows Update" troubleshooter
3. Follow recommendations
4. Restart and try updates again

Manual Update Reset:
1. Stop Windows Update service:
   - Open Services (services.msc)
   - Find "Windows Update" service
   - Right-click and stop

2. Clear update cache:
   - Navigate to C:\Windows\SoftwareDistribution
   - Delete all contents (requires admin rights)

3. Restart Windows Update service
4. Check for updates again

DRIVER ISSUES

Driver Problem Symptoms:
- Device not working or recognized
- Yellow warning triangles in Device Manager
- Blue screens with driver-related error codes
- Performance issues with specific hardware
- Audio, video, or network connectivity problems

Driver Troubleshooting:
1. Open Device Manager (devmgmt.msc)
2. Look for devices with warning symbols
3. Right-click problematic device
4. Try these options in order:
   - Update driver (search automatically)
   - Uninstall device (restart to reinstall)
   - Roll back driver (if recently updated)
   - Disable/enable device

Finding Correct Drivers:
1. Identify exact hardware model
2. Visit manufacturer's website
3. Download drivers for your specific Windows version
4. Avoid third-party driver update utilities
5. Create restore point before installing

Graphics Driver Issues:
- Display problems, artifacts, or crashes
- Gaming performance issues
- Multiple monitor problems
- Video playback issues

Solutions:
- Use Display Driver Uninstaller (DDU) in Safe Mode
- Download latest drivers from NVIDIA/AMD
- Install drivers and restart
- Check Windows Update for driver updates

BLUE SCREEN OF DEATH (BSOD)

Understanding BSOD:
- System crashes to prevent damage
- Displays error code and technical information
- Usually indicates hardware or driver issues
- Can be caused by overheating or power problems

Common BSOD Error Codes:
- SYSTEM_THREAD_EXCEPTION_NOT_HANDLED: Driver issue
- MEMORY_MANAGEMENT: RAM problem
- INACCESSIBLE_BOOT_DEVICE: Storage/driver issue
- KERNEL_SECURITY_CHECK_FAILURE: Security software conflict
- DPC_WATCHDOG_VIOLATION: Driver timing issue

BSOD Troubleshooting:
1. Note the exact error code
2. Check for overheating
3. Test RAM with MemTest86
4. Update all drivers
5. Check for Windows updates
6. Run system file checker
7. Check hard drive health

Analyzing Crash Dumps:
1. Enable crash dumps in System Properties
2. Use BlueScreenView or WinDbg to analyze
3. Look for recurring patterns
4. Identify problematic drivers or hardware
5. Focus fixes on identified components

REGISTRY ISSUES

Registry Problems:
- System settings reverting
- Applications not starting correctly
- Error messages about missing registry entries
- System instability after software installation/removal

Registry Backup:
1. Open Registry Editor (regedit)
2. Select Computer (top level)
3. File > Export
4. Save backup file with descriptive name
5. Store in safe location

Common Registry Fixes:
1. Run System File Checker first
2. Use Windows built-in registry repair tools
3. Restore from previous system restore point
4. Use registry cleaner cautiously (backup first)
5. Manual registry editing (advanced users only)

MALWARE AND SECURITY ISSUES

Malware Symptoms:
- Extremely slow performance
- Unexpected pop-ups and advertisements
- Browser redirects to unknown sites
- Mysterious network activity
- Unknown programs installed
- Antivirus disabled or not working

Malware Removal Process:
1. Boot from external antivirus rescue disk
2. Run full system scan in Safe Mode
3. Use multiple scanning tools:
   - Windows Defender full scan
   - Malwarebytes Anti-Malware
   - AdwCleaner for adware
   - RootkitRevealer for rootkits

4. Clear browser data and reset settings
5. Change all passwords after cleaning
6. Update all software and OS

Prevention Strategies:
- Keep Windows and software updated
- Use reputable antivirus with real-time protection
- Avoid suspicious downloads and email attachments
- Use standard user accounts for daily activities
- Regular system backups
- Enable Windows Defender or quality third-party AV

USER ACCOUNT ISSUES

Profile Problems:
- Can't log into user account
- Desktop and settings missing
- "User Profile Service failed logon" error
- Temporary profile created instead of normal profile

Profile Repair:
1. Create new administrator account
2. Copy data from old profile to new
3. Delete corrupted profile registry entries
4. Recreate user profile
5. Restore personal files and settings

Password Issues:
- Forgotten local account password
- Microsoft account sync problems
- Password complexity requirements
- Account lockout situations

Password Recovery:
1. Use password reset disk if created
2. Boot from Windows installation media
3. Replace sethc.exe with cmd.exe
4. Reset password using net user command
5. Restore original sethc.exe file

SYSTEM RESTORE AND RECOVERY

System Restore Points:
- Automatic creation before major changes
- Manual creation before risky operations
- Include system files, registry, and drivers
- Don't affect personal files

Using System Restore:
1. Control Panel > Recovery > Open System Restore
2. Choose restore point before problems started
3. Review affected programs
4. Confirm restoration
5. System will restart and restore

Creating Recovery Media:
1. Control Panel > Recovery > Create Recovery Drive
2. Include system files if space allows
3. Use 32GB+ USB drive
4. Test recovery media before needed
5. Update periodically

Reset vs. Refresh:
- Refresh: Keep personal files, remove programs
- Reset: Complete fresh installation
- Both require Windows installation or recovery media
- Backup important data first

PREVENTIVE MAINTENANCE

Weekly Tasks:
- Restart computer completely
- Run antivirus full scan
- Check available disk space
- Review running processes
- Empty recycle bin

Monthly Tasks:
- Install Windows updates
- Update drivers and software
- Run disk cleanup utility
- Check for malware
- Review startup programs

Quarterly Tasks:
- Create system backup
- Create new restore point
- Clean temporary files thoroughly
- Check hard drive health
- Review and organize files

Annual Tasks:
- Consider fresh Windows installation
- Evaluate hardware upgrade needs
- Review backup strategy
- Update recovery media
- Clean internal components

PROFESSIONAL HELP INDICATORS

When to Seek Help:
- Multiple hardware failures
- Repeated blue screens after troubleshooting
- Suspected malware that can't be removed
- Data recovery needs
- Network security breaches
- Time constraints for critical repairs
- Comfort level exceeded for repairs

Documentation for Technicians:
- List of symptoms and when they occur
- Recent changes or installations
- Error messages (screenshots helpful)
- Steps already attempted
- Backup status of important data
""",

        # ============ CUSTOMER SERVICE TRAINING ============
        
        "policies/training/customer_service_excellence.txt": """
PC Customer Service Excellence Training Manual

CUSTOMER SERVICE FUNDAMENTALS

Understanding Customer Needs:
1. Technical Skill Level Assessment:
   - Beginner: Basic computer operation
   - Intermediate: Comfortable with settings and software
   - Advanced: Understands hardware and troubleshooting
   - Professional: IT background or expert knowledge

2. Communication Style Adaptation:
   - Visual learners: Provide diagrams and screenshots
   - Auditory learners: Explain processes step-by-step
   - Kinesthetic learners: Guide through hands-on practice
   - Technical customers: Use precise technical language
   - Non-technical customers: Use simple, friendly explanations

CUSTOMER INTERACTION PROTOCOLS

Initial Contact Best Practices:
- Greet warmly and professionally
- Introduce yourself and your role
- Ask for customer's name and use it throughout interaction
- Listen actively to their concerns
- Confirm understanding before proceeding

Example Opening: "Good morning! This is Sarah from PC Support. I'm here to help you get your computer running perfectly. May I have your name and a brief description of what's happening with your system?"

Problem Assessment Framework:
1. Gather Information:
   - When did the problem start?
   - What were you doing when it occurred?
   - Is this the first time this has happened?
   - Have any recent changes been made?
   - What error messages are you seeing?

2. Understand Impact:
   - How is this affecting your work/daily use?
   - Is this urgent or can it wait?
   - Are you losing important data?
   - Do you have backup systems available?

3. Set Expectations:
   - Estimated time for diagnosis
   - Potential costs involved
   - Various solution options
   - Timeline for resolution

TECHNICAL COMMUNICATION SKILLS

Explaining Technical Concepts:
1. Use Analogies:
   - RAM is like your workspace - more RAM = bigger desk
   - CPU is like your brain - faster CPU = quicker thinking
   - Hard drive is like a filing cabinet - stores all your information
   - Internet connection is like a highway - more bandwidth = more lanes

2. Break Down Complex Processes:
   - Divide into simple, sequential steps
   - Check understanding after each major step
   - Use "first, then, next, finally" structure
   - Provide visual aids when possible

3. Avoid Technical Jargon:
   - Instead of "defragmentation" say "organizing files for better performance"
   - Instead of "driver update" say "updating software that helps parts communicate"
   - Instead of "BSOD" say "system crash screen"

PROBLEM-SOLVING METHODOLOGY

Systematic Troubleshooting Approach:
1. Listen and Document:
   - Record all symptoms reported
   - Note customer's words exactly
   - Ask clarifying questions
   - Confirm understanding

2. Start Simple:
   - Check obvious solutions first
   - Verify basics (power, connections)
   - Try quick fixes before complex ones
   - Rule out user error gently

3. Escalate Systematically:
   - Move from software to hardware
   - Test one variable at a time
   - Document what works and what doesn't
   - Keep customer informed of progress

4. Verify Solutions:
   - Test thoroughly before declaring fixed
   - Have customer confirm resolution
   - Explain what was wrong and why
   - Provide prevention tips

DIFFICULT SITUATION MANAGEMENT

Handling Frustrated Customers:
1. Acknowledge Feelings:
   "I understand how frustrating this must be for you."
   "I can hear that this is really impacting your work."
   "Let's work together to get this resolved quickly."

2. Take Ownership:
   "I'm going to personally make sure we fix this."
   "This is my priority right now."
   "I won't consider this closed until you're completely satisfied."

3. Provide Regular Updates:
   "I'm still working on this - here's what I've found so far..."
   "This is taking longer than expected, but I'm making progress..."
   "I have two more things to try, and then we'll explore other options."

Managing Unrealistic Expectations:
- Explain technical limitations clearly
- Offer alternative solutions
- Be honest about costs and timeframes
- Focus on what you CAN do
- Involve supervisor when necessary

De-escalation Techniques:
1. Lower Your Voice:
   - Speak slowly and calmly
   - Use a soothing tone
   - Don't match their energy level

2. Use Positive Language:
   - "Let's see what we can do" instead of "That's impossible"
   - "Here's what I recommend" instead of "You should have"
   - "We'll find a solution" instead of "This is a problem"

3. Focus on Solutions:
   - Move conversation toward resolution
   - Offer multiple options when possible
   - Emphasize customer control and choice

PRODUCT KNOWLEDGE REQUIREMENTS

Hardware Expertise:
- Basic computer components and functions
- Common failure modes and symptoms
- Upgrade options and compatibility
- Performance expectations for different systems
- Warranty coverage and limitations

Software Knowledge:
- Windows operating system basics
- Common application issues
- Driver installation and troubleshooting
- Security software and best practices
- Backup and recovery procedures

Current Technology Trends:
- Stay updated on new releases
- Understand generational improvements
- Know competitive products
- Recognize emerging technologies
- Anticipate future customer needs

SALES INTEGRATION

Identifying Upgrade Opportunities:
1. Performance Issues:
   - Slow boot times → SSD upgrade
   - Multitasking problems → RAM upgrade
   - Gaming performance → Graphics card
   - Storage space → Larger hard drive

2. Age-Related Problems:
   - Frequent crashes → System replacement
   - Compatibility issues → OS upgrade
   - Multiple component failures → New computer
   - Outdated features → Modern system

Consultative Selling Approach:
- Focus on customer needs, not product features
- Explain benefits in terms of their specific use case
- Provide options at different price points
- Be honest about whether upgrades make sense
- Consider total cost of ownership

Ethical Considerations:
- Never oversell unnecessary components
- Disclose all costs upfront
- Explain warranty implications
- Offer both repair and replacement options
- Respect customer budget constraints

FOLLOW-UP PROCEDURES

Immediate Follow-up (24-48 hours):
- Confirm solution is still working
- Check if any new issues have appeared
- Answer any additional questions
- Ensure customer satisfaction

Long-term Follow-up (2-4 weeks):
- Check system performance
- Remind about maintenance tasks
- Identify any emerging needs
- Build relationship for future business

Documentation Requirements:
- Complete work order with all details
- Note any ongoing concerns
- Record customer preferences and communication style
- Update customer history for future reference

PERFORMANCE METRICS

Customer Satisfaction Measures:
- First-call resolution rate
- Customer satisfaction scores
- Repeat customer rate
- Referral generation
- Complaint frequency

Technical Competency Indicators:
- Accuracy of initial diagnosis
- Efficiency of problem resolution
- Knowledge demonstration
- Continuous learning participation
- Certification maintenance

Communication Excellence Markers:
- Customer feedback on explanation clarity
- Ability to calm frustrated customers
- Success with non-technical customers
- Professional language use
- Active listening demonstration

CONTINUOUS IMPROVEMENT

Staying Current:
- Regularly review product manuals
- Participate in manufacturer training
- Follow technology news and trends
- Learn from experienced colleagues
- Practice with new technologies

Customer Feedback Integration:
- Review all customer comments
- Identify common complaint patterns
- Adjust procedures based on feedback
- Share improvements with team
- Track improvement effectiveness

Professional Development:
- Pursue relevant certifications
- Attend industry conferences
- Join professional organizations
- Read technical publications
- Network with industry professionals

EMERGENCY PROCEDURES

Data Loss Situations:
- Stop all system activity immediately
- Don't attempt repairs that could worsen damage
- Explain data recovery options and costs
- Set realistic expectations about recovery success
- Refer to data recovery specialists when appropriate

System Security Breaches:
- Isolate affected system from network
- Document all symptoms and recent activity
- Recommend immediate password changes
- Suggest professional security assessment
- Provide prevention education

Hardware Failures During Service:
- Stop work immediately
- Document exactly what occurred
- Inform customer and supervisor
- Take responsibility appropriately
- Focus on solution and next steps

Remember: Every customer interaction is an opportunity to build trust, demonstrate expertise, and create a positive experience that leads to loyalty and referrals.
"""
    }
    
    # Create all documents
    created_files = []
    
    for file_path, content in documents.items():
        full_path = base_dir / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        created_files.append(full_path)
        print(f"✅ Created: {file_path}")
    
    return created_files

if __name__ == "__main__":
    print("📚 Creating Comprehensive PC Documentation")
    print("=" * 60)
    
    try:
        created_files = create_comprehensive_documentation()
        
        print(f"\n✅ Successfully created {len(created_files)} comprehensive documents!")
        print(f"\n📊 Enhanced Documentation Coverage:")
        print(f"   🖥️  Detailed PC Manuals (Dell Inspiron, HP Gaming)")
        print(f"   🔧 Advanced Hardware Diagnostics")
        print(f"   🌐 Complete Network Troubleshooting")
        print(f"   💻 Comprehensive Windows Support")
        print(f"   👥 Customer Service Training")
        
        print(f"\n🎯 Your knowledge base now includes:")
        print(f"   • Step-by-step setup procedures")
        print(f"   • Advanced diagnostic techniques") 
        print(f"   • Professional troubleshooting methods")
        print(f"   • Customer service best practices")
        print(f"   • Gaming PC optimization")
        print(f"   • Network security procedures")
        
        print(f"\n🚀 Ready for professional-level PC support!")
        
    except Exception as e:
        print(f"❌ Error creating documents: {e}")
