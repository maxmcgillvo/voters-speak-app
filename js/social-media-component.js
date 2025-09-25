/**
 * Social Media Component for Voters Speak App
 * Provides modular social media link functionality for government officials
 */

class SocialMediaComponent {
    constructor() {
        this.socialPlatforms = {
            twitter: {
                name: 'Twitter',
                icon: '🐦',
                baseUrl: 'https://twitter.com/',
                color: '#1DA1F2'
            },
            facebook: {
                name: 'Facebook',
                icon: '📘',
                baseUrl: 'https://facebook.com/',
                color: '#1877F2'
            },
            instagram: {
                name: 'Instagram',
                icon: '📷',
                baseUrl: 'https://instagram.com/',
                color: '#E4405F'
            },
            linkedin: {
                name: 'LinkedIn',
                icon: '💼',
                baseUrl: 'https://linkedin.com/in/',
                color: '#0A66C2'
            },
            youtube: {
                name: 'YouTube',
                icon: '📹',
                baseUrl: 'https://youtube.com/',
                color: '#FF0000'
            },
            tiktok: {
                name: 'TikTok',
                icon: '🎵',
                baseUrl: 'https://tiktok.com/@',
                color: '#000000'
            }
        };
    }

    /**
     * Render social media links for an official
     * @param {Object} socialMedia - Object containing social media handles
     * @param {Object} options - Rendering options
     * @returns {HTMLElement} - Container element with social media links
     */
    render(socialMedia, options = {}) {
        const config = {
            showIcons: true,
            showLabels: false,
            style: 'horizontal', // 'horizontal' or 'vertical'
            maxLinks: 6,
            ...options
        };

        if (!socialMedia || Object.keys(socialMedia).length === 0) {
            return null;
        }

        const container = document.createElement('div');
        container.className = 'social-media-links';
        container.setAttribute('role', 'list');
        container.setAttribute('aria-label', 'Social media profiles');

        // Apply base styles
        this.applyContainerStyles(container, config.style);

        // Render each social media link
        Object.entries(socialMedia)
            .filter(([platform, handle]) => handle && this.socialPlatforms[platform])
            .slice(0, config.maxLinks)
            .forEach(([platform, handle]) => {
                const linkElement = this.createSocialLink(platform, handle, config);
                if (linkElement) {
                    container.appendChild(linkElement);
                }
            });

        return container.children.length > 0 ? container : null;
    }

    /**
     * Create a single social media link
     * @param {string} platform - Social media platform key
     * @param {string} handle - User handle/username
     * @param {Object} config - Configuration options
     * @returns {HTMLElement} - Link element
     */
    createSocialLink(platform, handle, config) {
        const platformInfo = this.socialPlatforms[platform];
        if (!platformInfo || !handle) {
            return null;
        }

        const link = document.createElement('a');
        const cleanHandle = handle.replace('@', '');
        const url = platformInfo.baseUrl + cleanHandle;
        
        // Set link attributes
        link.href = url;
        link.target = '_blank';
        link.rel = 'noopener noreferrer';
        link.className = 'social-link';
        link.setAttribute('role', 'listitem');
        link.setAttribute('aria-label', `${platformInfo.name} profile`);
        link.title = `Follow on ${platformInfo.name}`;

        // Create link content
        let linkContent = '';
        if (config.showIcons) {
            linkContent += `<span class="social-icon" aria-hidden="true">${platformInfo.icon}</span>`;
        }
        if (config.showLabels) {
            linkContent += `<span class="social-label">${platformInfo.name}</span>`;
        }
        if (!config.showIcons && !config.showLabels) {
            linkContent = platformInfo.icon; // fallback to icon
        }

        link.innerHTML = linkContent;

        // Apply link styles
        this.applySocialLinkStyles(link, platformInfo, config);

        return link;
    }

    /**
     * Apply styles to the container
     * @param {HTMLElement} container - Container element
     * @param {string} style - Layout style
     */
    applyContainerStyles(container, style) {
        const baseStyles = {
            display: 'flex',
            gap: '8px',
            alignItems: 'center',
            flexWrap: 'wrap',
            marginTop: '5px'
        };

        if (style === 'vertical') {
            baseStyles.flexDirection = 'column';
            baseStyles.alignItems = 'flex-start';
        }

        Object.assign(container.style, baseStyles);
    }

    /**
     * Apply styles to individual social links
     * @param {HTMLElement} link - Link element
     * @param {Object} platformInfo - Platform information
     * @param {Object} config - Configuration options
     */
    applySocialLinkStyles(link, platformInfo, config) {
        const baseStyles = {
            display: 'inline-flex',
            alignItems: 'center',
            gap: '4px',
            padding: '6px 10px',
            borderRadius: '15px',
            textDecoration: 'none',
            fontSize: '0.85rem',
            fontWeight: '500',
            transition: 'all 0.2s ease',
            backgroundColor: '#f8f9fa',
            color: platformInfo.color,
            border: `1px solid ${platformInfo.color}20`,
            minWidth: '36px',
            justifyContent: 'center'
        };

        // Apply hover effects
        link.addEventListener('mouseenter', () => {
            link.style.backgroundColor = platformInfo.color;
            link.style.color = 'white';
            link.style.transform = 'translateY(-1px)';
            link.style.boxShadow = `0 2px 8px ${platformInfo.color}30`;
        });

        link.addEventListener('mouseleave', () => {
            link.style.backgroundColor = '#f8f9fa';
            link.style.color = platformInfo.color;
            link.style.transform = 'translateY(0)';
            link.style.boxShadow = 'none';
        });

        Object.assign(link.style, baseStyles);
    }

    /**
     * Add CSS styles to the document
     * This method can be called once to add component styles
     */
    addStyles() {
        if (document.getElementById('social-media-component-styles')) {
            return; // Styles already added
        }

        const styles = `
            <style id="social-media-component-styles">
                .social-media-links {
                    margin-top: 8px;
                }
                
                .social-link:focus {
                    outline: 2px solid #4A90E2;
                    outline-offset: 2px;
                }
                
                .social-link:active {
                    transform: translateY(0) scale(0.95);
                }
                
                .social-icon {
                    display: inline-block;
                    line-height: 1;
                }
                
                .social-label {
                    font-weight: 500;
                }
                
                @media (max-width: 480px) {
                    .social-media-links {
                        gap: 6px;
                    }
                    
                    .social-link {
                        padding: 4px 8px !important;
                        font-size: 0.8rem !important;
                    }
                }
                
                /* High contrast mode support */
                @media (prefers-contrast: high) {
                    .social-link {
                        border-width: 2px !important;
                        font-weight: bold !important;
                    }
                }
                
                /* Reduced motion support */
                @media (prefers-reduced-motion: reduce) {
                    .social-link {
                        transition: none !important;
                    }
                }
            </style>
        `;
        
        document.head.insertAdjacentHTML('beforeend', styles);
    }

    /**
     * Initialize the component and add styles to document
     */
    static init() {
        const component = new SocialMediaComponent();
        component.addStyles();
        return component;
    }
}

// Auto-initialize when script loads
if (typeof window !== 'undefined') {
    window.SocialMediaComponent = SocialMediaComponent;
    // Initialize component styles
    document.addEventListener('DOMContentLoaded', () => {
        SocialMediaComponent.init();
    });
}