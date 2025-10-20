// Cabinet Secretaries - Executive Branch Leadership
const executiveData = [
    // President & Vice President (Core Leadership)
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
        address: "1600 Pennsylvania Avenue NW, Washington, DC 20500",
        socialMedia: {
            x: "realDonaldTrump",
            instagram: "realdonaldtrump",
            truth: "realDonaldTrump"
        }
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
        address: "1600 Pennsylvania Avenue NW, Washington, DC 20500",
        socialMedia: {
            x: "VP",
            instagram: "vp"
        }
    },
    
    // Cabinet Secretaries
    {
        name: "Marco Rubio",
        title: "Secretary of State",
        position: "Secretary of State",
        branch: "Executive",
        level: "Cabinet Secretary",
        email: "public@state.gov",
        phone: "(202) 647-4000",
        website: "https://www.state.gov",
        office: "Department of State",
        address: "2201 C Street NW, Washington, DC 20520",
        socialMedia: {
            x: "SecRubio",
            instagram: "secrubio"
        }
    },
    {
        name: "Scott Bessent",
        title: "Secretary of the Treasury",
        position: "Secretary of Treasury",
        branch: "Executive",
        level: "Cabinet Secretary",
        email: "public@treasury.gov",
        phone: "(202) 622-2000",
        website: "https://home.treasury.gov",
        office: "Department of Treasury",
        address: "1500 Pennsylvania Avenue NW, Washington, DC 20220",
        socialMedia: {
            x: "SecScottBessent"
        }
    },
    {
        name: "Pete Hegseth",
        title: "Secretary of Defense",
        position: "Secretary of Defense",
        branch: "Executive",
        level: "Cabinet Secretary",
        email: "public@defense.gov",
        phone: "(703) 571-3343",
        website: "https://www.defense.gov",
        office: "Department of Defense",
        address: "1000 Defense Pentagon, Washington, DC 20301",
        socialMedia: {
            x: "PeteHegseth",
            facebook: "PeteHegseth",
            instagram: "petehegseth"
        }
    },
    {
        name: "Pam Bondi",
        title: "Attorney General",
        position: "Attorney General",
        branch: "Executive",
        level: "Cabinet Secretary",
        email: "public@usdoj.gov",
        phone: "(202) 514-2000",
        website: "https://www.justice.gov",
        office: "Department of Justice",
        address: "950 Pennsylvania Avenue NW, Washington, DC 20530",
        socialMedia: {
            x: "AGPamBondi",
            instagram: "agpambondi"
        }
    },
    {
        name: "Kristi Noem",
        title: "Secretary of Homeland Security",
        position: "Secretary of Homeland Security",
        branch: "Executive",
        level: "Cabinet Secretary",
        email: "public@dhs.gov",
        phone: "(202) 282-8000",
        website: "https://www.dhs.gov",
        office: "Department of Homeland Security",
        address: "3801 Nebraska Avenue NW, Washington, DC 20528",
        socialMedia: {
            x: "Sec_Noem",
            instagram: "sec_noem",
            facebook: "kristi.noem"
        }
    },
    {
        name: "Linda McMahon",
        title: "Secretary of Education",
        position: "Secretary of Education",
        branch: "Executive",
        level: "Cabinet Secretary",
        email: "public@ed.gov",
        phone: "(800) 872-5327",
        website: "https://www.ed.gov",
        office: "Department of Education",
        address: "400 Maryland Avenue SW, Washington, DC 20202",
        socialMedia: {
            x: "EDSecMcMahon",
            instagram: "edsecmcmahon",
            facebook: "edsecmcmahon",
            linkedin: "lindamcmahon"
        }
    },
    {
        name: "Doug Collins",
        title: "Secretary of Veterans Affairs",
        position: "Secretary of Veterans Affairs",
        branch: "Executive",
        level: "Cabinet Secretary",
        email: "public@va.gov",
        phone: "(800) 827-1000",
        website: "https://www.va.gov",
        office: "Department of Veterans Affairs",
        address: "810 Vermont Avenue NW, Washington, DC 20420",
        socialMedia: {
            x: "SecVetAffairs",
            instagram: "dougcollinsga",
            facebook: "secvetaffairs"
        }
    },
    {
        name: "Russell Vought",
        title: "Director of the Office of Management and Budget",
        position: "OMB Director",
        branch: "Executive",
        level: "Cabinet Secretary",
        email: "public@omb.eop.gov",
        phone: "(202) 395-3080",
        website: "https://www.whitehouse.gov/omb/",
        office: "Office of Management and Budget",
        address: "725 17th Street NW, Washington, DC 20503",
        socialMedia: {
            x: "RussVought45"
        }
    },
    
    // Key White House Staff
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
        address: "1600 Pennsylvania Avenue NW, Washington, DC 20500",
        socialMedia: {
            x: "susiewiles",
            linkedin: "susie-wiles"
        }
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
        address: "1600 Pennsylvania Avenue NW, Washington, DC 20500",
        socialMedia: {
            x: "Scavino47",
            truth: "DanScavino"
        }
    },
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
        address: "1600 Pennsylvania Avenue NW, Washington, DC 20500",
        socialMedia: {
            x: "PressSec",
            instagram: "karolineleavitt",
            facebook: "KarolineLeavittNH"
        }
    },
    
];

// Make this available globally for the site
if (typeof window !== 'undefined') {
    window.executiveData = executiveData;
}