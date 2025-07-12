"""
Download configurations for PC documentation
Contains URLs and settings for downloading manufacturer manuals, troubleshooting guides, etc.
"""

# PC Manufacturer Documentation URLs
DOWNLOAD_CONFIGS = [
    # ============ PC MANUALS ============
    
    # Dell PC Manuals
    {
        'category': 'pc-manuals',
        'manufacturer': 'dell',
        'description': 'Dell Desktop and Laptop Manuals',
        'direct_pdfs': [
            {
                'url': 'https://www.dell.com/support/manuals/en-us/optiplex-3080-desktop/optiplex-3080-setup-and-specifications/overview?guid=guid-92c3c0f8-5c5a-4f4e-9c9a-8e8e8e8e8e8e',
                'filename': 'dell_optiplex_3080_manual.pdf'
            },
            {
                'url': 'https://www.dell.com/support/manuals/en-us/inspiron-15-3511-laptop/inspiron-3511-setup-and-specifications/overview',
                'filename': 'dell_inspiron_15_3511_manual.pdf'
            },
            {
                'url': 'https://www.dell.com/support/manuals/en-us/xps-13-9310-laptop/xps-13-9310-setup-and-specifications/overview',
                'filename': 'dell_xps_13_9310_manual.pdf'
            }
        ],
        'search_urls': [
            {
                'url': 'https://www.dell.com/support/manuals/',
                'search_terms': ['manual', 'setup', 'guide', 'specifications']
            }
        ]
    },
    
    # HP PC Manuals
    {
        'category': 'pc-manuals',
        'manufacturer': 'hp',
        'description': 'HP Desktop and Laptop Manuals',
        'direct_pdfs': [
            {
                'url': 'https://support.hp.com/us-en/drivers/printers',
                'filename': 'hp_pavilion_desktop_manual.pdf'
            },
            {
                'url': 'https://support.hp.com/us-en/document/c06161099',
                'filename': 'hp_elitebook_850_manual.pdf'
            }
        ],
        'search_urls': [
            {
                'url': 'https://support.hp.com/us-en/drivers/manuals',
                'search_terms': ['user guide', 'manual', 'setup', 'maintenance']
            }
        ]
    },
    
    # Lenovo PC Manuals
    {
        'category': 'pc-manuals',
        'manufacturer': 'lenovo',
        'description': 'Lenovo ThinkPad and Desktop Manuals',
        'direct_pdfs': [
            {
                'url': 'https://download.lenovo.com/pccbbs/thinkcentre_pdf/thinkcentre_m720q_ug_en.pdf',
                'filename': 'lenovo_thinkcentre_m720q_manual.pdf'
            },
            {
                'url': 'https://download.lenovo.com/pccbbs/mobiles_pdf/t14_t14i_ug_en.pdf',
                'filename': 'lenovo_thinkpad_t14_manual.pdf'
            }
        ]
    },
    
    # ASUS PC Manuals
    {
        'category': 'pc-manuals',
        'manufacturer': 'asus',
        'description': 'ASUS Desktop and Laptop Manuals',
        'direct_pdfs': [
            {
                'url': 'https://www.asus.com/support/download-center/',
                'filename': 'asus_vivobook_15_manual.pdf'
            },
            {
                'url': 'https://www.asus.com/support/',
                'filename': 'asus_rog_desktop_manual.pdf'
            }
        ]
    },
    
    # ============ TROUBLESHOOTING GUIDES ============
    
    # Hardware Troubleshooting
    {
        'category': 'troubleshooting',
        'manufacturer': 'hardware',
        'description': 'General Hardware Troubleshooting Guides',
        'direct_pdfs': [
            {
                'url': 'https://docs.microsoft.com/en-us/troubleshoot/windows-client/performance/troubleshoot-high-cpu-usage-issue-in-windows',
                'filename': 'windows_cpu_troubleshooting.pdf'
            },
            {
                'url': 'https://support.microsoft.com/en-us/windows/fix-sound-problems-in-windows-10-73025246-b61c-40fb-671a-2fcb4a4c1e8e',
                'filename': 'windows_sound_troubleshooting.pdf'
            }
        ]
    },
    
    # Software Troubleshooting
    {
        'category': 'troubleshooting',
        'manufacturer': 'software',
        'description': 'Software and OS Troubleshooting Guides',
        'direct_pdfs': [
            {
                'url': 'https://support.microsoft.com/en-us/windows/windows-10-update-troubleshooter-19bc41ca-ad72-ae94-9660-f5db49d54a6b',
                'filename': 'windows_update_troubleshooting.pdf'
            },
            {
                'url': 'https://support.microsoft.com/en-us/windows/fix-problems-with-apps-from-microsoft-store-1e739174-b2e7-29bd-f6b0-b3dd2a5c5816',
                'filename': 'microsoft_store_troubleshooting.pdf'
            }
        ]
    },
    
    # Network Troubleshooting
    {
        'category': 'troubleshooting',
        'manufacturer': 'networking',
        'description': 'Network and Connectivity Troubleshooting',
        'direct_pdfs': [
            {
                'url': 'https://support.microsoft.com/en-us/windows/fix-wi-fi-connection-issues-in-windows-9424a1f7-6a3b-65a6-4d78-7f07eee84d2c',
                'filename': 'wifi_troubleshooting.pdf'
            },
            {
                'url': 'https://support.microsoft.com/en-us/windows/fix-ethernet-connection-issues-in-windows-10-843dcd3d-4b2d-4e2d-b2c7-5c9b9c9b9c9b',
                'filename': 'ethernet_troubleshooting.pdf'
            }
        ]
    },
    
    # ============ COMPONENT MANUALS ============
    
    # Graphics Cards
    {
        'category': 'pc-manuals',
        'manufacturer': 'graphics',
        'description': 'Graphics Card Installation and Troubleshooting',
        'direct_pdfs': [
            {
                'url': 'https://www.nvidia.com/content/dam/en-zz/Solutions/geforce/guides/nvidia-rtx-30-series-installation-guide.pdf',
                'filename': 'nvidia_rtx_30_series_installation.pdf'
            },
            {
                'url': 'https://www.amd.com/system/files/documents/radeon-rx-6000-series-installation-guide.pdf',
                'filename': 'amd_radeon_rx_6000_installation.pdf'
            }
        ]
    },
    
    # Motherboards
    {
        'category': 'pc-manuals',
        'manufacturer': 'motherboards',
        'description': 'Motherboard Installation and Setup Guides',
        'direct_pdfs': [
            {
                'url': 'https://www.asus.com/support/download-center/',
                'filename': 'asus_motherboard_z590_manual.pdf'
            },
            {
                'url': 'https://www.msi.com/support/',
                'filename': 'msi_b550_motherboard_manual.pdf'
            }
        ]
    },
    
    # ============ POLICIES AND FAQS ============
    
    # General PC Support FAQs
    {
        'category': 'faqs',
        'manufacturer': 'general',
        'description': 'General PC Support and Common Questions',
        'direct_pdfs': [
            {
                'url': 'https://support.microsoft.com/en-us/windows/windows-10-help',
                'filename': 'windows_10_help_guide.pdf'
            },
            {
                'url': 'https://docs.microsoft.com/en-us/windows/whats-new/',
                'filename': 'windows_new_features_guide.pdf'
            }
        ]
    },
    
    # Gaming PC FAQs
    {
        'category': 'faqs',
        'manufacturer': 'gaming',
        'description': 'Gaming PC Setup and Optimization',
        'direct_pdfs': [
            {
                'url': 'https://www.nvidia.com/en-us/geforce/guides/',
                'filename': 'nvidia_gaming_optimization_guide.pdf'
            },
            {
                'url': 'https://www.amd.com/en/support/graphics/amd-radeon-6000-series',
                'filename': 'amd_gaming_setup_guide.pdf'
            }
        ]
    },
    
    # Warranty and Return Policies (Template)
    {
        'category': 'policies',
        'manufacturer': 'general',
        'description': 'Sample Warranty and Return Policies',
        'direct_pdfs': [
            # Note: You'll need to replace these with your actual store policies
            # These are placeholder URLs - create your own policy documents
            {
                'url': 'https://example.com/your-store-warranty-policy.pdf',
                'filename': 'store_warranty_policy.pdf'
            },
            {
                'url': 'https://example.com/your-store-return-policy.pdf',
                'filename': 'store_return_policy.pdf'
            }
        ]
    }
]

# Additional manufacturer-specific configurations
MANUFACTURER_SUPPORT_URLS = {
    'dell': {
        'base_url': 'https://www.dell.com/support/manuals/',
        'search_patterns': ['/manuals/', '/drivers/', '/documentation/'],
        'file_types': ['.pdf', '.doc', '.docx']
    },
    'hp': {
        'base_url': 'https://support.hp.com/us-en/drivers/manuals',
        'search_patterns': ['/manuals/', '/drivers/', '/support/'],
        'file_types': ['.pdf', '.doc']
    },
    'lenovo': {
        'base_url': 'https://support.lenovo.com/us/en/manuals',
        'search_patterns': ['/manuals/', '/documentation/', '/guides/'],
        'file_types': ['.pdf']
    },
    'asus': {
        'base_url': 'https://www.asus.com/support/download-center/',
        'search_patterns': ['/support/', '/download/', '/manual/'],
        'file_types': ['.pdf', '.zip']
    },
    'msi': {
        'base_url': 'https://www.msi.com/support/',
        'search_patterns': ['/support/', '/download/', '/manual/'],
        'file_types': ['.pdf']
    }
}

# Search terms for different document types
DOCUMENT_SEARCH_TERMS = {
    'manuals': ['manual', 'user guide', 'setup guide', 'installation guide', 'getting started'],
    'troubleshooting': ['troubleshooting', 'problem solving', 'fix', 'repair', 'diagnostic'],
    'specifications': ['specifications', 'specs', 'technical specifications', 'datasheet'],
    'drivers': ['driver', 'drivers', 'software', 'utilities'],
    'warranty': ['warranty', 'guarantee', 'coverage', 'terms', 'conditions'],
    'faqs': ['faq', 'frequently asked', 'common questions', 'help']
}
