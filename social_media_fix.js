// Emergency Social Media Display Fix
// This will ensure social media icons show up with emojis

// Simple social media display function that works without external dependencies
function displaySocialMediaSimple(socialMediaData) {
    if (!socialMediaData || Object.keys(socialMediaData).length === 0) {
        return '';
    }
    
    let socialHtml = '<div style="background: #fffacd; padding: 8px; margin: 5px 0; border-radius: 4px;">';
    socialHtml += '<strong>Social Media:</strong> ';
    
    const platforms = [];
    if (socialMediaData.twitter) {
        platforms.push(`🐦 <a href="https://twitter.com/${socialMediaData.twitter}" target="_blank" style="color: #1DA1F2; text-decoration: none;">@${socialMediaData.twitter}</a>`);
    }
    if (socialMediaData.facebook) {
        platforms.push(`📘 <a href="https://facebook.com/${socialMediaData.facebook}" target="_blank" style="color: #1877F2; text-decoration: none;">${socialMediaData.facebook}</a>`);
    }
    if (socialMediaData.instagram) {
        platforms.push(`📷 <a href="https://instagram.com/${socialMediaData.instagram}" target="_blank" style="color: #E4405F; text-decoration: none;">@${socialMediaData.instagram}</a>`);
    }
    if (socialMediaData.linkedin) {
        platforms.push(`💼 <a href="https://linkedin.com/in/${socialMediaData.linkedin}" target="_blank" style="color: #0077B5; text-decoration: none;">${socialMediaData.linkedin}</a>`);
    }
    
    socialHtml += platforms.join(' | ');
    socialHtml += '</div>';
    
    return socialHtml;
}

// Override the existing displayOfficials function to ensure social media shows
function displayOfficialsWithSocialMedia(containerId, officials) {
    const container = document.getElementById(containerId);
    if (!container) {
        console.error(`Container with ID "${containerId}" not found`);
        return;
    }

    container.innerHTML = '';

    officials.forEach(official => {
        const card = document.createElement('div');
        card.className = 'official-card';
        card.style.cssText = 'background: white; border: 1px solid #ddd; border-radius: 8px; padding: 15px; margin: 10px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1);';

        let cardHTML = `
            <div style="border-bottom: 1px solid #eee; padding-bottom: 10px; margin-bottom: 10px;">
                <h3 style="margin: 0; color: #333;">${official.name}</h3>
                <p style="margin: 5px 0; color: #666; font-weight: bold;">${official.title}</p>
            </div>
            <div style="display: grid; gap: 8px;">
                <div><strong>State:</strong> ${official.state}</div>
                <div><strong>Party:</strong> ${official.party}</div>
                <div><strong>Email:</strong> <a href="mailto:${official.email}" style="color: #0066cc;">${official.email}</a></div>
                <div><strong>Phone:</strong> <a href="tel:${official.phone}" style="color: #0066cc;">${official.phone}</a></div>
                <div><strong>Office:</strong> ${official.office}</div>
                <div><strong>Website:</strong> <a href="${official.website}" target="_blank" style="color: #0066cc;">Visit Website</a></div>
        `;

        // Add social media if it exists
        if (official.socialMedia && Object.keys(official.socialMedia).length > 0) {
            cardHTML += displaySocialMediaSimple(official.socialMedia);
        }

        cardHTML += '</div>';
        card.innerHTML = cardHTML;
        container.appendChild(card);
    });

    console.log(`✅ Displayed ${officials.length} officials in ${containerId}`);
}

// Replace the existing display functions
window.displayOfficials = displayOfficialsWithSocialMedia;

console.log("🔧 Social Media Fix loaded - social media should now display with emojis!");