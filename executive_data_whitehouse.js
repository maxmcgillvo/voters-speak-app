// Core White House Leadership - Executive Branch
const executiveData = [
    // President & Vice President
    {
        name: "Donald J. Trump",
        title: "President of the United States",
        position: "President",
        branch: "Executive",
        level: "President",
        email: "president@whitehouse.gov",
        phone: "(202) 456-1414",
        website: "https://www.whitehouse.gov/administration/president-trump/",
        office: "The White House",
        address: "1600 Pennsylvania Avenue NW, Washington, DC 20500"
    },
    {
        name: "JD Vance",
        title: "Vice President of the United States",
        position: "Vice President",
        branch: "Executive",
        level: "Vice President",
        email: "vice.president@whitehouse.gov",
        phone: "(202) 456-2326",
        website: "https://www.whitehouse.gov/administration/vice-president-vance/",
        office: "The White House",
        address: "1600 Pennsylvania Avenue NW, Washington, DC 20500"
    },
    
    // Chief of Staff Office
    {
        name: "Susie Wiles",
        title: "White House Chief of Staff",
        position: "Chief of Staff",
        branch: "Executive",
        level: "Senior Staff",
        email: "chief.staff@who.eop.gov",
        phone: "(202) 456-1414",
        website: "https://www.whitehouse.gov/administration/",
        office: "West Wing",
        address: "1600 Pennsylvania Avenue NW, Washington, DC 20500"
    },
    {
        name: "Dan Scavino",
        title: "White House Deputy Chief of Staff",
        position: "Deputy Chief of Staff",
        branch: "Executive",
        level: "Senior Staff",
        email: "deputy.chief.staff@who.eop.gov",
        phone: "(202) 456-1414",
        website: "https://www.whitehouse.gov/administration/",
        office: "West Wing",
        address: "1600 Pennsylvania Avenue NW, Washington, DC 20500"
    },
    
    // Key Senior Advisors
    {
        name: "Stephen Miller",
        title: "Deputy Chief of Staff for Policy & Homeland Security Advisor",
        position: "Senior Policy Advisor",
        branch: "Executive",
        level: "Senior Staff",
        email: "policy.advisor@who.eop.gov",
        phone: "(202) 456-1414",
        website: "https://www.whitehouse.gov/administration/",
        office: "West Wing",
        address: "1600 Pennsylvania Avenue NW, Washington, DC 20500"
    },
    {
        name: "Taylor Budowich",
        title: "Deputy Chief of Staff for Communications & Cabinet Secretary",
        position: "Communications Director",
        branch: "Executive",
        level: "Senior Staff",
        email: "communications@who.eop.gov",
        phone: "(202) 456-1414",
        website: "https://www.whitehouse.gov/administration/",
        office: "West Wing",
        address: "1600 Pennsylvania Avenue NW, Washington, DC 20500"
    },
    
    // Press & Communications
    {
        name: "Karoline Leavitt",
        title: "White House Press Secretary",
        position: "Press Secretary",
        branch: "Executive",
        level: "Senior Staff",
        email: "press@who.eop.gov",
        phone: "(202) 456-1414",
        website: "https://www.whitehouse.gov/briefing-room/",
        office: "West Wing",
        address: "1600 Pennsylvania Avenue NW, Washington, DC 20500"
    },
    
    // National Security Council
    {
        name: "Marco Rubio",
        title: "National Security Advisor (acting)",
        position: "National Security Advisor",
        branch: "Executive",
        level: "Senior Staff",
        email: "nsc@who.eop.gov",
        phone: "(202) 456-1414",
        website: "https://www.whitehouse.gov/nsc/",
        office: "West Wing",
        address: "1600 Pennsylvania Avenue NW, Washington, DC 20500"
    }
];

// Make this available globally for the site
if (typeof window !== 'undefined') {
    window.executiveData = executiveData;
}