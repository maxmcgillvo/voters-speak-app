// Enhanced phone link solution for cross-platform compatibility

function createPhoneLink(phoneNumber, displayText) {
    const cleanNumber = phoneNumber.replace(/[^\d]/g, '');
    const telLink = `tel:+1${cleanNumber}`;
    
    // Detect platform
    const isMac = navigator.platform.toUpperCase().indexOf('MAC') >= 0;
    const isDesktop = !/Mobi|Android/i.test(navigator.userAgent);
    const isSafari = /^((?!chrome|android).)*safari/i.test(navigator.userAgent);
    
    let clickHandler = '';
    
    if (isMac && isDesktop) {
        // Mac Desktop - provide multiple options
        clickHandler = `onclick="handleMacDesktopCall('${cleanNumber}', '${phoneNumber}'); return false;"`;
    }
    
    return `<a href="${telLink}" ${clickHandler} style="color: inherit; text-decoration: none;" title="Click to call ${phoneNumber}">${displayText || phoneNumber}</a>`;
}

function handleMacDesktopCall(cleanNumber, formattedNumber) {
    console.log("Mac Desktop call attempt:", cleanNumber);
    
    // Try tel: link first
    window.location.href = `tel:+1${cleanNumber}`;
    
    // Show user-friendly options
    setTimeout(() => {
        showMacCallOptions(formattedNumber, cleanNumber);
    }, 500);
}

function showMacCallOptions(formattedNumber, cleanNumber) {
    const options = `
        <div style="position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); 
                    background: white; border: 2px solid #007bff; border-radius: 10px; 
                    padding: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.3); z-index: 1000;">
            <h3 style="margin-top: 0;">📞 Call Options</h3>
            <p><strong>${formattedNumber}</strong></p>
            
            <button onclick="attemptCall('${cleanNumber}')" style="display: block; width: 100%; 
                    padding: 10px; margin: 5px 0; background: #007bff; color: white; 
                    border: none; border-radius: 5px; cursor: pointer;">
                Try FaceTime/Continuity Call
            </button>
            
            <button onclick="copyPhoneNumber('${formattedNumber}')" style="display: block; width: 100%; 
                    padding: 10px; margin: 5px 0; background: #28a745; color: white; 
                    border: none; border-radius: 5px; cursor: pointer;">
                Copy Phone Number
            </button>
            
            <button onclick="closeCallOptions()" style="display: block; width: 100%; 
                    padding: 10px; margin: 5px 0; background: #6c757d; color: white; 
                    border: none; border-radius: 5px; cursor: pointer;">
                Cancel
            </button>
            
            <p style="font-size: 12px; color: #666; margin-bottom: 0;">
                💡 Tip: On Mac, you can also use FaceTime or iPhone continuity features
            </p>
        </div>
        <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; 
                    background: rgba(0,0,0,0.5); z-index: 999;" onclick="closeCallOptions()"></div>
    `;
    
    const div = document.createElement('div');
    div.id = 'macCallOptions';
    div.innerHTML = options;
    document.body.appendChild(div);
}

function attemptCall(cleanNumber) {
    window.location.href = `tel:+1${cleanNumber}`;
    closeCallOptions();
}

function copyPhoneNumber(phoneNumber) {
    navigator.clipboard.writeText(phoneNumber).then(() => {
        alert(`Phone number copied: ${phoneNumber}`);
        closeCallOptions();
    }).catch(err => {
        alert('Copy failed. Please select and copy manually: ' + phoneNumber);
    });
}

function closeCallOptions() {
    const options = document.getElementById('macCallOptions');
    if (options) {
        options.remove();
    }
}

// Alternative: Show phone number with copy button
function createPhoneWithCopy(phoneNumber) {
    const cleanNumber = phoneNumber.replace(/[^\d]/g, '');
    const telLink = `tel:+1${cleanNumber}`;
    
    return `
        <div style="display: inline-flex; align-items: center; gap: 8px;">
            <a href="${telLink}" onclick="handlePhoneClick('${cleanNumber}', '${phoneNumber}'); return false;" 
               style="color: inherit; text-decoration: none;" title="Click to call">
                ${phoneNumber}
            </a>
            <button onclick="copyPhoneNumber('${phoneNumber}')" 
                    style="background: #f8f9fa; border: 1px solid #dee2e6; border-radius: 3px; 
                           padding: 2px 6px; font-size: 12px; cursor: pointer;" 
                    title="Copy phone number">
                📋
            </button>
        </div>
    `;
}

function handlePhoneClick(cleanNumber, formattedNumber) {
    const isMac = navigator.platform.toUpperCase().indexOf('MAC') >= 0;
    const isDesktop = !/Mobi|Android/i.test(navigator.userAgent);
    
    if (isMac && isDesktop) {
        handleMacDesktopCall(cleanNumber, formattedNumber);
    } else {
        // For other platforms, try tel: link directly
        window.location.href = `tel:+1${cleanNumber}`;
    }
}