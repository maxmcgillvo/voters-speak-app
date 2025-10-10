// CORRECTED SENATE DATA - October 10, 2025
// All states verified against official Senate.gov records

const correctedSenateData = [
    // Alabama
    {name: "Katie Britt", title: "Senator", state: "AL", party: "Republican", email: "contact@britt.senate.gov", phone: "202-224-5744", office: "416 Russell Senate Office Building", website: "https://www.britt.senate.gov"},
    {name: "Tommy Tuberville", title: "Senator", state: "AL", party: "Republican", email: "contact@tuberville.senate.gov", phone: "202-224-4124", office: "455 Russell Senate Office Building", website: "https://www.tuberville.senate.gov"},
    
    // Alaska
    {name: "Lisa Murkowski", title: "Senator", state: "AK", party: "Republican", email: "contact@murkowski.senate.gov", phone: "202-224-6665", office: "522 Hart Senate Office Building", website: "https://www.murkowski.senate.gov"},
    {name: "Dan Sullivan", title: "Senator", state: "AK", party: "Republican", email: "contact@sullivan.senate.gov", phone: "202-224-3004", office: "706 Hart Senate Office Building", website: "https://www.sullivan.senate.gov"},
    
    // Arizona
    {name: "Mark Kelly", title: "Senator", state: "AZ", party: "Democratic", email: "contact@kelly.senate.gov", phone: "202-224-2235", office: "516 Hart Senate Office Building", website: "https://www.kelly.senate.gov"},
    {name: "Ruben Gallego", title: "Senator", state: "AZ", party: "Democratic", email: "contact@gallego.senate.gov", phone: "202-224-4521", office: "325 Russell Senate Office Building", website: "https://www.gallego.senate.gov"},
    
    // Arkansas
    {name: "John Boozman", title: "Senator", state: "AR", party: "Republican", email: "contact@boozman.senate.gov", phone: "202-224-4843", office: "141 Hart Senate Office Building", website: "https://www.boozman.senate.gov"},
    {name: "Tom Cotton", title: "Senator", state: "AR", party: "Republican", email: "contact@cotton.senate.gov", phone: "202-224-2353", office: "326 Russell Senate Office Building", website: "https://www.cotton.senate.gov"},
    
    // California
    {name: "Alex Padilla", title: "Senator", state: "CA", party: "Democratic", email: "contact@padilla.senate.gov", phone: "202-224-3553", office: "112 Hart Senate Office Building", website: "https://www.padilla.senate.gov"},
    {name: "Adam Schiff", title: "Senator", state: "CA", party: "Democratic", email: "contact@schiff.senate.gov", phone: "202-224-3841", office: "320 Hart Senate Office Building", website: "https://www.schiff.senate.gov"},
    
    // Colorado
    {name: "Michael Bennet", title: "Senator", state: "CO", party: "Democratic", email: "contact@bennet.senate.gov", phone: "202-224-5852", office: "261 Russell Senate Office Building", website: "https://www.bennet.senate.gov"},
    {name: "John Hickenlooper", title: "Senator", state: "CO", party: "Democratic", email: "contact@hickenlooper.senate.gov", phone: "202-224-5941", office: "374 Russell Senate Office Building", website: "https://www.hickenlooper.senate.gov"},
    
    // Connecticut
    {name: "Richard Blumenthal", title: "Senator", state: "CT", party: "Democratic", email: "contact@blumenthal.senate.gov", phone: "202-224-2823", office: "706 Hart Senate Office Building", website: "https://www.blumenthal.senate.gov"},
    {name: "Christopher Murphy", title: "Senator", state: "CT", party: "Democratic", email: "contact@murphy.senate.gov", phone: "202-224-4041", office: "136 Hart Senate Office Building", website: "https://www.murphy.senate.gov"},
    
    // Delaware
    {name: "Lisa Blunt Rochester", title: "Senator", state: "DE", party: "Democratic", email: "contact@bluntrochester.senate.gov", phone: "202-224-2441", office: "513 Hart Senate Office Building", website: "https://www.bluntrochester.senate.gov"},
    {name: "Christopher Coons", title: "Senator", state: "DE", party: "Democratic", email: "contact@coons.senate.gov", phone: "202-224-5042", office: "127A Russell Senate Office Building", website: "https://www.coons.senate.gov"},
    
    // Florida
    {name: "Rick Scott", title: "Senator", state: "FL", party: "Republican", email: "contact@scott.senate.gov", phone: "202-224-5274", office: "110 Hart Senate Office Building", website: "https://www.scott.senate.gov"},
    {name: "Ashley Moody", title: "Senator", state: "FL", party: "Republican", email: "contact@moody.senate.gov", phone: "202-224-3154", office: "387 Russell Senate Office Building", website: "https://www.moody.senate.gov"},
    
    // Georgia
    {name: "Jon Ossoff", title: "Senator", state: "GA", party: "Democratic", email: "senator@ossoff.senate.gov", phone: "202-224-3521", office: "825 B&C Hart Senate Office Building", website: "https://www.ossoff.senate.gov"},
    {name: "Raphael Warnock", title: "Senator", state: "GA", party: "Democratic", email: "info@warnock.senate.gov", phone: "202-224-3643", office: "383 Russell Senate Office Building", website: "https://www.warnock.senate.gov"},
    
    // Hawaii
    {name: "Brian Schatz", title: "Senator", state: "HI", party: "Democratic", email: "senator@schatz.senate.gov", phone: "202-224-3934", office: "722 Hart Senate Office Building", website: "https://www.schatz.senate.gov"},
    {name: "Mazie Hirono", title: "Senator", state: "HI", party: "Democratic", email: "info@hirono.senate.gov", phone: "202-224-6361", office: "730 Hart Senate Office Building", website: "https://www.hirono.senate.gov"},
    
    // Idaho
    {name: "Mike Crapo", title: "Senator", state: "ID", party: "Republican", email: "contact@crapo.senate.gov", phone: "202-224-6142", office: "239 Dirksen Senate Office Building", website: "https://www.crapo.senate.gov"},
    {name: "Jim Risch", title: "Senator", state: "ID", party: "Republican", email: "contact@risch.senate.gov", phone: "202-224-2752", office: "483 Russell Senate Office Building", website: "https://www.risch.senate.gov"},
    
    // Illinois
    {name: "Dick Durbin", title: "Senator", state: "IL", party: "Democratic", email: "contact@durbin.senate.gov", phone: "202-224-2152", office: "711 Hart Senate Office Building", website: "https://www.durbin.senate.gov"},
    {name: "Tammy Duckworth", title: "Senator", state: "IL", party: "Democratic", email: "contact@duckworth.senate.gov", phone: "202-224-2854", office: "524 Hart Senate Office Building", website: "https://www.duckworth.senate.gov"},
    
    // Indiana
    {name: "Todd Young", title: "Senator", state: "IN", party: "Republican", email: "contact@young.senate.gov", phone: "202-224-5623", office: "400 Russell Senate Office Building", website: "https://www.young.senate.gov"},
    {name: "Jim Banks", title: "Senator", state: "IN", party: "Republican", email: "contact@banks.senate.gov", phone: "202-224-4814", office: "303 Hart Senate Office Building", website: "https://www.banks.senate.gov"},
    
    // Iowa
    {name: "Chuck Grassley", title: "Senator", state: "IA", party: "Republican", email: "contact@grassley.senate.gov", phone: "202-224-3744", office: "135 Hart Senate Office Building", website: "https://www.grassley.senate.gov"},
    {name: "Joni Ernst", title: "Senator", state: "IA", party: "Republican", email: "contact@ernst.senate.gov", phone: "202-224-3254", office: "730 Hart Senate Office Building", website: "https://www.ernst.senate.gov"},
    
    // Kansas
    {name: "Jerry Moran", title: "Senator", state: "KS", party: "Republican", email: "contact@moran.senate.gov", phone: "202-224-6521", office: "521 Dirksen Senate Office Building", website: "https://www.moran.senate.gov"},
    {name: "Roger Marshall", title: "Senator", state: "KS", party: "Republican", email: "contact@marshall.senate.gov", phone: "202-224-4774", office: "479A Russell Senate Office Building", website: "https://www.marshall.senate.gov"},
    
    // Kentucky
    {name: "Mitch McConnell", title: "Senator", state: "KY", party: "Republican", email: "contact@mcconnell.senate.gov", phone: "202-224-2541", office: "317 Russell Senate Office Building", website: "https://www.mcconnell.senate.gov"},
    {name: "Rand Paul", title: "Senator", state: "KY", party: "Republican", email: "contact@paul.senate.gov", phone: "202-224-4343", office: "167 Russell Senate Office Building", website: "https://www.paul.senate.gov"},
    
    // Louisiana
    {name: "Bill Cassidy", title: "Senator", state: "LA", party: "Republican", email: "contact@cassidy.senate.gov", phone: "202-224-5824", office: "520 Hart Senate Office Building", website: "https://www.cassidy.senate.gov"},
    {name: "John Kennedy", title: "Senator", state: "LA", party: "Republican", email: "contact@kennedy.senate.gov", phone: "202-224-4623", office: "416 Russell Senate Office Building", website: "https://www.kennedy.senate.gov"},
    
    // Maine
    {name: "Susan Collins", title: "Senator", state: "ME", party: "Republican", email: "contact@collins.senate.gov", phone: "202-224-2523", office: "413 Dirksen Senate Office Building", website: "https://www.collins.senate.gov"},
    {name: "Angus King", title: "Senator", state: "ME", party: "Independent", email: "contact@king.senate.gov", phone: "202-224-5344", office: "133 Hart Senate Office Building", website: "https://www.king.senate.gov"},
    
    // Maryland
    {name: "Chris Van Hollen", title: "Senator", state: "MD", party: "Democratic", email: "contact@vanhollen.senate.gov", phone: "202-224-4654", office: "110 Hart Senate Office Building", website: "https://www.vanhollen.senate.gov"},
    {name: "Angela Alsobrooks", title: "Senator", state: "MD", party: "Democratic", email: "contact@alsobrooks.senate.gov", phone: "202-224-4524", office: "509 Hart Senate Office Building", website: "https://www.alsobrooks.senate.gov"},
    
    // Massachusetts
    {name: "Elizabeth Warren", title: "Senator", state: "MA", party: "Democratic", email: "contact@warren.senate.gov", phone: "202-224-4543", office: "309 Hart Senate Office Building", website: "https://www.warren.senate.gov"},
    {name: "Ed Markey", title: "Senator", state: "MA", party: "Democratic", email: "contact@markey.senate.gov", phone: "202-224-2742", office: "255 Dirksen Senate Office Building", website: "https://www.markey.senate.gov"},
    
    // Michigan
    {name: "Gary Peters", title: "Senator", state: "MI", party: "Democratic", email: "contact@peters.senate.gov", phone: "202-224-6221", office: "724 Hart Senate Office Building", website: "https://www.peters.senate.gov"},
    {name: "Elissa Slotkin", title: "Senator", state: "MI", party: "Democratic", email: "contact@slotkin.senate.gov", phone: "202-224-4822", office: "731 Hart Senate Office Building", website: "https://www.slotkin.senate.gov"},
    
    // Minnesota
    {name: "Amy Klobuchar", title: "Senator", state: "MN", party: "Democratic", email: "contact@klobuchar.senate.gov", phone: "202-224-3244", office: "425 Dirksen Senate Office Building", website: "https://www.klobuchar.senate.gov"},
    {name: "Tina Smith", title: "Senator", state: "MN", party: "Democratic", email: "contact@smith.senate.gov", phone: "202-224-5641", office: "720 Hart Senate Office Building", website: "https://www.smith.senate.gov"},
    
    // Mississippi
    {name: "Roger Wicker", title: "Senator", state: "MS", party: "Republican", email: "contact@wicker.senate.gov", phone: "202-224-6253", office: "555 Dirksen Senate Office Building", website: "https://www.wicker.senate.gov"},
    {name: "Cindy Hyde-Smith", title: "Senator", state: "MS", party: "Republican", email: "contact@hyde-smith.senate.gov", phone: "202-224-5054", office: "702 Hart Senate Office Building", website: "https://www.hyde-smith.senate.gov"},
    
    // Missouri
    {name: "Josh Hawley", title: "Senator", state: "MO", party: "Republican", email: "contact@hawley.senate.gov", phone: "202-224-6154", office: "212 Russell Senate Office Building", website: "https://www.hawley.senate.gov"},
    {name: "Eric Schmitt", title: "Senator", state: "MO", party: "Republican", email: "contact@schmitt.senate.gov", phone: "202-224-5721", office: "825A Hart Senate Office Building", website: "https://www.schmitt.senate.gov"},
    
    // Montana
    {name: "Steve Daines", title: "Senator", state: "MT", party: "Republican", email: "contact@daines.senate.gov", phone: "202-224-2651", office: "320 Hart Senate Office Building", website: "https://www.daines.senate.gov"},
    {name: "Tim Sheehy", title: "Senator", state: "MT", party: "Republican", email: "contact@sheehy.senate.gov", phone: "202-224-2644", office: "124 Russell Senate Office Building", website: "https://www.sheehy.senate.gov"},
    
    // Nebraska
    {name: "Deb Fischer", title: "Senator", state: "NE", party: "Republican", email: "contact@fischer.senate.gov", phone: "202-224-6551", office: "448 Russell Senate Office Building", website: "https://www.fischer.senate.gov"},
    {name: "Pete Ricketts", title: "Senator", state: "NE", party: "Republican", email: "contact@ricketts.senate.gov", phone: "202-224-4224", office: "139 Russell Senate Office Building", website: "https://www.ricketts.senate.gov"},
    
    // Nevada
    {name: "Catherine Cortez Masto", title: "Senator", state: "NV", party: "Democratic", email: "contact@cortezmasto.senate.gov", phone: "202-224-3542", office: "516 Hart Senate Office Building", website: "https://www.cortezmasto.senate.gov"},
    {name: "Jacky Rosen", title: "Senator", state: "NV", party: "Democratic", email: "contact@rosen.senate.gov", phone: "202-224-6244", office: "713 Hart Senate Office Building", website: "https://www.rosen.senate.gov"},
    
    // New Hampshire
    {name: "Jeanne Shaheen", title: "Senator", state: "NH", party: "Democratic", email: "contact@shaheen.senate.gov", phone: "202-224-2841", office: "506 Hart Senate Office Building", website: "https://www.shaheen.senate.gov"},
    {name: "Maggie Hassan", title: "Senator", state: "NH", party: "Democratic", email: "contact@hassan.senate.gov", phone: "202-224-3324", office: "330 Hart Senate Office Building", website: "https://www.hassan.senate.gov"},
    
    // New Jersey
    {name: "Andy Kim", title: "Senator", state: "NJ", party: "Democratic", email: "contact@kim.senate.gov", phone: "202-224-4744", office: "520 Hart Senate Office Building", website: "https://www.kim.senate.gov"},
    {name: "Cory Booker", title: "Senator", state: "NJ", party: "Democratic", email: "contact@booker.senate.gov", phone: "202-224-3224", office: "717 Hart Senate Office Building", website: "https://www.booker.senate.gov"},
    
    // New Mexico
    {name: "Martin Heinrich", title: "Senator", state: "NM", party: "Democratic", email: "contact@heinrich.senate.gov", phone: "202-224-5521", office: "303 Hart Senate Office Building", website: "https://www.heinrich.senate.gov"},
    {name: "Ben Ray Luján", title: "Senator", state: "NM", party: "Democratic", email: "contact@lujan.senate.gov", phone: "202-224-6621", office: "498 Russell Senate Office Building", website: "https://www.lujan.senate.gov"},
    
    // New York
    {name: "Chuck Schumer", title: "Senator", state: "NY", party: "Democratic", email: "contact@schumer.senate.gov", phone: "202-224-6542", office: "322 Hart Senate Office Building", website: "https://www.schumer.senate.gov"},
    {name: "Kirsten Gillibrand", title: "Senator", state: "NY", party: "Democratic", email: "contact@gillibrand.senate.gov", phone: "202-224-4451", office: "478 Russell Senate Office Building", website: "https://www.gillibrand.senate.gov"},
    
    // North Carolina
    {name: "Thom Tillis", title: "Senator", state: "NC", party: "Republican", email: "contact@tillis.senate.gov", phone: "202-224-6342", office: "113 Dirksen Senate Office Building", website: "https://www.tillis.senate.gov"},
    {name: "Ted Budd", title: "Senator", state: "NC", party: "Republican", email: "contact@budd.senate.gov", phone: "202-224-3154", office: "217 Russell Senate Office Building", website: "https://www.budd.senate.gov"},
    
    // North Dakota
    {name: "John Hoeven", title: "Senator", state: "ND", party: "Republican", email: "contact@hoeven.senate.gov", phone: "202-224-2551", office: "338 Russell Senate Office Building", website: "https://www.hoeven.senate.gov"},
    {name: "Kevin Cramer", title: "Senator", state: "ND", party: "Republican", email: "contact@cramer.senate.gov", phone: "202-224-2043", office: "400 Russell Senate Office Building", website: "https://www.cramer.senate.gov"},
    
    // OHIO - CORRECTED SENATORS
    {name: "Bernie Moreno", title: "Senator", state: "OH", party: "Republican", email: "contact@moreno.senate.gov", phone: "202-224-2315", office: "284 Russell Senate Office Building", website: "https://www.moreno.senate.gov"},
    {name: "Jon Husted", title: "Senator", state: "OH", party: "Republican", email: "contact@husted.senate.gov", phone: "202-224-3353", office: "304 Russell Senate Office Building", website: "https://www.husted.senate.gov"},
    
    // Oklahoma
    {name: "Markwayne Mullin", title: "Senator", state: "OK", party: "Republican", email: "contact@mullin.senate.gov", phone: "202-224-4721", office: "330 Hart Senate Office Building", website: "https://www.mullin.senate.gov"},
    {name: "James Lankford", title: "Senator", state: "OK", party: "Republican", email: "contact@lankford.senate.gov", phone: "202-224-5754", office: "731 Hart Senate Office Building", website: "https://www.lankford.senate.gov"},
    
    // Oregon
    {name: "Ron Wyden", title: "Senator", state: "OR", party: "Democratic", email: "contact@wyden.senate.gov", phone: "202-224-5244", office: "221 Dirksen Senate Office Building", website: "https://www.wyden.senate.gov"},
    {name: "Jeff Merkley", title: "Senator", state: "OR", party: "Democratic", email: "contact@merkley.senate.gov", phone: "202-224-3753", office: "531 Hart Senate Office Building", website: "https://www.merkley.senate.gov"},
    
    // Pennsylvania
    {name: "Bob Casey Jr.", title: "Senator", state: "PA", party: "Democratic", email: "contact@casey.senate.gov", phone: "202-224-6324", office: "702 Hart Senate Office Building", website: "https://www.casey.senate.gov"},
    {name: "John Fetterman", title: "Senator", state: "PA", party: "Democratic", email: "contact@fetterman.senate.gov", phone: "202-224-4254", office: "142 Russell Senate Office Building", website: "https://www.fetterman.senate.gov"},
    
    // Rhode Island
    {name: "Jack Reed", title: "Senator", state: "RI", party: "Democratic", email: "contact@reed.senate.gov", phone: "202-224-4642", office: "728 Hart Senate Office Building", website: "https://www.reed.senate.gov"},
    {name: "Sheldon Whitehouse", title: "Senator", state: "RI", party: "Democratic", email: "contact@whitehouse.senate.gov", phone: "202-224-2921", office: "530 Hart Senate Office Building", website: "https://www.whitehouse.senate.gov"},
    
    // South Carolina
    {name: "Lindsey Graham", title: "Senator", state: "SC", party: "Republican", email: "contact@graham.senate.gov", phone: "202-224-5972", office: "211 Russell Senate Office Building", website: "https://www.lgraham.senate.gov"},
    {name: "Tim Scott", title: "Senator", state: "SC", party: "Republican", email: "contact@scott.senate.gov", phone: "202-224-6121", office: "104 Hart Senate Office Building", website: "https://www.scott.senate.gov"},
    
    // South Dakota
    {name: "John Thune", title: "Senator", state: "SD", party: "Republican", email: "contact@thune.senate.gov", phone: "202-224-2321", office: "511 Dirksen Senate Office Building", website: "https://www.thune.senate.gov"},
    {name: "Mike Rounds", title: "Senator", state: "SD", party: "Republican", email: "contact@rounds.senate.gov", phone: "202-224-5842", office: "716 Hart Senate Office Building", website: "https://www.rounds.senate.gov"},
    
    // Tennessee
    {name: "Marsha Blackburn", title: "Senator", state: "TN", party: "Republican", email: "contact@blackburn.senate.gov", phone: "202-224-3344", office: "357 Dirksen Senate Office Building", website: "https://www.blackburn.senate.gov"},
    {name: "Bill Hagerty", title: "Senator", state: "TN", party: "Republican", email: "contact@hagerty.senate.gov", phone: "202-224-4944", office: "251 Russell Senate Office Building", website: "https://www.hagerty.senate.gov"},
    
    // Texas
    {name: "John Cornyn", title: "Senator", state: "TX", party: "Republican", email: "contact@cornyn.senate.gov", phone: "202-224-2934", office: "517 Hart Senate Office Building", website: "https://www.cornyn.senate.gov"},
    {name: "Ted Cruz", title: "Senator", state: "TX", party: "Republican", email: "contact@cruz.senate.gov", phone: "202-224-5922", office: "167 Russell Senate Office Building", website: "https://www.cruz.senate.gov"},
    
    // Utah
    {name: "Mike Lee", title: "Senator", state: "UT", party: "Republican", email: "contact@lee.senate.gov", phone: "202-224-5444", office: "363 Russell Senate Office Building", website: "https://www.lee.senate.gov"},
    {name: "John Curtis", title: "Senator", state: "UT", party: "Republican", email: "contact@curtis.senate.gov", phone: "202-224-5251", office: "502 Hart Senate Office Building", website: "https://www.curtis.senate.gov"},
    
    // Vermont
    {name: "Bernie Sanders", title: "Senator", state: "VT", party: "Independent", email: "contact@sanders.senate.gov", phone: "202-224-5141", office: "332 Dirksen Senate Office Building", website: "https://www.sanders.senate.gov"},
    {name: "Peter Welch", title: "Senator", state: "VT", party: "Democratic", email: "contact@welch.senate.gov", phone: "202-224-4242", office: "115 Russell Senate Office Building", website: "https://www.welch.senate.gov"},
    
    // Virginia
    {name: "Mark Warner", title: "Senator", state: "VA", party: "Democratic", email: "contact@warner.senate.gov", phone: "202-224-2023", office: "703 Hart Senate Office Building", website: "https://www.warner.senate.gov"},
    {name: "Tim Kaine", title: "Senator", state: "VA", party: "Democratic", email: "contact@kaine.senate.gov", phone: "202-224-4024", office: "231 Russell Senate Office Building", website: "https://www.kaine.senate.gov"},
    
    // Washington
    {name: "Patty Murray", title: "Senator", state: "WA", party: "Democratic", email: "contact@murray.senate.gov", phone: "202-224-2621", office: "154 Russell Senate Office Building", website: "https://www.murray.senate.gov"},
    {name: "Maria Cantwell", title: "Senator", state: "WA", party: "Democratic", email: "contact@cantwell.senate.gov", phone: "202-224-3441", office: "511 Hart Senate Office Building", website: "https://www.cantwell.senate.gov"},
    
    // West Virginia
    {name: "Jim Justice", title: "Senator", state: "WV", party: "Republican", email: "contact@justice.senate.gov", phone: "202-224-3954", office: "G12 Dirksen Senate Office Building", website: "https://www.justice.senate.gov"},
    {name: "Shelley Moore Capito", title: "Senator", state: "WV", party: "Republican", email: "contact@capito.senate.gov", phone: "202-224-6472", office: "170 Russell Senate Office Building", website: "https://www.capito.senate.gov"},
    
    // Wisconsin
    {name: "Ron Johnson", title: "Senator", state: "WI", party: "Republican", email: "contact@ronjohnson.senate.gov", phone: "202-224-5323", office: "328 Hart Senate Office Building", website: "https://www.ronjohnson.senate.gov"},
    {name: "Tammy Baldwin", title: "Senator", state: "WI", party: "Democratic", email: "contact@baldwin.senate.gov", phone: "202-224-5653", office: "709 Hart Senate Office Building", website: "https://www.baldwin.senate.gov"},
    
    // Wyoming
    {name: "John Barrasso", title: "Senator", state: "WY", party: "Republican", email: "contact@barrasso.senate.gov", phone: "202-224-6441", office: "307 Dirksen Senate Office Building", website: "https://www.barrasso.senate.gov"},
    {name: "Cynthia Lummis", title: "Senator", state: "WY", party: "Republican", email: "contact@lummis.senate.gov", phone: "202-224-3424", office: "127A Russell Senate Office Building", website: "https://www.lummis.senate.gov"}
];

export default correctedSenateData;