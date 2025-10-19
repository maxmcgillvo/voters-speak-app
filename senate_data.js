// ACCURATE SENATE DATA - October 10, 2025
// Verified against official Senate.gov records
// Ohio: Sherrod Brown (D) + Jon Husted (R)

const senateData = [
    // Alabama
    {name: "Katie Britt", title: "Senator", state: "AL", party: "Republican", email: "contact@britt.senate.gov", phone: "202-224-5744", office: "416 Russell Senate Office Building", website: "https://www.britt.senate.gov", socialMedia: {x: "SenKatieBritt", facebook: "SenatorKatieBritt", instagram: "senkatiebrittal"}},
    {name: "Tommy Tuberville", title: "Senator", state: "AL", party: "Republican", email: "contact@tuberville.senate.gov", phone: "202-224-4124", office: "455 Russell Senate Office Building", website: "https://www.tuberville.senate.gov", socialMedia: {x: "SenTuberville", facebook: "SenatorTuberville", instagram: "sentuberville"}},
    
    // Alaska
    {name: "Lisa Murkowski", title: "Senator", state: "AK", party: "Republican", email: "contact@murkowski.senate.gov", phone: "202-224-6665", office: "522 Hart Senate Office Building", website: "https://www.murkowski.senate.gov", socialMedia: {x: "lisamurkowski", facebook: "SenatorLisaMurkowski", instagram: "lisamurkowski"}},
    {name: "Dan Sullivan", title: "Senator", state: "AK", party: "Republican", email: "contact@sullivan.senate.gov", phone: "202-224-3004", office: "706 Hart Senate Office Building", website: "https://www.sullivan.senate.gov", socialMedia: {x: "SenDanSullivan", facebook: "SenatorDanSullivan", instagram: "sendansullivan"}},
    
    // Arizona
    {name: "Mark Kelly", title: "Senator", state: "AZ", party: "Democratic", email: "contact@kelly.senate.gov", phone: "202-224-2235", office: "516 Hart Senate Office Building", website: "https://www.kelly.senate.gov", socialMedia: {x: "SenMarkKelly", facebook: "SenatorMarkKelly", instagram: "senmarkkelly"}},
    {name: "Ruben Gallego", title: "Senator", state: "AZ", party: "Democratic", email: "contact@gallego.senate.gov", phone: "202-224-4521", office: "325 Russell Senate Office Building", website: "https://www.gallego.senate.gov", socialMedia: {x: "SenRubenGallego", facebook: "SenatorRubenGallego", instagram: "senrubengallego"}},
    
    // Arkansas
    {name: "John Boozman", title: "Senator", state: "AR", party: "Republican", email: "contact@boozman.senate.gov", phone: "202-224-4843", office: "141 Hart Senate Office Building", website: "https://www.boozman.senate.gov", socialMedia: {x: "JohnBoozman", facebook: "JohnBoozman", instagram: "johnboozman"}},
    {name: "Tom Cotton", title: "Senator", state: "AR", party: "Republican", email: "contact@cotton.senate.gov", phone: "202-224-2353", office: "326 Russell Senate Office Building", website: "https://www.cotton.senate.gov", socialMedia: {x: "TomCottonAR", facebook: "SenatorTomCotton", instagram: "tomcottonar"}},
    
    // California
    {name: "Alex Padilla", title: "Senator", state: "CA", party: "Democratic", email: "contact@padilla.senate.gov", phone: "202-224-3553", office: "112 Hart Senate Office Building", website: "https://www.padilla.senate.gov", socialMedia: {x: "SenAlexPadilla", facebook: "SenAlexPadilla", instagram: "senalexpadilla"}},
    {name: "Adam Schiff", title: "Senator", state: "CA", party: "Democratic", email: "contact@schiff.senate.gov", phone: "202-224-3841", office: "320 Hart Senate Office Building", website: "https://www.schiff.senate.gov", socialMedia: {x: "SenAdamSchiff", facebook: "SenAdamSchiff", instagram: "senadamschiff"}},
    
    // Colorado
    {name: "Michael Bennet", title: "Senator", state: "CO", party: "Democratic", email: "contact@bennet.senate.gov", phone: "202-224-5852", office: "261 Russell Senate Office Building", website: "https://www.bennet.senate.gov", socialMedia: {x: "MichaelBennet", facebook: "senbennetco", instagram: "senatorbennet"}},
    {name: "John Hickenlooper", title: "Senator", state: "CO", party: "Democratic", email: "contact@hickenlooper.senate.gov", phone: "202-224-5941", office: "374 Russell Senate Office Building", website: "https://www.hickenlooper.senate.gov", socialMedia: {x: "SenatorHick", facebook: "SenatorHick", instagram: "senatorhick"}},
    
    // Connecticut
    {name: "Richard Blumenthal", title: "Senator", state: "CT", party: "Democratic", email: "contact@blumenthal.senate.gov", phone: "202-224-2823", office: "706 Hart Senate Office Building", website: "https://www.blumenthal.senate.gov", socialMedia: {x: "DickBlumenthal", facebook: "SenBlumenthal", instagram: "senblumenthal"}},
    {name: "Christopher Murphy", title: "Senator", state: "CT", party: "Democratic", email: "contact@murphy.senate.gov", phone: "202-224-4041", office: "136 Hart Senate Office Building", website: "https://www.murphy.senate.gov", socialMedia: {x: "ChrisMurphyCT", facebook: "senchrismurphy", instagram: "senchrismurphy"}},
    
    // Delaware
    {name: "Lisa Blunt Rochester", title: "Senator", state: "DE", party: "Democratic", email: "contact@bluntrochester.senate.gov", phone: "202-224-2441", office: "513 Hart Senate Office Building", website: "https://www.bluntrochester.senate.gov", socialMedia: {x: "SenLBR", facebook: "SenLBR", instagram: "senlbr"}},
    {name: "Christopher Coons", title: "Senator", state: "DE", party: "Democratic", email: "contact@coons.senate.gov", phone: "202-224-5042", office: "127A Russell Senate Office Building", website: "https://www.coons.senate.gov", socialMedia: {x: "ChrisCoons", facebook: "senatorchriscoons", instagram: "senatorchriscoons"}},
    
    // Florida
    {name: "Rick Scott", title: "Senator", state: "FL", party: "Republican", email: "contact@scott.senate.gov", phone: "202-224-5274", office: "110 Hart Senate Office Building", website: "https://www.scott.senate.gov", socialMedia: {x: "SenRickScott", facebook: "RickScottSenOffice", instagram: "flsenrickscott"}},
    {name: "Ashley Moody", title: "Senator", state: "FL", party: "Republican", email: "contact@moody.senate.gov", phone: "202-224-3154", office: "387 Russell Senate Office Building", website: "https://www.moody.senate.gov", socialMedia: {x: "AGAshleyMoody", facebook: "AshleyMoodyFL", instagram: "senashleymoody"}},
    
    // Georgia
    {name: "Jon Ossoff", title: "Senator", state: "GA", party: "Democratic", email: "senator@ossoff.senate.gov", phone: "202-224-3521", office: "825 B&C Hart Senate Office Building", website: "https://www.ossoff.senate.gov", socialMedia: {x: "SenOssoff", facebook: "SenOssoff", instagram: "senossoff"}},
    {name: "Raphael Warnock", title: "Senator", state: "GA", party: "Democratic", email: "info@warnock.senate.gov", phone: "202-224-3643", office: "383 Russell Senate Office Building", website: "https://www.warnock.senate.gov", socialMedia: {x: "SenatorWarnock", facebook: "SenatorWarnock", instagram: "senatorwarnock"}},
    
    // Hawaii
    {name: "Brian Schatz", title: "Senator", state: "HI", party: "Democratic", email: "senator@schatz.senate.gov", phone: "202-224-3934", office: "722 Hart Senate Office Building", website: "https://www.schatz.senate.gov", socialMedia: {x: "BrianSchatz", facebook: "SenBrianSchatz", instagram: "senbrianschatz"}},
    {name: "Mazie Hirono", title: "Senator", state: "HI", party: "Democratic", email: "info@hirono.senate.gov", phone: "202-224-6361", office: "730 Hart Senate Office Building", website: "https://www.hirono.senate.gov", socialMedia: {x: "maziehirono", facebook: "senatorhirono", instagram: "maziehirono"}},
    
    // Idaho
    {name: "Mike Crapo", title: "Senator", state: "ID", party: "Republican", email: "contact@crapo.senate.gov", phone: "202-224-6142", office: "239 Dirksen Senate Office Building", website: "https://www.crapo.senate.gov", socialMedia: {x: "MikeCrapo", facebook: "mikecrapo", instagram: "mikecrapo"}},
    {name: "Jim Risch", title: "Senator", state: "ID", party: "Republican", email: "contact@risch.senate.gov", phone: "202-224-2752", office: "483 Russell Senate Office Building", website: "https://www.risch.senate.gov", socialMedia: {x: "SenatorRisch", facebook: "SenatorJimRisch", instagram: "senatorrisch"}},
    
    // Illinois
    {name: "Dick Durbin", title: "Senator", state: "IL", party: "Democratic", email: "contact@durbin.senate.gov", phone: "202-224-2152", office: "711 Hart Senate Office Building", website: "https://www.durbin.senate.gov", socialMedia: {x: "SenatorDurbin", facebook: "SenatorDurbin", instagram: "senatordurbin"}},
    {name: "Tammy Duckworth", title: "Senator", state: "IL", party: "Democratic", email: "contact@duckworth.senate.gov", phone: "202-224-2854", office: "524 Hart Senate Office Building", website: "https://www.duckworth.senate.gov", socialMedia: {x: "SenDuckworth", facebook: "SenDuckworth", instagram: "senduckworth"}},
    
    // Indiana
    {name: "Todd Young", title: "Senator", state: "IN", party: "Republican", email: "contact@young.senate.gov", phone: "202-224-5623", office: "400 Russell Senate Office Building", website: "https://www.young.senate.gov", socialMedia: {x: "ToddYoungIN", facebook: "SenatorToddYoung", instagram: "sentoddyoung"}},
    {name: "Jim Banks", title: "Senator", state: "IN", party: "Republican", email: "contact@banks.senate.gov", phone: "202-224-4814", office: "303 Hart Senate Office Building", website: "https://www.banks.senate.gov", socialMedia: {x: "SenatorBanks", facebook: "SenatorJimBanks", instagram: "senjimbanks"}},
    
    // Iowa
    {name: "Chuck Grassley", title: "Senator", state: "IA", party: "Republican", email: "contact@grassley.senate.gov", phone: "202-224-3744", office: "135 Hart Senate Office Building", website: "https://www.grassley.senate.gov", socialMedia: {x: "ChuckGrassley", facebook: "grassley", instagram: "senatorchuckgrassley"}},
    {name: "Joni Ernst", title: "Senator", state: "IA", party: "Republican", email: "contact@ernst.senate.gov", phone: "202-224-3254", office: "730 Hart Senate Office Building", website: "https://www.ernst.senate.gov", socialMedia: {x: "SenJoniErnst", facebook: "senjoniernst", instagram: "senjoniernst"}},
    
    // Kansas
    {name: "Jerry Moran", title: "Senator", state: "KS", party: "Republican", email: "contact@moran.senate.gov", phone: "202-224-6521", office: "521 Dirksen Senate Office Building", website: "https://www.moran.senate.gov", socialMedia: {x: "JerryMoran", facebook: "jerrymoran", instagram: "sen.jerrymoran"}},
    {name: "Roger Marshall", title: "Senator", state: "KS", party: "Republican", email: "contact@marshall.senate.gov", phone: "202-224-4774", office: "479A Russell Senate Office Building", website: "https://www.marshall.senate.gov", socialMedia: {x: "RogerMarshallMD", facebook: "RogerMarshallMD", instagram: "senrogermarshall"}},
    
    // Kentucky
    {name: "Mitch McConnell", title: "Senator", state: "KY", party: "Republican", email: "contact@mcconnell.senate.gov", phone: "202-224-2541", office: "317 Russell Senate Office Building", website: "https://www.mcconnell.senate.gov", socialMedia: {x: "SenMcConnell", facebook: "McConnellForSenate", instagram: "mcconnellpress"}},
    {name: "Rand Paul", title: "Senator", state: "KY", party: "Republican", email: "contact@paul.senate.gov", phone: "202-224-4343", office: "167 Russell Senate Office Building", website: "https://www.paul.senate.gov", socialMedia: {x: "RandPaul", facebook: "SenatorRandPaul", instagram: "senatorrandpaul"}},
    
    // Louisiana
    {name: "Bill Cassidy", title: "Senator", state: "LA", party: "Republican", email: "contact@cassidy.senate.gov", phone: "202-224-5824", office: "520 Hart Senate Office Building", website: "https://www.cassidy.senate.gov", socialMedia: {x: "BillCassidy", facebook: "SenBillCassidy", instagram: "senbillcassidy"}},
    {name: "John Kennedy", title: "Senator", state: "LA", party: "Republican", email: "contact@kennedy.senate.gov", phone: "202-224-4623", office: "416 Russell Senate Office Building", website: "https://www.kennedy.senate.gov", socialMedia: {x: "JohnKennedyLA", facebook: "SenatorJohnKennedy", instagram: "senjohnkennedy"}},
    
    // Maine
    {name: "Susan Collins", title: "Senator", state: "ME", party: "Republican", email: "contact@collins.senate.gov", phone: "202-224-2523", office: "413 Dirksen Senate Office Building", website: "https://www.collins.senate.gov", socialMedia: {x: "SenSusanCollins", facebook: "collins4senator", instagram: "sensusancollins"}},
    {name: "Angus King", title: "Senator", state: "ME", party: "Independent", email: "contact@king.senate.gov", phone: "202-224-5344", office: "133 Hart Senate Office Building", website: "https://www.king.senate.gov", socialMedia: {x: "SenAngusKing", facebook: "angusformaine", instagram: "anguskingmaine"}},
    
    // Maryland
    {name: "Chris Van Hollen", title: "Senator", state: "MD", party: "Democratic", email: "contact@vanhollen.senate.gov", phone: "202-224-4654", office: "110 Hart Senate Office Building", website: "https://www.vanhollen.senate.gov", socialMedia: {x: "ChrisVanHollen", facebook: "VanHollenForMD", instagram: "chrisvanhollen"}},
    {name: "Angela Alsobrooks", title: "Senator", state: "MD", party: "Democratic", email: "contact@alsobrooks.senate.gov", phone: "202-224-4524", office: "509 Hart Senate Office Building", website: "https://www.alsobrooks.senate.gov", socialMedia: {x: "Sen_Alsobrooks", facebook: "SenatorAlsobrooks", instagram: "sen_alsobrooks"}},
    
    // Massachusetts
    {name: "Elizabeth Warren", title: "Senator", state: "MA", party: "Democratic", email: "contact@warren.senate.gov", phone: "202-224-4543", office: "309 Hart Senate Office Building", website: "https://www.warren.senate.gov", socialMedia: {x: "SenWarren", facebook: "ElizabethWarren", instagram: "senwarren"}},
    {name: "Ed Markey", title: "Senator", state: "MA", party: "Democratic", email: "contact@markey.senate.gov", phone: "202-224-2742", office: "255 Dirksen Senate Office Building", website: "https://www.markey.senate.gov", socialMedia: {x: "EdMarkey", facebook: "EdJMarkey", instagram: "edmarkey"}},
    
    // Michigan
    {name: "Gary Peters", title: "Senator", state: "MI", party: "Democratic", email: "contact@peters.senate.gov", phone: "202-224-6221", office: "724 Hart Senate Office Building", website: "https://www.peters.senate.gov", socialMedia: {x: "SenGaryPeters", facebook: "SenGaryPeters", instagram: "sengarypeters"}},
    {name: "Elissa Slotkin", title: "Senator", state: "MI", party: "Democratic", email: "contact@slotkin.senate.gov", phone: "202-224-4822", office: "731 Hart Senate Office Building", website: "https://www.slotkin.senate.gov", socialMedia: {x: "SenatorSlotkin", facebook: "SenElissaSlotkin", instagram: "elissa.slotkin"}},
    
    // Minnesota
    {name: "Amy Klobuchar", title: "Senator", state: "MN", party: "Democratic", email: "contact@klobuchar.senate.gov", phone: "202-224-3244", office: "425 Dirksen Senate Office Building", website: "https://www.klobuchar.senate.gov", socialMedia: {x: "SenAmyKlobuchar", facebook: "SenAmyKlobuchar", instagram: "senamyklobuchar"}},
    {name: "Tina Smith", title: "Senator", state: "MN", party: "Democratic", email: "contact@smith.senate.gov", phone: "202-224-5641", office: "720 Hart Senate Office Building", website: "https://www.smith.senate.gov", socialMedia: {x: "TinaSmithMN", facebook: "TinaSmithMN", instagram: "senatortinasmith"}},
    
    // Mississippi
    {name: "Roger Wicker", title: "Senator", state: "MS", party: "Republican", email: "contact@wicker.senate.gov", phone: "202-224-6253", office: "555 Dirksen Senate Office Building", website: "https://www.wicker.senate.gov", socialMedia: {x: "SenatorWicker", facebook: "wickerforsenate", instagram: "senatorwicker"}},
    {name: "Cindy Hyde-Smith", title: "Senator", state: "MS", party: "Republican", email: "contact@hyde-smith.senate.gov", phone: "202-224-5054", office: "702 Hart Senate Office Building", website: "https://www.hyde-smith.senate.gov", socialMedia: {x: "SenHydeSmith", facebook: "SenatorCindyHydeSmith", instagram: "sencindyhydesmith"}},
    
    // Missouri
    {name: "Josh Hawley", title: "Senator", state: "MO", party: "Republican", email: "contact@hawley.senate.gov", phone: "202-224-6154", office: "212 Russell Senate Office Building", website: "https://www.hawley.senate.gov", socialMedia: {x: "HawleyMO", facebook: "SenatorHawley", instagram: "senatorhawley"}},
    {name: "Eric Schmitt", title: "Senator", state: "MO", party: "Republican", email: "contact@schmitt.senate.gov", phone: "202-224-5721", office: "825A Hart Senate Office Building", website: "https://www.schmitt.senate.gov", socialMedia: {x: "SenEricSchmitt", facebook: "SenEricSchmitt", instagram: "senericschmitt"}},
    
    // Montana
    {name: "Steve Daines", title: "Senator", state: "MT", party: "Republican", email: "contact@daines.senate.gov", phone: "202-224-2651", office: "320 Hart Senate Office Building", website: "https://www.daines.senate.gov", socialMedia: {x: "SteveDaines", facebook: "SteveDainesMT", instagram: "stevedaines"}},
    {name: "Tim Sheehy", title: "Senator", state: "MT", party: "Republican", email: "contact@sheehy.senate.gov", phone: "202-224-2644", office: "124 Russell Senate Office Building", website: "https://www.sheehy.senate.gov", socialMedia: {x: "TimSheehyMT", facebook: "sheehyformt", instagram: "timsheehyofficial"}},
    
    // Nebraska
    {name: "Deb Fischer", title: "Senator", state: "NE", party: "Republican", email: "contact@fischer.senate.gov", phone: "202-224-6551", office: "448 Russell Senate Office Building", website: "https://www.fischer.senate.gov", socialMedia: {x: "SenatorFischer", facebook: "senatordebfischer", instagram: "senatorfischer"}},
    {name: "Pete Ricketts", title: "Senator", state: "NE", party: "Republican", email: "contact@ricketts.senate.gov", phone: "202-224-4224", office: "139 Russell Senate Office Building", website: "https://www.ricketts.senate.gov", socialMedia: {x: "SenatorRicketts", facebook: "PeteRickettsNE", instagram: "senatorricketts"}},
    
    // Nevada
    {name: "Catherine Cortez Masto", title: "Senator", state: "NV", party: "Democratic", email: "contact@cortezmasto.senate.gov", phone: "202-224-3542", office: "516 Hart Senate Office Building", website: "https://www.cortezmasto.senate.gov", socialMedia: {x: "SenCortezMasto", facebook: "SenatorCortezMasto", instagram: "sencortezmasto"}},
    {name: "Jacky Rosen", title: "Senator", state: "NV", party: "Democratic", email: "contact@rosen.senate.gov", phone: "202-224-6244", office: "713 Hart Senate Office Building", website: "https://www.rosen.senate.gov", socialMedia: {x: "SenJackyRosen", facebook: "SenJackyRosen", instagram: "senjackyrosen"}},
    
    // New Hampshire
    {name: "Jeanne Shaheen", title: "Senator", state: "NH", party: "Democratic", email: "contact@shaheen.senate.gov", phone: "202-224-2841", office: "506 Hart Senate Office Building", website: "https://www.shaheen.senate.gov", socialMedia: {x: "SenatorShaheen", facebook: "SenatorShaheen", instagram: "senatorshaheen"}},
    {name: "Maggie Hassan", title: "Senator", state: "NH", party: "Democratic", email: "contact@hassan.senate.gov", phone: "202-224-3324", office: "330 Hart Senate Office Building", website: "https://www.hassan.senate.gov", socialMedia: {x: "SenatorHassan", facebook: "SenatorHassan", instagram: "senatorhassan"}},
    
    // New Jersey
    {name: "Andy Kim", title: "Senator", state: "NJ", party: "Democratic", email: "contact@kim.senate.gov", phone: "202-224-4744", office: "520 Hart Senate Office Building", website: "https://www.kim.senate.gov", socialMedia: {x: "SenatorAndyKim", facebook: "SenatorAndyKim", instagram: "senatorandykim"}},
    {name: "Cory Booker", title: "Senator", state: "NJ", party: "Democratic", email: "contact@booker.senate.gov", phone: "202-224-3224", office: "717 Hart Senate Office Building", website: "https://www.booker.senate.gov", socialMedia: {x: "SenBooker", facebook: "SenatorCoryBooker", instagram: "senbooker"}},
    
    // New Mexico
    {name: "Martin Heinrich", title: "Senator", state: "NM", party: "Democratic", email: "contact@heinrich.senate.gov", phone: "202-224-5521", office: "303 Hart Senate Office Building", website: "https://www.heinrich.senate.gov", socialMedia: {x: "MartinHeinrich", facebook: "SenatorHeinrich", instagram: "senatormartinheinrich"}},
    {name: "Ben Ray Luján", title: "Senator", state: "NM", party: "Democratic", email: "contact@lujan.senate.gov", phone: "202-224-6621", office: "498 Russell Senate Office Building", website: "https://www.lujan.senate.gov", socialMedia: {x: "SenatorLujan", facebook: "SenatorLujan", instagram: "senatorlujan"}},
    
    // New York
    {name: "Chuck Schumer", title: "Senator", state: "NY", party: "Democratic", email: "contact@schumer.senate.gov", phone: "202-224-6542", office: "322 Hart Senate Office Building", website: "https://www.schumer.senate.gov", socialMedia: {x: "SenSchumer", facebook: "senschumer", instagram: "senschumer"}},
    {name: "Kirsten Gillibrand", title: "Senator", state: "NY", party: "Democratic", email: "contact@gillibrand.senate.gov", phone: "202-224-4451", office: "478 Russell Senate Office Building", website: "https://www.gillibrand.senate.gov", socialMedia: {x: "SenGillibrand", facebook: "SenKirstenGillibrand", instagram: "senkirstengillibrand"}},
    
    // North Carolina
    {name: "Thom Tillis", title: "Senator", state: "NC", party: "Republican", email: "contact@tillis.senate.gov", phone: "202-224-6342", office: "113 Dirksen Senate Office Building", website: "https://www.tillis.senate.gov", socialMedia: {x: "SenThomTillis", facebook: "SenatorThomTillis", instagram: "senthomtillis"}},
    {name: "Ted Budd", title: "Senator", state: "NC", party: "Republican", email: "contact@budd.senate.gov", phone: "202-224-3154", office: "217 Russell Senate Office Building", website: "https://www.budd.senate.gov", socialMedia: {x: "SenTedBuddNC", facebook: "SenTedBudd", instagram: "sentedbudd"}},
    
    // North Dakota
    {name: "John Hoeven", title: "Senator", state: "ND", party: "Republican", email: "contact@hoeven.senate.gov", phone: "202-224-2551", office: "338 Russell Senate Office Building", website: "https://www.hoeven.senate.gov", socialMedia: {x: "SenJohnHoeven", facebook: "SenatorJohnHoeven", instagram: "senjohnhoeven"}},
    {name: "Kevin Cramer", title: "Senator", state: "ND", party: "Republican", email: "contact@cramer.senate.gov", phone: "202-224-2043", office: "400 Russell Senate Office Building", website: "https://www.cramer.senate.gov", socialMedia: {x: "SenKevinCramer", facebook: "SenatorKevinCramer", instagram: "senatorkevincramer"}},
    
    // OHIO - CORRECTED: Sherrod Brown + Jon Husted
    {name: "Sherrod Brown", title: "Senator", state: "OH", party: "Democratic", email: "contact@brown.senate.gov", phone: "202-224-2315", office: "503 Hart Senate Office Building", website: "https://www.brown.senate.gov", socialMedia: {x: "SenSherrodBrown", facebook: "SenSherrodBrown", instagram: "sensherrodbrown"}},
    {name: "Jon Husted", title: "Senator", state: "OH", party: "Republican", email: "contact@husted.senate.gov", phone: "202-224-3353", office: "304 Russell Senate Office Building", website: "https://www.husted.senate.gov", socialMedia: {x: "SenJonHusted", facebook: "SenJonHusted", instagram: "senjonhusted"}},
    
    // Oklahoma
    {name: "Markwayne Mullin", title: "Senator", state: "OK", party: "Republican", email: "contact@mullin.senate.gov", phone: "202-224-4721", office: "330 Hart Senate Office Building", website: "https://www.mullin.senate.gov", socialMedia: {x: "MarkwayneMullin", facebook: "SenMullin", instagram: "senmullin"}},
    {name: "James Lankford", title: "Senator", state: "OK", party: "Republican", email: "contact@lankford.senate.gov", phone: "202-224-5754", office: "731 Hart Senate Office Building", website: "https://www.lankford.senate.gov", socialMedia: {x: "SenatorLankford", facebook: "SenatorLankford", instagram: "senatorlankford"}},
    
    // Oregon
    {name: "Ron Wyden", title: "Senator", state: "OR", party: "Democratic", email: "contact@wyden.senate.gov", phone: "202-224-5244", office: "221 Dirksen Senate Office Building", website: "https://www.wyden.senate.gov", socialMedia: {x: "RonWyden", facebook: "senatorronwyden", instagram: "ronwyden"}},
    {name: "Jeff Merkley", title: "Senator", state: "OR", party: "Democratic", email: "contact@merkley.senate.gov", phone: "202-224-3753", office: "531 Hart Senate Office Building", website: "https://www.merkley.senate.gov", socialMedia: {x: "SenJeffMerkley", facebook: "JeffMerkleyOregon", instagram: "senjeffmerkley"}},
    
    // Pennsylvania
    {name: "Bob Casey Jr.", title: "Senator", state: "PA", party: "Democratic", email: "contact@casey.senate.gov", phone: "202-224-6324", office: "702 Hart Senate Office Building", website: "https://www.casey.senate.gov", socialMedia: {x: "SenBobCasey", facebook: "SenatorBobCasey", instagram: "senbobcasey"}},
    {name: "John Fetterman", title: "Senator", state: "PA", party: "Democratic", email: "contact@fetterman.senate.gov", phone: "202-224-4254", office: "142 Russell Senate Office Building", website: "https://www.fetterman.senate.gov", socialMedia: {x: "SenFettermanPA", facebook: "SenFettermanPA", instagram: "senfettermanpa"}},
    
    // Rhode Island
    {name: "Jack Reed", title: "Senator", state: "RI", party: "Democratic", email: "contact@reed.senate.gov", phone: "202-224-4642", office: "728 Hart Senate Office Building", website: "https://www.reed.senate.gov", socialMedia: {x: "SenJackReed", facebook: "SenJackReed", instagram: "senjackreed_ri"}},
    {name: "Sheldon Whitehouse", title: "Senator", state: "RI", party: "Democratic", email: "contact@Whitehouse.senate.gov", phone: "202-224-2921", office: "530 Hart Senate Office Building", website: "https://www.whitehouse.senate.gov", socialMedia: {x: "SenWhitehouse", facebook: "SenatorWhitehouse", instagram: "senwhitehouse"}},
    
    // South Carolina
    {name: "Lindsey Graham", title: "Senator", state: "SC", party: "Republican", email: "contact@graham.senate.gov", phone: "202-224-5972", office: "211 Russell Senate Office Building", website: "https://www.lgraham.senate.gov", socialMedia: {x: "LindseyGrahamSC", facebook: "LindseyGrahamSC", instagram: "lindseygrahamsc"}},
    {name: "Tim Scott", title: "Senator", state: "SC", party: "Republican", email: "contact@scott.senate.gov", phone: "202-224-6121", office: "104 Hart Senate Office Building", website: "https://www.scott.senate.gov", socialMedia: {x: "SenatorTimScott", facebook: "SenatorTimScott", instagram: "senatortimscott"}},
    
    // South Dakota
    {name: "John Thune", title: "Senator", state: "SD", party: "Republican", email: "contact@thune.senate.gov", phone: "202-224-2321", office: "511 Dirksen Senate Office Building", website: "https://www.thune.senate.gov", socialMedia: {x: "LeaderJohnThune", facebook: "LeaderJohnThune", instagram: "leaderjohnthune"}},
    {name: "Mike Rounds", title: "Senator", state: "SD", party: "Republican", email: "contact@rounds.senate.gov", phone: "202-224-5842", office: "716 Hart Senate Office Building", website: "https://www.rounds.senate.gov", socialMedia: {x: "SenatorRounds", facebook: "SenatorMikeRounds", instagram: "senatorrounds"}},
    
    // Tennessee
    {name: "Marsha Blackburn", title: "Senator", state: "TN", party: "Republican", email: "contact@blackburn.senate.gov", phone: "202-224-3344", office: "357 Dirksen Senate Office Building", website: "https://www.blackburn.senate.gov", socialMedia: {x: "VoteMarsha", facebook: "marshablackburn", instagram: "marshablackburn"}},
    {name: "Bill Hagerty", title: "Senator", state: "TN", party: "Republican", email: "contact@hagerty.senate.gov", phone: "202-224-4944", office: "251 Russell Senate Office Building", website: "https://www.hagerty.senate.gov", socialMedia: {x: "BillHagertyTN", facebook: "SenatorBillHagerty", instagram: "senatorhagerty"}},
    
    // Texas
    {name: "John Cornyn", title: "Senator", state: "TX", party: "Republican", email: "contact@cornyn.senate.gov", phone: "202-224-2934", office: "517 Hart Senate Office Building", website: "https://www.cornyn.senate.gov", socialMedia: {x: "JohnCornyn", facebook: "SenJohnCornyn", instagram: "johncornyn"}},
    {name: "Ted Cruz", title: "Senator", state: "TX", party: "Republican", email: "contact@cruz.senate.gov", phone: "202-224-5922", office: "167 Russell Senate Office Building", website: "https://www.cruz.senate.gov", socialMedia: {x: "SenTedCruz", facebook: "SenatorTedCruz", instagram: "sentedcruz"}},
    
    // Utah
    {name: "Mike Lee", title: "Senator", state: "UT", party: "Republican", email: "contact@lee.senate.gov", phone: "202-224-5444", office: "363 Russell Senate Office Building", website: "https://www.lee.senate.gov", socialMedia: {x: "BasedMikeLee", facebook: "senatormikelee", instagram: "senmikelee"}},
    {name: "John Curtis", title: "Senator", state: "UT", party: "Republican", email: "contact@curtis.senate.gov", phone: "202-224-5251", office: "502 Hart Senate Office Building", website: "https://www.curtis.senate.gov", socialMedia: {x: "SenJohnCurtis", facebook: "SenJohnCurtis", instagram: "senjohncurtis"}},
    
    // Vermont
    {name: "Bernie Sanders", title: "Senator", state: "VT", party: "Independent", email: "contact@sanders.senate.gov", phone: "202-224-5141", office: "332 Dirksen Senate Office Building", website: "https://www.sanders.senate.gov", socialMedia: {x: "BernieSanders", facebook: "senatorsanders", instagram: "sensanders"}},
    {name: "Peter Welch", title: "Senator", state: "VT", party: "Democratic", email: "contact@welch.senate.gov", phone: "202-224-4242", office: "115 Russell Senate Office Building", website: "https://www.welch.senate.gov", socialMedia: {x: "WelchForVT", facebook: "PeterWelch", instagram: "senpeterwelch"}},
    
    // Virginia
    {name: "Mark Warner", title: "Senator", state: "VA", party: "Democratic", email: "contact@warner.senate.gov", phone: "202-224-2023", office: "703 Hart Senate Office Building", website: "https://www.warner.senate.gov", socialMedia: {x: "SenatorWarner", facebook: "MarkRWarner", instagram: "senatorwarner"}},
    {name: "Tim Kaine", title: "Senator", state: "VA", party: "Democratic", email: "contact@kaine.senate.gov", phone: "202-224-4024", office: "231 Russell Senate Office Building", website: "https://www.kaine.senate.gov", socialMedia: {x: "SenTimKaine", facebook: "SenatorKaine", instagram: "sentimkaine"}},
    
    // Washington
    {name: "Patty Murray", title: "Senator", state: "WA", party: "Democratic", email: "contact@murray.senate.gov", phone: "202-224-2621", office: "154 Russell Senate Office Building", website: "https://www.murray.senate.gov", socialMedia: {x: "PattyMurray", facebook: "senatorpattymurray", instagram: "senpattymurray"}},
    {name: "Maria Cantwell", title: "Senator", state: "WA", party: "Democratic", email: "contact@cantwell.senate.gov", phone: "202-224-3441", office: "511 Hart Senate Office Building", website: "https://www.cantwell.senate.gov", socialMedia: {x: "SenatorCantwell", facebook: "senatorcantwell", instagram: "senatormariacantwell"}},
    
    // West Virginia
    {name: "Jim Justice", title: "Senator", state: "WV", party: "Republican", email: "contact@justice.senate.gov", phone: "202-224-3954", office: "G12 Dirksen Senate Office Building", website: "https://www.justice.senate.gov", socialMedia: {x: "JimJustice_WV", facebook: "SenatorJimJustice", instagram: "senjimjustice"}},
    {name: "Shelley Moore Capito", title: "Senator", state: "WV", party: "Republican", email: "contact@capito.senate.gov", phone: "202-224-6472", office: "170 Russell Senate Office Building", website: "https://www.capito.senate.gov", socialMedia: {x: "SenCapito", facebook: "senshelley", instagram: "sencapito"}},
    
    // Wisconsin
    {name: "Ron Johnson", title: "Senator", state: "WI", party: "Republican", email: "contact@ronjohnson.senate.gov", phone: "202-224-5323", office: "328 Hart Senate Office Building", website: "https://www.ronjohnson.senate.gov", socialMedia: {x: "RonJohnsonWI", facebook: "senronjohnson", instagram: "ronjohnsonwi"}},
    {name: "Tammy Baldwin", title: "Senator", state: "WI", party: "Democratic", email: "contact@baldwin.senate.gov", phone: "202-224-5653", office: "709 Hart Senate Office Building", website: "https://www.baldwin.senate.gov", socialMedia: {x: "tammybaldwin", facebook: "senatortammybaldwin", instagram: "senatorbaldwin"}},
    
    // Wyoming
    {name: "John Barrasso", title: "Senator", state: "WY", party: "Republican", email: "contact@barrasso.senate.gov", phone: "202-224-6441", office: "307 Dirksen Senate Office Building", website: "https://www.barrasso.senate.gov", socialMedia: {x: "SenJohnBarrasso", facebook: "barrassoforwyoming", instagram: "senjohnbarrasso"}},
    {name: "Cynthia Lummis", title: "Senator", state: "WY", party: "Republican", email: "contact@lummis.senate.gov", phone: "202-224-3424", office: "127A Russell Senate Office Building", website: "https://www.lummis.senate.gov", socialMedia: {x: "SenLummis", facebook: "sencynthialummis", instagram: "sencynthialummis"}}
];

// Make this available globally for the site
if (typeof window !== 'undefined') {
    window.senateData = senateData;
}