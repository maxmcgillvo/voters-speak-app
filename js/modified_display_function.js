/**
 * Modified Display Function for Voters Speak App
 * Updated to integrate the Social Media Component
 * This replaces the existing displayOfficials function in index.html
 */

/**
 * Enhanced displayOfficials function with Social Media Component integration
 * @param {string} containerId - ID of the container element
 * @param {Array} officials - Array of official data objects
 */
function displayOfficials(containerId, officials) {
    const container = document.getElementById(containerId);
    if (!container) {
        console.error(`Container with ID "${containerId}" not found`);
        return;
    }

    // Clear existing content
    container.innerHTML = '';

    // Initialize Social Media Component if not already done
    if (!window.socialMediaComponent) {
        window.socialMediaComponent = new SocialMediaComponent();
        window.socialMediaComponent.addStyles();
    }

    // Create each official card using DOM manipulation for better performance
    officials.forEach(official => {
        const card = createOfficialCard(official);
        container.appendChild(card);
    });
}

/**
 * Create an individual official card element
 * @param {Object} official - Official data object
 * @returns {HTMLElement} - Complete official card element
 */
function createOfficialCard(official) {
    // Main card container
    const card = document.createElement('div');
    card.className = 'official-card';
    card.setAttribute('role', 'article');
    card.setAttribute('aria-label', `Contact information for ${official.name}`);

    // Create card header
    const header = createOfficialHeader(official);
    card.appendChild(header);

    // Create card details
    const details = createOfficialDetails(official);
    card.appendChild(details);

    return card;
}

/**
 * Create the header section of an official card
 * @param {Object} official - Official data object
 * @returns {HTMLElement} - Header element
 */
function createOfficialHeader(official) {
    const header = document.createElement('div');
    header.className = 'official-header';

    // Name and title container
    const nameContainer = document.createElement('div');
    
    const nameDiv = document.createElement('div');
    nameDiv.className = 'official-name';
    nameDiv.textContent = official.name;
    nameContainer.appendChild(nameDiv);

    const titleDiv = document.createElement('div');
    titleDiv.className = 'official-title';
    titleDiv.textContent = official.title + (official.district ? ` - ${official.district}` : '');
    nameContainer.appendChild(titleDiv);

    header.appendChild(nameContainer);

    // Party badge
    const partyBadge = document.createElement('span');
    partyBadge.className = `party-badge party-${official.party.toLowerCase()}`;
    partyBadge.textContent = official.party;
    header.appendChild(partyBadge);

    return header;
}

/**
 * Create the details section of an official card
 * @param {Object} official - Official data object
 * @returns {HTMLElement} - Details element
 */
function createOfficialDetails(official) {
    const details = document.createElement('div');
    details.className = 'official-details';

    // Add standard contact items
    const contactItems = [
        { type: 'state', value: official.state },
        { type: 'email', value: official.email },
        { type: 'phone', value: official.phone },
        { type: 'office', value: official.office },
        { type: 'website', value: official.website }
    ];

    contactItems.forEach(item => {
        if (item.value) {
            const contactItem = createContactItem(item.type, item.value, official);
            details.appendChild(contactItem);
        }
    });

    // Add social media component if social media data exists
    if (official.socialMedia && Object.keys(official.socialMedia).length > 0) {
        const socialMediaContainer = createSocialMediaContainer(official.socialMedia, official.name);
        details.appendChild(socialMediaContainer);
    }

    // Add appointment info for judicial officials
    if (official.appointment_year) {
        const appointmentItem = document.createElement('div');
        appointmentItem.className = 'contact-item';
        appointmentItem.innerHTML = `<strong>Appointed:</strong> ${official.appointment_year} by ${official.appointed_by}`;
        details.appendChild(appointmentItem);
    }

    return details;
}

/**
 * Create a contact item element
 * @param {string} type - Type of contact item
 * @param {string} value - Contact value
 * @param {Object} official - Official data object
 * @returns {HTMLElement} - Contact item element
 */
function createContactItem(type, value, official) {
    const item = document.createElement('div');
    item.className = 'contact-item';

    // Add icon based on type
    const icon = createContactIcon(type);
    item.appendChild(icon);

    // Add content based on type
    const content = createContactContent(type, value, official);
    item.appendChild(content);

    return item;
}

/**
 * Create contact icon SVG element
 * @param {string} type - Type of contact
 * @returns {HTMLElement} - SVG icon element
 */
function createContactIcon(type) {
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('class', 'contact-icon');
    svg.setAttribute('viewBox', '0 0 24 24');

    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    
    const iconPaths = {
        state: 'M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z',
        email: 'M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.89 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z',
        phone: 'M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z',
        office: 'M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z',
        website: 'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z'
    };

    path.setAttribute('d', iconPaths[type] || iconPaths.website);
    svg.appendChild(path);

    return svg;
}

/**
 * Create contact content element
 * @param {string} type - Type of contact
 * @param {string} value - Contact value
 * @param {Object} official - Official data object
 * @returns {HTMLElement} - Content element or text node
 */
function createContactContent(type, value, official) {
    if (type === 'email') {
        const link = document.createElement('a');
        link.href = `mailto:${value}`;
        link.textContent = value;
        link.setAttribute('aria-label', `Send email to ${official.name}`);
        return link;
    }

    if (type === 'phone') {
        const container = document.createElement('div');
        container.style.cursor = 'pointer';
        container.title = `Click to call ${value}`;
        
        const cleanNumber = value.replace(/[^\d]/g, '');
        container.onclick = () => handlePhoneClick(cleanNumber, value);

        const link = document.createElement('a');
        link.href = `tel:+1${cleanNumber}`;
        link.onclick = (e) => {
            e.stopPropagation();
            return handlePhoneClick(cleanNumber, value);
        };
        link.style.cssText = 'color: inherit; text-decoration: none;';
        link.title = `Click to call ${value}`;
        link.textContent = value;
        link.setAttribute('aria-label', `Call ${official.name} at ${value}`);
        
        container.appendChild(link);
        return container;
    }

    if (type === 'website') {
        const link = document.createElement('a');
        link.href = value;
        link.target = '_blank';
        link.rel = 'noopener noreferrer';
        link.textContent = 'Official Website';
        link.setAttribute('aria-label', `Visit ${official.name}'s official website`);
        return link;
    }

    // For state and office, return text node
    const textNode = document.createTextNode(value);
    return textNode;
}

/**
 * Create social media container with integrated SocialMediaComponent
 * @param {Object} socialMediaData - Social media handles object
 * @param {string} officialName - Name of the official for accessibility
 * @returns {HTMLElement} - Social media container element
 */
function createSocialMediaContainer(socialMediaData, officialName) {
    const container = document.createElement('div');
    container.className = 'contact-item social-media-item';
    container.setAttribute('aria-label', `Social media profiles for ${officialName}`);

    // Create social media icon
    const icon = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    icon.setAttribute('class', 'contact-icon');
    icon.setAttribute('viewBox', '0 0 24 24');
    icon.setAttribute('aria-hidden', 'true');

    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    path.setAttribute('d', 'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm3.5 6L12 10.5 8.5 8 12 5.5 15.5 8zM8.5 16L12 13.5l3.5 2.5L12 18.5 8.5 16z');
    icon.appendChild(path);

    container.appendChild(icon);

    // Use Social Media Component to render links
    const socialLinksContainer = window.socialMediaComponent.render(socialMediaData, {
        showIcons: true,
        showLabels: false,
        style: 'horizontal',
        maxLinks: 6
    });

    if (socialLinksContainer) {
        container.appendChild(socialLinksContainer);
    } else {
        // Fallback text if no valid social media links
        const fallbackText = document.createTextNode('Social Media');
        container.appendChild(fallbackText);
    }

    return container;
}

// Export functions for testing and external use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        displayOfficials,
        createOfficialCard,
        createOfficialHeader,
        createOfficialDetails,
        createContactItem,
        createSocialMediaContainer
    };
}