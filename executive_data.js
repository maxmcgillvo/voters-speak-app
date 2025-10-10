// Executive Branch Data - Updated October 10, 2025
// Current Administration (2025-2029)

const executiveData = [
    // President & Vice President
    {name: "Donald J. Trump", title: "President", party: "Republican", email: "comments@whitehouse.gov", phone: "202-456-1111", office: "The White House", website: "https://www.whitehouse.gov"},
    {name: "JD Vance", title: "Vice President", party: "Republican", email: "comments@whitehouse.gov", phone: "202-456-1111", office: "The White House", website: "https://www.whitehouse.gov"},
    
    // Cabinet Members (2025-2029 Administration)
    {name: "Marco Rubio", title: "Secretary of State", party: "Republican", email: "contact@state.gov", phone: "202-647-6575", office: "U.S. Department of State", website: "https://www.state.gov"},
    {name: "Scott Bessent", title: "Secretary of the Treasury", party: "Republican", email: "contact@treasury.gov", phone: "202-622-2000", office: "U.S. Department of Treasury", website: "https://www.treasury.gov"},
    {name: "Pete Hegseth", title: "Secretary of Defense", party: "Republican", email: "contact@defense.gov", phone: "703-571-3343", office: "U.S. Department of Defense", website: "https://www.defense.gov"},
    {name: "Pam Bondi", title: "Attorney General", party: "Republican", email: "contact@usdoj.gov", phone: "202-514-2000", office: "U.S. Department of Justice", website: "https://www.justice.gov"},
    {name: "Doug Burgum", title: "Secretary of the Interior", party: "Republican", email: "contact@ios.doi.gov", phone: "202-208-3100", office: "U.S. Department of the Interior", website: "https://www.doi.gov"},
    {name: "Brooke Rollins", title: "Secretary of Agriculture", party: "Republican", email: "contact@usda.gov", phone: "202-720-2791", office: "U.S. Department of Agriculture", website: "https://www.usda.gov"},
    {name: "Howard Lutnick", title: "Secretary of Commerce", party: "Republican", email: "contact@doc.gov", phone: "202-482-2000", office: "U.S. Department of Commerce", website: "https://www.commerce.gov"},
    {name: "Lori Chavez-DeRemer", title: "Secretary of Labor", party: "Republican", email: "contact@dol.gov", phone: "1-866-4-USA-DOL", office: "U.S. Department of Labor", website: "https://www.dol.gov"},
    {name: "Robert F. Kennedy Jr.", title: "Secretary of Health and Human Services", party: "Republican", email: "contact@hhs.gov", phone: "877-696-6775", office: "U.S. Department of Health and Human Services", website: "https://www.hhs.gov"},
    {name: "Scott Turner", title: "Secretary of Housing and Urban Development", party: "Republican", email: "contact@hud.gov", phone: "202-708-1112", office: "U.S. Department of Housing and Urban Development", website: "https://www.hud.gov"},
    {name: "Sean Duffy", title: "Secretary of Transportation", party: "Republican", email: "contact@dot.gov", phone: "202-366-4000", office: "U.S. Department of Transportation", website: "https://www.transportation.gov"},
    {name: "Chris Wright", title: "Secretary of Energy", party: "Republican", email: "contact@energy.gov", phone: "202-586-5000", office: "U.S. Department of Energy", website: "https://www.energy.gov"},
    {name: "Linda McMahon", title: "Secretary of Education", party: "Republican", email: "contact@ed.gov", phone: "1-800-USA-LEARN", office: "U.S. Department of Education", website: "https://www.ed.gov"},
    {name: "Kristi Noem", title: "Secretary of Homeland Security", party: "Republican", email: "contact@dhs.gov", phone: "202-282-8000", office: "U.S. Department of Homeland Security", website: "https://www.dhs.gov"},
    {name: "Elise Stefanik", title: "U.S. Ambassador to the United Nations", party: "Republican", email: "usun@state.gov", phone: "212-415-4000", office: "U.S. Mission to the United Nations", website: "https://usun.usmission.gov"}
];

// Method to prevent constant recreation - Dataset versioning system
const datasetMetadata = {
    lastUpdated: "2025-10-10",
    version: "1.0.0",
    administration: "2025-2029",
    dataSources: ["official government websites", "whitehouse.gov", "congress.gov"],
    updateCheckUrl: "https://api.gov/datasets/version-check",
    nextUpdate: "2025-12-31"
};

// Export with metadata
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { executiveData, datasetMetadata };
}