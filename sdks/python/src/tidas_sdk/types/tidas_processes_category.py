"""
Processes classification categories.

Clean implementation using Literal types (matches TypeScript SDK pattern).
DO NOT auto-generate - regenerate using generate_category_types.py
"""

from typing import Literal, TypedDict


class ProcessesCategoryData(TypedDict):
    """Processes category metadata."""

    level: Literal['0', '1', '2', '3']
    classId: str
    text: str


# Type-safe union of all processes category IDs
Processes = Literal[
    'A',  # Agriculture, forestry and fishing
    '01',  # Crop and animal production, hunting and related service activities
    '011',  # Growing of non-perennial crops
    '0111',  # Growing of cereals (except rice), leguminous crops and oil seeds
    '0112',  # Growing of rice
    '0113',  # Growing of vegetables and melons, roots and tubers
    '0114',  # Growing of sugar cane
    '0115',  # Growing of tobacco
    '0116',  # Growing of fibre crops
    '0119',  # Growing of other non-perennial crops
    '012',  # Growing of perennial crops
    '0121',  # Growing of grapes
    '0122',  # Growing of tropical and subtropical fruits
    '0123',  # Growing of citrus fruits
    '0124',  # Growing of pome fruits and stone fruits
    '0125',  # Growing of other tree and bush fruits and nuts
    '0126',  # Growing of oleaginous fruits
    '0127',  # Growing of beverage crops
    '0128',  # Growing of spices, aromatic, drug and pharmaceutical crops
    '0129',  # Growing of other perennial crops
    '013',  # Plant propagation
    '0130',  # Plant propagation
    '014',  # Animal production
    '0141',  # Raising of cattle and buffaloes
    '0142',  # Raising of horses and other equines
    '0143',  # Raising of camels and camelids
    '0144',  # Raising of sheep and goats
    '0145',  # Raising of swine and pigs
    '0146',  # Raising of poultry
    '0149',  # Raising of other animals
    '015',  # Mixed farming
    '0150',  # Mixed farming
    '016',  # Support activities to agriculture and post-harvest crop activities
    '0161',  # Support activities for crop production
    '0162',  # Support activities for animal production
    '0163',  # Post-harvest crop activities
    '0164',  # Seed processing for propagation
    '017',  # Hunting, trapping and related service activities
    '0170',  # Hunting, trapping and related service activities
    '02',  # Forestry and logging
    '021',  # Silviculture and other forestry activities
    '0210',  # Silviculture and other forestry activities
    '022',  # Logging
    '0220',  # Logging
    '023',  # Gathering of non-wood forest products
    '0230',  # Gathering of non-wood forest products
    '024',  # Support services to forestry
    '0240',  # Support services to forestry
    '03',  # Fishing and aquaculture
    '031',  # Fishing
    '0311',  # Marine fishing
    '0312',  # Freshwater fishing
    '032',  # Aquaculture
    '0321',  # Marine aquaculture
    '0322',  # Freshwater aquaculture
    '033',  # Support activities for fishing and aquaculture
    '0330',  # Support activities for fishing and aquaculture
    'B',  # Mining and quarrying
    '05',  # Mining of coal and lignite
    '051',  # Mining of hard coal
    '0510',  # Mining of hard coal
    '052',  # Mining of lignite
    '0520',  # Mining of lignite
    '06',  # Extraction of crude petroleum and natural gas
    '061',  # Extraction of crude petroleum
    '0610',  # Extraction of crude petroleum
    '062',  # Extraction of natural gas
    '0620',  # Extraction of natural gas
    '07',  # Mining of metal ores
    '071',  # Mining of iron ores
    '0710',  # Mining of iron ores
    '072',  # Mining of non-ferrous metal ores
    '0721',  # Mining of uranium and thorium ores
    '0729',  # Mining of other non-ferrous metal ores
    '08',  # Other mining and quarrying
    '081',  # Quarrying of stone, sand and clay
    '0810',  # Quarrying of stone, sand and clay
    '089',  # Mining and quarrying n.e.c.
    '0891',  # Mining of chemical and fertilizer minerals
    '0892',  # Extraction of peat
    '0893',  # Extraction of salt
    '0899',  # Other mining and quarrying n.e.c.
    '09',  # Mining support service activities
    '091',  # Support activities for petroleum and natural gas extraction
    '0910',  # Support activities for petroleum and natural gas extraction
    '099',  # Support activities for other mining and quarrying
    '0990',  # Support activities for other mining and quarrying
    'C',  # Manufacturing
    '10',  # Manufacture of food products
    '101',  # Processing and preserving of meat
    '1010',  # Processing and preserving of meat
    '102',  # Processing and preserving of fish, crustaceans and molluscs
    '1020',  # Processing and preserving of fish, crustaceans and molluscs
    '103',  # Processing and preserving of fruit and vegetables
    '1030',  # Processing and preserving of fruit and vegetables
    '104',  # Manufacture of vegetable and animal oils and fats
    '1040',  # Manufacture of vegetable and animal oils and fats
    '105',  # Manufacture of dairy products
    '1050',  # Manufacture of dairy products
    '106',  # Manufacture of grain mill products, starches and starch products
    '1061',  # Manufacture of grain mill products
    '1062',  # Manufacture of starches and starch products
    '107',  # Manufacture of other food products
    '1071',  # Manufacture of bakery products
    '1072',  # Manufacture of sugar
    '1073',  # Manufacture of cocoa, chocolate and sugar confectionery
    '1074',  # Manufacture of macaroni, noodles, couscous and similar farinaceous products
    '1075',  # Manufacture of prepared meals and dishes
    '1076',  # Processing of coffee and tea
    '1079',  # Manufacture of other food products n.e.c.
    '108',  # Manufacture of prepared animal feeds
    '1080',  # Manufacture of prepared animal feeds
    '11',  # Manufacture of beverages
    '110',  # Manufacture of beverages
    '1101',  # Distilling, rectifying and blending of spirits
    '1102',  # Manufacture of wines
    '1103',  # Manufacture of beer
    '1104',  # Manufacture of malt
    '1105',  # Manufacture of soft drinks; production of mineral waters and other bottled waters
    '12',  # Manufacture of tobacco products
    '120',  # Manufacture of tobacco products
    '1200',  # Manufacture of tobacco products
    '13',  # Manufacture of textiles
    '131',  # Spinning, weaving and finishing of textiles
    '1311',  # Preparation and spinning of textile fibres
    '1312',  # Weaving of textiles
    '1313',  # Finishing of textiles
    '139',  # Manufacture of other textiles
    '1391',  # Manufacture of knitted and crocheted fabrics
    '1392',  # Manufacture of made-up textile articles, except apparel
    '1393',  # Manufacture of carpets and rugs
    '1394',  # Manufacture of cordage, rope, twine and netting
    '1399',  # Manufacture of other textiles n.e.c.
    '14',  # Manufacture of wearing apparel
    '141',  # Manufacture of wearing apparel, except fur apparel
    '1410',  # Manufacture of wearing apparel, except fur apparel
    '142',  # Manufacture of articles of fur
    '1420',  # Manufacture of articles of fur
    '143',  # Manufacture of knitted and crocheted apparel
    '1430',  # Manufacture of knitted and crocheted apparel
    '15',  # Manufacture of leather and related products
    '151',  # Tanning, dyeing, dressing of leather and fur; manufacture of luggage, handbags, saddlery and harness
    '1511',  # Tanning and dressing of leather; dressing and dyeing of fur
    '1512',  # Manufacture of luggage, handbags and the like, saddlery and harness of any material
    '152',  # Manufacture of footwear
    '1520',  # Manufacture of footwear
    '16',  # Manufacture of wood and of products of wood and cork, except furniture; manufacture of articles of straw and plaiting materials
    '161',  # Sawmilling and planing of wood
    '1610',  # Sawmilling and planing of wood
    '162',  # Manufacture of products of wood, cork, straw and plaiting materials
    '1621',  # Manufacture of veneer sheets and wood-based panels
    '1622',  # Manufacture of builders' carpentry and joinery
    '1623',  # Manufacture of wooden containers
    '1629',  # Manufacture of other products of wood; manufacture of articles of cork, straw and plaiting materials
    '17',  # Manufacture of paper and paper products
    '170',  # Manufacture of paper and paper products
    '1701',  # Manufacture of pulp, paper and paperboard
    '1702',  # Manufacture of corrugated paper and paperboard and of containers of paper and paperboard
    '1709',  # Manufacture of other articles of paper and paperboard
    '18',  # Printing and reproduction of recorded media
    '181',  # Printing and service activities related to printing
    '1811',  # Printing
    '1812',  # Service activities related to printing
    '182',  # Reproduction of recorded media
    '1820',  # Reproduction of recorded media
    '19',  # Manufacture of coke and refined petroleum products
    '191',  # Manufacture of coke oven products
    '1910',  # Manufacture of coke oven products
    '192',  # Manufacture of refined petroleum products; manufacture of fossil fuel products
    '1920',  # Manufacture of refined petroleum products; manufacture of fossil fuel products
    '20',  # Manufacture of chemicals and chemical products
    '201',  # Manufacture of basic chemicals, fertilizers and nitrogen compounds, plastics and synthetic rubber in primary forms
    '2011',  # Manufacture of basic chemicals
    '2012',  # Manufacture of fertilizers and nitrogen compounds
    '2013',  # Manufacture of plastics and synthetic rubber in primary forms
    '202',  # Manufacture of other chemical products
    '2021',  # Manufacture of pesticides and other agrochemical products
    '2022',  # Manufacture of paints, varnishes and similar coatings, printing ink and mastics
    '2023',  # Manufacture of soap and detergents, cleaning and polishing preparations, perfumes and toilet preparations
    '2029',  # Manufacture of other chemical products n.e.c.
    '203',  # Manufacture of man-made fibres
    '2030',  # Manufacture of man-made fibres
    '21',  # Manufacture of basic pharmaceutical products and pharmaceutical preparations
    '210',  # Manufacture of pharmaceuticals, medicinal chemical and botanical products
    '2100',  # Manufacture of pharmaceuticals, medicinal chemical and botanical products
    '22',  # Manufacture of rubber and plastic products
    '221',  # Manufacture of rubber products
    '2211',  # Manufacture of rubber tyres and tubes; retreading and rebuilding of rubber tyres
    '2219',  # Manufacture of other rubber products
    '222',  # Manufacture of plastics products
    '2220',  # Manufacture of plastics products
    '23',  # Manufacture of other non-metallic mineral products
    '231',  # Manufacture of glass and glass products
    '2310',  # Manufacture of glass and glass products
    '239',  # Manufacture of non-metallic mineral products n.e.c.
    '2391',  # Manufacture of refractory products
    '2392',  # Manufacture of clay building materials
    '2393',  # Manufacture of other porcelain and ceramic products
    '2394',  # Manufacture of cement, lime and plaster
    '2395',  # Manufacture of articles of concrete, cement and plaster
    '2396',  # Cutting, shaping and finishing of stone
    '2399',  # Manufacture of other non-metallic mineral products n.e.c.
    '24',  # Manufacture of basic metals
    '241',  # Manufacture of basic iron and steel
    '2410',  # Manufacture of basic iron and steel
    '242',  # Manufacture of basic precious and other non-ferrous metals
    '2420',  # Manufacture of basic precious and other non-ferrous metals
    '243',  # Casting of metals
    '2431',  # Casting of iron and steel
    '2432',  # Casting of non-ferrous metals
    '25',  # Manufacture of fabricated metal products, except machinery and equipment
    '251',  # Manufacture of structural metal products, tanks, reservoirs and steam generators
    '2511',  # Manufacture of structural metal products
    '2512',  # Manufacture of tanks, reservoirs and containers of metal
    '2513',  # Manufacture of steam generators, except central heating hot water boilers
    '252',  # Manufacture of weapons and ammunition
    '2520',  # Manufacture of weapons and ammunition
    '259',  # Manufacture of other fabricated metal products; metalworking service activities
    '2591',  # Forging, pressing, stamping and roll-forming of metal; powder metallurgy
    '2592',  # Treatment and coating of metals; machining
    '2593',  # Manufacture of cutlery, hand tools and general hardware
    '2599',  # Manufacture of other fabricated metal products n.e.c.
    '26',  # Manufacture of computer, electronic and optical products
    '261',  # Manufacture of electronic components and boards
    '2611',  # Manufacture of solar cells, solar panels and photovoltaic inverters
    '2619',  # Manufacture of other electronic components and boards
    '262',  # Manufacture of computers and peripheral equipment
    '2620',  # Manufacture of computers and peripheral equipment
    '263',  # Manufacture of communication equipment
    '2630',  # Manufacture of communication equipment
    '264',  # Manufacture of consumer electronics
    '2640',  # Manufacture of consumer electronics
    '265',  # Manufacture of measuring, testing, navigating and control equipment; watches and clocks
    '2651',  # Manufacture of measuring, testing, navigating and control equipment
    '2652',  # Manufacture of watches and clocks
    '266',  # Manufacture of irradiation, electromedical and electrotherapeutic equipment
    '2660',  # Manufacture of irradiation, electromedical and electrotherapeutic equipment
    '267',  # Manufacture of optical instruments and photographic equipment
    '2670',  # Manufacture of optical instruments and photographic equipment
    '268',  # Manufacture of magnetic and optical media
    '2680',  # Manufacture of magnetic and optical media
    '27',  # Manufacture of electrical equipment
    '271',  # Manufacture of electric motors, generators, transformers and electricity distribution and control apparatus
    '2710',  # Manufacture of electric motors, generators, transformers and electricity distribution and control apparatus
    '272',  # Manufacture of batteries and accumulators
    '2720',  # Manufacture of batteries and accumulators
    '273',  # Manufacture of wiring and wiring devices
    '2731',  # Manufacture of fibre optic cables
    '2732',  # Manufacture of other electronic and electric wires and cables
    '2733',  # Manufacture of wiring devices
    '274',  # Manufacture of lighting equipment
    '2740',  # Manufacture of lighting equipment
    '275',  # Manufacture of domestic appliances
    '2750',  # Manufacture of domestic appliances
    '279',  # Manufacture of other electrical equipment
    '2790',  # Manufacture of other electrical equipment
    '28',  # Manufacture of machinery and equipment n.e.c.
    '281',  # Manufacture of general-purpose machinery
    '2811',  # Manufacture of engines and turbines, except aircraft, vehicle and cycle engines
    '2812',  # Manufacture of fluid power equipment
    '2813',  # Manufacture of other pumps, compressors, taps and valves
    '2814',  # Manufacture of bearings, gears, gearing and driving elements
    '2815',  # Manufacture of ovens, furnaces and permanent household heating equipment
    '2816',  # Manufacture of lifting and handling equipment
    '2817',  # Manufacture of office machinery and equipment (except computers and peripheral equipment)
    '2818',  # Manufacture of power-driven hand tools
    '2819',  # Manufacture of other general-purpose machinery
    '282',  # Manufacture of special-purpose machinery
    '2821',  # Manufacture of agricultural and forestry machinery
    '2822',  # Manufacture of metal-forming machinery and machine tools
    '2823',  # Manufacture of machinery for metallurgy
    '2824',  # Manufacture of machinery for mining, quarrying and construction
    '2825',  # Manufacture of machinery for food, beverage and tobacco processing
    '2826',  # Manufacture of machinery for textile, apparel and leather production
    '2829',  # Manufacture of other special-purpose machinery
    '29',  # Manufacture of motor vehicles, trailers and semi-trailers
    '291',  # Manufacture of motor vehicles
    '2910',  # Manufacture of motor vehicles
    '292',  # Manufacture of bodies (coachwork) for motor vehicles; manufacture of trailers and semi-trailers
    '2920',  # Manufacture of bodies (coachwork) for motor vehicles; manufacture of trailers and semi-trailers
    '293',  # Manufacture of parts and accessories for motor vehicles
    '2930',  # Manufacture of parts and accessories for motor vehicles
    '30',  # Manufacture of other transport equipment
    '301',  # Building of ships and boats
    '3011',  # Building of ships and floating structures
    '3012',  # Building of pleasure and sporting boats
    '302',  # Manufacture of railway locomotives and rolling stock
    '3020',  # Manufacture of railway locomotives and rolling stock
    '303',  # Manufacture of air and spacecraft and related machinery
    '3030',  # Manufacture of air and spacecraft and related machinery
    '304',  # Manufacture of military fighting vehicles
    '3040',  # Manufacture of military fighting vehicles
    '309',  # Manufacture of transport equipment n.e.c.
    '3091',  # Manufacture of motorcycles
    '3092',  # Manufacture of bicycles and invalid carriages
    '3099',  # Manufacture of other transport equipment n.e.c.
    '31',  # Manufacture of furniture
    '310',  # Manufacture of furniture
    '3101',  # Manufacture of wooden furniture
    '3102',  # Manufacture of other furniture
    '32',  # Other manufacturing
    '321',  # Manufacture of jewellery, bijouterie and related articles
    '3211',  # Manufacture of jewellery and related articles
    '3212',  # Manufacture of imitation jewellery and related articles
    '322',  # Manufacture of musical instruments
    '3220',  # Manufacture of musical instruments
    '323',  # Manufacture of sports goods
    '3230',  # Manufacture of sports goods
    '324',  # Manufacture of games and toys
    '3240',  # Manufacture of games and toys
    '325',  # Manufacture of medical and dental instruments and supplies
    '3250',  # Manufacture of medical and dental instruments and supplies
    '329',  # Other manufacturing n.e.c.
    '3290',  # Other manufacturing n.e.c.
    '33',  # Repair, maintenance and installation of machinery and equipment
    '331',  # Repair and maintenance of fabricated metal products, machinery and equipment
    '3311',  # Repair and maintenance of fabricated metal products
    '3312',  # Repair and maintenance of machinery
    '3313',  # Repair and maintenance of electronic and optical equipment
    '3314',  # Repair and maintenance of electrical equipment
    '3315',  # Repair and maintenance of transport equipment, except motor vehicles
    '3319',  # Repair and maintenance of other equipment
    '332',  # Installation of industrial machinery and equipment
    '3320',  # Installation of industrial machinery and equipment
    'D',  # Electricity, gas, steam and air conditioning supply
    '35',  # Electricity, gas, steam and air conditioning supply
    '351',  # Electric power generation, transmission and distribution activities
    '3511',  # Electric power generation activities from non-renewable sources
    '3512',  # Electric power generation activities from renewable sources
    '3513',  # Electric power transmission and distribution activities
    '352',  # Manufacture of gas; distribution of gaseous fuels through mains
    '3520',  # Manufacture of gas; distribution of gaseous fuels through mains
    '353',  # Steam and air conditioning supply
    '3530',  # Steam and air conditioning supply
    '354',  # Activities of brokers and agents for electric power and natural gas
    '3540',  # Activities of brokers and agents for electric power and natural gas
    'E',  # Water supply; sewerage, waste management and remediation activities
    '36',  # Water collection, treatment and supply
    '360',  # Water collection, treatment and supply
    '3600',  # Water collection, treatment and supply
    '37',  # Sewerage
    '370',  # Sewerage
    '3700',  # Sewerage
    '38',  # Waste collection, treatment and disposal, and recovery activities
    '381',  # Waste collection activities
    '3811',  # Collection of non-hazardous waste
    '3812',  # Collection of hazardous waste
    '382',  # Waste treatment and disposal
    '3821',  # Treatment and disposal of non-hazardous waste
    '3822',  # Treatment and disposal of hazardous waste
    '383',  # Materials and other waste recovery
    '3830',  # Materials and other waste recovery
    '39',  # Remediation and other waste management service activities
    '390',  # Remediation and other waste management service activities
    '3900',  # Remediation and other waste management service activities
    'F',  # Construction
    '41',  # Construction of residential and non-residential buildings
    '410',  # Construction of residential and non-residential buildings
    '4100',  # Construction of residential and non-residential buildings
    '42',  # Civil engineering
    '421',  # Construction of roads and railways
    '4210',  # Construction of roads and railways
    '422',  # Construction of utility projects
    '4220',  # Construction of utility projects
    '429',  # Construction of other civil engineering projects
    '4290',  # Construction of other civil engineering projects
    '43',  # Specialized construction activities
    '431',  # Demolition and site preparation
    '4311',  # Demolition
    '4312',  # Site preparation
    '432',  # Electrical, plumbing and other construction installation activities
    '4321',  # Electrical installation
    '4322',  # Plumbing, heat and air-conditioning installation
    '4329',  # Other construction installation
    '433',  # Building completion and finishing
    '4330',  # Building completion and finishing
    '434',  # Intermediation service activities for specialized construction services
    '4340',  # Intermediation service activities for specialized construction services
    '439',  # Other specialized construction activities
    '4390',  # Other specialized construction activities
    'G',  # Wholesale and retail trade
    '46',  # Wholesale trade
    '461',  # Wholesale on a fee or contract basis
    '4610',  # Wholesale on a fee or contract basis
    '462',  # Wholesale of agricultural raw materials and live animals
    '4620',  # Wholesale of agricultural raw materials and live animals
    '463',  # Wholesale of food, beverages and tobacco
    '4630',  # Wholesale of food, beverages and tobacco
    '464',  # Wholesale of household goods
    '4641',  # Wholesale of textiles, clothing and footwear
    '4642',  # Wholesale of household, office and shop furniture, carpets and lighting equipment
    '4649',  # Wholesale of other household goods
    '465',  # Wholesale of machinery, equipment and supplies
    '4651',  # Wholesale of computers, computer peripheral equipment and software
    '4652',  # Wholesale of electronic and telecommunications equipment and parts
    '4653',  # Wholesale of agricultural machinery, equipment and supplies
    '4659',  # Wholesale of other machinery and equipment
    '466',  # Wholesale of motor vehicles, motorcycles and related parts and accessories
    '4661',  # Wholesale of motor vehicles
    '4662',  # Wholesale of motor vehicle parts and accessories
    '4663',  # Wholesale of motorcycles, motorcycle parts and accessories
    '467',  # Other specialized wholesale
    '4671',  # Wholesale of solid, liquid and gaseous fuels and related products
    '4672',  # Wholesale of metals and metal ores
    '4673',  # Wholesale of construction materials, hardware, plumbing and heating equipment and supplies
    '4679',  # Wholesale of chemicals, waste and scrap and other products n.e.c.
    '469',  # Non-specialized wholesale trade
    '4690',  # Non-specialized wholesale trade
    '47',  # Retail trade
    '471',  # Non-specialized retail sale
    '4711',  # Non-specialized retail sale with food, beverages or tobacco predominating
    '4719',  # Other non-specialized retail sale
    '472',  # Retail sale of food, beverages and tobacco
    '4721',  # Retail sale of food
    '4722',  # Retail sale of beverages
    '4723',  # Retail sale of tobacco products
    '473',  # Retail sale of automotive fuel
    '4730',  # Retail sale of automotive fuel
    '474',  # Retail sale of information and communication equipment
    '4740',  # Retail sale of information and communication equipment
    '475',  # Retail sale of other household equipment
    '4751',  # Retail sale of textiles
    '4752',  # Retail sale of hardware, building materials, paints and glass
    '4753',  # Retail sale of carpets, rugs, wall and floor coverings
    '4759',  # Retail sale of electrical household appliances, furniture, lighting equipment and other household articles
    '476',  # Retail sale of cultural and recreational goods
    '4761',  # Retail sale of books, newspapers, stationery and office supplies
    '4762',  # Retail sale of sporting equipment
    '4763',  # Retail sale of games and toys
    '4769',  # Retail sale of cultural and recreational goods n.e.c.
    '477',  # Retail sale of other goods, except motor vehicles and motorcycles
    '4771',  # Retail sale of clothing, footwear and leather articles
    '4772',  # Retail sale of pharmaceutical and medical goods, cosmetic and toilet articles
    '4773',  # Retail sale of other new goods n.e.c.
    '4774',  # Retail sale of second-hand goods
    '478',  # Retail sale of motor vehicles, motorcycles and related parts and accessories
    '4781',  # Retail sale of motor vehicles
    '4782',  # Retail sale of motor vehicle parts and accessories
    '4783',  # Retail sale of motorcycles, motorcycles parts and accessories
    '479',  # Intermediation service activities for retail sale
    '4790',  # Intermediation service activities for retail sale
    'H',  # Transportation and storage
    '49',  # Land transport and transport via pipelines
    '491',  # Transport via railways
    '4911',  # Passenger rail transport, interurban
    '4912',  # Freight rail transport
    '492',  # Other land transport
    '4921',  # Urban and suburban passenger land transport
    '4922',  # Other passenger land transport
    '4923',  # Freight transport by road
    '493',  # Transport via pipeline
    '4930',  # Transport via pipeline
    '50',  # Water transport
    '501',  # Sea and coastal water transport
    '5011',  # Sea and coastal passenger water transport
    '5012',  # Sea and coastal freight water transport
    '502',  # Inland water transport
    '5021',  # Inland passenger water transport
    '5022',  # Inland freight water transport
    '51',  # Air transport
    '511',  # Passenger air transport
    '5110',  # Passenger air transport
    '512',  # Freight air transport
    '5120',  # Freight air transport
    '52',  # Warehousing and support activities for transportation
    '521',  # Warehousing and storage
    '5210',  # Warehousing and storage
    '522',  # Support activities for transportation
    '5221',  # Service activities incidental to land transportation
    '5222',  # Service activities incidental to water transportation
    '5223',  # Service activities incidental to air transportation
    '5224',  # Cargo handling
    '5229',  # Other support activities for transportation
    '523',  # Intermediation service activities for transportation
    '5231',  # Intermediation service activities for freight transportation
    '5232',  # Intermediation service activities for passenger transportation
    '53',  # Postal and courier activities
    '531',  # Postal activities
    '5310',  # Postal activities
    '532',  # Courier activities
    '5320',  # Courier activities
    '533',  # Intermediation service activities for postal and courier activities
    '5330',  # Intermediation service activities for postal and courier activities
    'I',  # Accommodation and food service activities
    '55',  # Accommodation
    '551',  # Hotels and similar accommodation activities
    '5510',  # Hotels and similar accommodation activities
    '552',  # Other short term accommodation activities
    '5520',  # Other short term accommodation activities
    '553',  # Camping grounds, recreational vehicle parks and trailer parks
    '5530',  # Camping grounds, recreational vehicle parks and trailer parks
    '554',  # Intermediation service activities for accommodation
    '5540',  # Intermediation service activities for accommodation
    '559',  # Other accommodation n.e.c.
    '5590',  # Other accommodation n.e.c.
    '56',  # Food and beverage service activities
    '561',  # Restaurants and mobile food service activities
    '5610',  # Restaurants and mobile food service activities
    '562',  # Event catering and other food service activities
    '5621',  # Event catering activities
    '5629',  # Other food service activities
    '563',  # Beverage serving activities
    '5630',  # Beverage serving activities
    '564',  # Intermediation service activities for food and beverage services activities
    '5640',  # Intermediation service activities for food and beverage services activities
    'J',  # Publishing, broadcasting, and content production and distribution activities
    '58',  # Publishing activities
    '581',  # Publishing of books, newspapers, periodicals and other publishing activities
    '5811',  # Publishing of books
    '5812',  # Publishing of newspapers
    '5813',  # Publishing of journals and periodicals
    '5819',  # Other publishing activities
    '582',  # Software publishing
    '5821',  # Publishing of video games
    '5829',  # Other software publishing
    '59',  # Motion picture, video and television programme production, sound recording and music publishing activities
    '591',  # Motion picture, video and television programme activities
    '5911',  # Motion picture, video and television programme production activities
    '5912',  # Motion picture, video and television programme post-production activities
    '5913',  # Motion picture, video and television programme distribution activities
    '5914',  # Motion picture projection activities
    '592',  # Sound recording and music publishing activities
    '5920',  # Sound recording and music publishing activities
    '60',  # Programming, broadcasting, news agency and other content distribution activities
    '601',  # Radio broadcasting and audio distribution activities
    '6010',  # Radio broadcasting and audio distribution activities
    '602',  # Television programming, broadcasting and video distribution activities
    '6020',  # Television programming, broadcasting and video distribution activities
    '603',  # News agency and other content distribution activities
    '6031',  # News agency activities
    '6039',  # Social network sites and other content distribution activities
    'K',  # Telecommunications, computer programming, consultancy, computing infrastructure, and other information service activities
    '61',  # Telecommunications
    '611',  # Wired, wireless, and satellite telecommunication activities
    '6110',  # Wired, wireless, and satellite telecommunication activities
    '612',  # Telecommunication reselling activities and intermediation service activities for telecommunication
    '6120',  # Telecommunication reselling activities and intermediation service activities for telecommunication
    '619',  # Other telecommunication activities
    '6190',  # Other telecommunication activities
    '62',  # Computer programming, consultancy and related activities
    '621',  # Computer programming activities
    '6211',  # Development of video games, video game software, and video game software tools
    '6219',  # Other computer programming activities
    '622',  # Computer consultancy and computer facilities management activities
    '6220',  # Computer consultancy and computer facilities management activities
    '629',  # Other information technology and computer service activities
    '6290',  # Other information technology and computer service activities
    '63',  # Computing infrastructure, data processing, hosting, and other information service activities
    '631',  # Computing infrastructure, data processing, hosting and related activities
    '6310',  # Computing infrastructure, data processing, hosting and related activities
    '639',  # Web search portals activities and other information service activities
    '6390',  # Web search portals activities and other information service activities
    'L',  # Financial and insurance activities
    '64',  # Financial service activities, except insurance and pension funding
    '641',  # Monetary intermediation
    '6411',  # Central banking
    '6419',  # Other monetary intermediation
    '642',  # Activities of holding companies and financing conduits
    '6421',  # Activities of holding companies
    '6422',  # Activities of financing conduits
    '643',  # Activities of trusts, funds and similar financial entities
    '6431',  # Activities of money market funds
    '6432',  # Activities of non-money market investments funds
    '6433',  # Activities of trust, estate and agency accounts
    '649',  # Other financial service activities, except insurance and pension funding activities
    '6491',  # Financial leasing activities
    '6492',  # International trade financing activities
    '6493',  # Factoring activities
    '6494',  # Securitisation activities
    '6495',  # Other credit granting activities
    '6499',  # Other financial service activities n.e.c., except insurance and pension funding activities
    '65',  # Insurance, reinsurance and pension funding, except compulsory social security
    '651',  # Insurance
    '6511',  # Life insurance
    '6512',  # Non-life insurance
    '652',  # Reinsurance
    '6520',  # Reinsurance
    '653',  # Pension funding
    '6530',  # Pension funding
    '66',  # Activities auxiliary to financial service and insurance activities
    '661',  # Activities auxiliary to financial services, except insurance and pension funding
    '6611',  # Administration of financial markets
    '6612',  # Security and commodity contracts brokerage
    '6619',  # Other activities auxiliary to financial service activities, except insurance and pension funding
    '662',  # Activities auxiliary to insurance and pension funding
    '6621',  # Risk and damage evaluation
    '6622',  # Activities of insurance agents and brokers
    '6629',  # Other activities auxiliary to insurance and pension funding
    '663',  # Fund management activities
    '6630',  # Fund management activities
    'M',  # Real estate activities
    '68',  # Real estate activities
    '681',  # Real estate activities with own or leased property
    '6810',  # Real estate activities with own or leased property
    '682',  # Real estate activities on a fee or contract basis
    '6821',  # Intermediation service activities for real estate
    '6829',  # Other real estate activities on a fee or contract basis
    'N',  # Professional, scientific and technical activities
    '69',  # Legal and accounting activities
    '691',  # Legal activities
    '6910',  # Legal activities
    '692',  # Accounting, bookkeeping and auditing activities; tax consultancy
    '6920',  # Accounting, bookkeeping and auditing activities; tax consultancy
    '70',  # Activities of head offices; management consultancy activities
    '701',  # Activities of head offices
    '7010',  # Activities of head offices
    '702',  # Business and other management consultancy activities
    '7020',  # Business and other management consultancy activities
    '71',  # Architectural and engineering activities; technical testing and analysis
    '711',  # Architectural and engineering, and related technical consultancy activities
    '7110',  # Architectural and engineering, and related technical consultancy activities
    '712',  # Technical testing and analysis
    '7120',  # Technical testing and analysis
    '72',  # Scientific research and development
    '721',  # Research and experimental development on natural sciences and engineering
    '7210',  # Research and experimental development on natural sciences and engineering
    '722',  # Research and experimental development on social sciences and humanities
    '7220',  # Research and experimental development on social sciences and humanities
    '73',  # Activities of advertising, market research and public relations
    '731',  # Advertising activities
    '7310',  # Advertising activities
    '732',  # Market research and public opinion polling activities
    '7320',  # Market research and public opinion polling activities
    '733',  # Public relations activities
    '7330',  # Public relations activities
    '74',  # Other professional, scientific and technical activities
    '741',  # Specialized design activities
    '7410',  # Specialized design activities
    '742',  # Photographic activities
    '7420',  # Photographic activities
    '743',  # Translation and interpretation activities
    '7430',  # Translation and interpretation activities
    '749',  # Other professional, scientific and technical activities n.e.c.
    '7491',  # Patent brokering and marketing service activities
    '7499',  # All other professional, scientific and technical activities n.e.c.
    '75',  # Veterinary activities
    '750',  # Veterinary activities
    '7500',  # Veterinary activities
    'O',  # Administrative and support service activities
    '77',  # Rental and leasing activities
    '771',  # Rental and leasing of motor vehicles
    '7710',  # Rental and leasing of motor vehicles
    '772',  # Rental and leasing of personal and household goods
    '7721',  # Rental and leasing of recreational and sports goods
    '7729',  # Rental and leasing of other personal and household goods
    '773',  # Rental and leasing of other machinery, equipment and tangible goods
    '7730',  # Rental and leasing of other machinery, equipment and tangible goods
    '774',  # Leasing of intellectual property and similar products, except copyrighted works
    '7740',  # Leasing of intellectual property and similar products, except copyrighted works
    '775',  # Intermediation service activities for rental and leasing of tangible goods and non-financial intangible assets
    '7751',  # Intermediation service activities for rental and leasing of cars, motorhomes and trailers
    '7752',  # Intermediation service activities for rental and leasing of other tangible goods and non-financial intangible assets
    '78',  # Employment activities
    '781',  # Activities of employment placement agencies
    '7810',  # Activities of employment placement agencies
    '782',  # Temporary employment agency activities and other human resource provisions
    '7820',  # Temporary employment agency activities and other human resource provisions
    '79',  # Travel agency, tour operator, and other travel related activities
    '791',  # Travel agency and tour operator activities
    '7911',  # Travel agency activities
    '7912',  # Tour operator activities
    '799',  # Other travel related activities
    '7990',  # Other travel related activities
    '80',  # Investigation and security activities
    '801',  # Investigation and security activities
    '8011',  # Investigation and private security activities
    '8019',  # Security activities n.e.c.
    '81',  # Services to buildings and landscape activities
    '811',  # Combined facilities support activities
    '8110',  # Combined facilities support activities
    '812',  # Cleaning activities
    '8121',  # General cleaning of buildings
    '8129',  # Other cleaning activities
    '813',  # Landscape service activities
    '8130',  # Landscape service activities
    '82',  # Office administrative, office support and other business support activities
    '821',  # Office administrative and support activities
    '8210',  # Office administrative and support activities
    '822',  # Activities of call centres
    '8220',  # Activities of call centres
    '823',  # Organization of conventions and trade shows
    '8230',  # Organization of conventions and trade shows
    '824',  # Intermediation service activities for business support activities n.e.c., except financial intermediation
    '8240',  # Intermediation service activities for business support activities n.e.c., except financial intermediation
    '829',  # Business support service activities n.e.c.
    '8291',  # Activities of collection agencies and credit bureaus
    '8292',  # Packaging activities
    '8299',  # Other business support service activities n.e.c.
    'P',  # Public administration and defence; compulsory social security
    '84',  # Public administration and defence; compulsory social security
    '841',  # Administration of the State and the economic, social and environmental policies of the community
    '8411',  # General public administration activities
    '8412',  # Regulation of the activities of providing health care, education, cultural services and other social services, excluding social security and environment
    '8413',  # Regulation of the activities of providing environmental services
    '8414',  # Regulation of and contribution to more efficient operation of businesses
    '842',  # Provision of services to the community as a whole
    '8421',  # Foreign affairs
    '8422',  # Defence activities
    '8423',  # Public order and safety activities
    '843',  # Compulsory social security activities
    '8430',  # Compulsory social security activities
    'Q',  # Education
    '85',  # Education
    '851',  # Pre-primary education
    '8510',  # Pre-primary education
    '852',  # Primary education
    '8520',  # Primary education
    '853',  # Secondary and post-secondary non-tertiary education
    '8531',  # General secondary education
    '8532',  # Vocational secondary education
    '8533',  # Post-secondary non-tertiary education
    '854',  # Tertiary education
    '8540',  # Tertiary education
    '855',  # Other education
    '8551',  # Sports and recreation education
    '8552',  # Cultural education
    '8553',  # Driving school activities
    '8559',  # Other education n.e.c.
    '856',  # Educational support activities
    '8561',  # Intermediation service activities for courses and tutors
    '8569',  # Other educational support activities
    'R',  # Human health and social work activities
    '86',  # Human health activities
    '861',  # Hospital activities
    '8610',  # Hospital activities
    '862',  # Medical and dental practice activities
    '8620',  # Medical and dental practice activities
    '869',  # Other human health activities
    '8691',  # Intermediation service activities for medical, dental, and other human health services
    '8699',  # Other human health activities n.e.c
    '87',  # Residential care activities
    '871',  # Residential nursing care activities
    '8710',  # Residential nursing care activities
    '872',  # Residential care activities for persons living with or having a diagnosis of a mental illness or substance abuse
    '8720',  # Residential care activities for persons living with or having a diagnosis of a mental illness or substance abuse
    '873',  # Residential care activities for older persons or persons with physical disabilities
    '8730',  # Residential care activities for older persons or persons with physical disabilities
    '879',  # Other residential care activities
    '8791',  # Intermediation service activities for residential care activities
    '8799',  # Other residential care activities n.e.c.
    '88',  # Social work activities without accommodation
    '881',  # Social work activities without accommodation for older persons or persons with disabilities
    '8810',  # Social work activities without accommodation for older persons or persons with disabilities
    '889',  # Other social work activities without accommodation
    '8890',  # Other social work activities without accommodation
    'S',  # Arts, sports and recreation
    '90',  # Arts creation and performing arts activities
    '901',  # Arts creation activities
    '9011',  # Literary creation and musical composition activities
    '9012',  # Visual arts creation activities
    '9013',  # Other arts creation activities
    '902',  # Activities of performing arts
    '9020',  # Activities of performing arts
    '903',  # Support activities to arts creation and performing arts
    '9031',  # Operation of arts facilities and sites
    '9039',  # Other support activities to arts creation and performing arts
    '91',  # Library, archives, museum and other cultural activities
    '911',  # Library and archive activities
    '9111',  # Library activities
    '9112',  # Archive activities
    '912',  # Museum, collection, historical site and monument activities
    '9121',  # Museum and collection activities
    '9122',  # Historical site and monument activities
    '913',  # Conservation, restoration and other support activities for cultural heritage
    '9130',  # Conservation, restoration and other support activities for cultural heritage
    '914',  # Botanical and zoological garden and nature reserve activities
    '9141',  # Botanical and zoological garden activities
    '9142',  # Nature reserve activities
    '92',  # Gambling and betting activities
    '920',  # Gambling and betting activities
    '9200',  # Gambling and betting activities
    '93',  # Sports activities and amusement and recreation activities
    '931',  # Sports activities
    '9311',  # Operation of sports facilities
    '9312',  # Activities of sports clubs
    '9319',  # Other sports activities
    '932',  # Amusement and recreation activities
    '9321',  # Activities of amusement parks and theme parks
    '9329',  # Other amusement and recreation activities
    'T',  # Other service activities
    '94',  # Activities of membership organizations
    '941',  # Activities of business, employers and professional membership organizations
    '9411',  # Activities of business and employers membership organizations
    '9412',  # Activities of professional membership organizations
    '942',  # Activities of trade unions
    '9420',  # Activities of trade unions
    '949',  # Activities of other membership organizations
    '9491',  # Activities of religious organizations
    '9492',  # Activities of political organizations
    '9499',  # Activities of other membership organizations n.e.c.
    '95',  # Repair and maintenance of computers, personal and household goods, and motor vehicles and motorcycles
    '951',  # Repair and maintenance of computers and communication equipment
    '9510',  # Repair and maintenance of computers and communication equipment
    '952',  # Repair and maintenance of personal and household goods
    '9521',  # Repair and maintenance of consumer electronics
    '9522',  # Repair and maintenance of household appliances and home and garden equipment
    '9523',  # Repair and maintenance of footwear and leather goods
    '9524',  # Repair and maintenance of furniture and home furnishings
    '9529',  # Repair and maintenance of other personal and household goods
    '953',  # Repair and maintenance of motor vehicles and motorcycles
    '9531',  # Repair and maintenance of motor vehicles
    '9532',  # Repair and maintenance of motorcycles
    '954',  # Intermediation service activities for repair and maintenance of computers, personal and household goods, and motor vehicles and motorcycles
    '9540',  # Intermediation service activities for repair and maintenance of computers, personal and household goods, and motor vehicles and motorcycles
    '96',  # Personal service activities
    '961',  # Washing and cleaning of textile and fur products
    '9610',  # Washing and cleaning of textile and fur products
    '962',  # Hairdressing, beauty treatment, day spa and similar activities
    '9621',  # Hairdressing and barber activities
    '9622',  # Beauty care and other beauty treatment activities
    '9623',  # Day spa, sauna and steam bath activities
    '963',  # Funeral and related activities
    '9630',  # Funeral and related activities
    '964',  # Intermediation service activities for personal services
    '9640',  # Intermediation service activities for personal services
    '969',  # Other personal service activities n.e.c.
    '9690',  # Other personal service activities n.e.c.
    'U',  # Activities of households as employers; undifferentiated goods- and services-producing activities of households for own use
    '97',  # Activities of households as employers of domestic personnel
    '970',  # Activities of households as employers of domestic personnel
    '9700',  # Activities of households as employers of domestic personnel
    '98',  # Undifferentiated goods- and services-producing activities of private households for own use
    '981',  # Undifferentiated goods-producing activities of private households for own use
    '9810',  # Undifferentiated goods-producing activities of private households for own use
    '982',  # Undifferentiated service-producing activities of private households for own use
    '9820',  # Undifferentiated service-producing activities of private households for own use
    'V',  # Activities of extraterritorial organizations and bodies
    '99',  # Activities of extraterritorial organizations and bodies
    '990',  # Activities of extraterritorial organizations and bodies
    '9900',  # Activities of extraterritorial organizations and bodies
]


# Type-safe union of all processes category text values
# Note: This is a very large Literal type with ~649 values.
# The full list is generated from PROCESSES_CATEGORIES.
# For type checking purposes, we use str as the actual type since
# Python's type checker may have issues with such large Literal types.
# In practice, the values are validated at runtime using PROCESSES_CATEGORIES.
TidasProcessesText = str  # Effectively all text values from PROCESSES_CATEGORIES


# Runtime metadata for lookups
PROCESSES_CATEGORIES: dict[str, ProcessesCategoryData] = {
    'A': {
        'level': '0',
        'classId': 'A',
        'text': 'Agriculture, forestry and fishing',
    },
    '01': {
        'level': '1',
        'classId': '01',
        'text': 'Crop and animal production, hunting and related service activities',
    },
    '011': {
        'level': '2',
        'classId': '011',
        'text': 'Growing of non-perennial crops',
    },
    '0111': {
        'level': '3',
        'classId': '0111',
        'text': 'Growing of cereals (except rice), leguminous crops and oil seeds',
    },
    '0112': {
        'level': '3',
        'classId': '0112',
        'text': 'Growing of rice',
    },
    '0113': {
        'level': '3',
        'classId': '0113',
        'text': 'Growing of vegetables and melons, roots and tubers',
    },
    '0114': {
        'level': '3',
        'classId': '0114',
        'text': 'Growing of sugar cane',
    },
    '0115': {
        'level': '3',
        'classId': '0115',
        'text': 'Growing of tobacco',
    },
    '0116': {
        'level': '3',
        'classId': '0116',
        'text': 'Growing of fibre crops',
    },
    '0119': {
        'level': '3',
        'classId': '0119',
        'text': 'Growing of other non-perennial crops',
    },
    '012': {
        'level': '2',
        'classId': '012',
        'text': 'Growing of perennial crops',
    },
    '0121': {
        'level': '3',
        'classId': '0121',
        'text': 'Growing of grapes',
    },
    '0122': {
        'level': '3',
        'classId': '0122',
        'text': 'Growing of tropical and subtropical fruits',
    },
    '0123': {
        'level': '3',
        'classId': '0123',
        'text': 'Growing of citrus fruits',
    },
    '0124': {
        'level': '3',
        'classId': '0124',
        'text': 'Growing of pome fruits and stone fruits',
    },
    '0125': {
        'level': '3',
        'classId': '0125',
        'text': 'Growing of other tree and bush fruits and nuts',
    },
    '0126': {
        'level': '3',
        'classId': '0126',
        'text': 'Growing of oleaginous fruits',
    },
    '0127': {
        'level': '3',
        'classId': '0127',
        'text': 'Growing of beverage crops',
    },
    '0128': {
        'level': '3',
        'classId': '0128',
        'text': 'Growing of spices, aromatic, drug and pharmaceutical crops',
    },
    '0129': {
        'level': '3',
        'classId': '0129',
        'text': 'Growing of other perennial crops',
    },
    '013': {
        'level': '2',
        'classId': '013',
        'text': 'Plant propagation',
    },
    '0130': {
        'level': '3',
        'classId': '0130',
        'text': 'Plant propagation',
    },
    '014': {
        'level': '2',
        'classId': '014',
        'text': 'Animal production',
    },
    '0141': {
        'level': '3',
        'classId': '0141',
        'text': 'Raising of cattle and buffaloes',
    },
    '0142': {
        'level': '3',
        'classId': '0142',
        'text': 'Raising of horses and other equines',
    },
    '0143': {
        'level': '3',
        'classId': '0143',
        'text': 'Raising of camels and camelids',
    },
    '0144': {
        'level': '3',
        'classId': '0144',
        'text': 'Raising of sheep and goats',
    },
    '0145': {
        'level': '3',
        'classId': '0145',
        'text': 'Raising of swine and pigs',
    },
    '0146': {
        'level': '3',
        'classId': '0146',
        'text': 'Raising of poultry',
    },
    '0149': {
        'level': '3',
        'classId': '0149',
        'text': 'Raising of other animals',
    },
    '015': {
        'level': '2',
        'classId': '015',
        'text': 'Mixed farming',
    },
    '0150': {
        'level': '3',
        'classId': '0150',
        'text': 'Mixed farming',
    },
    '016': {
        'level': '2',
        'classId': '016',
        'text': 'Support activities to agriculture and post-harvest crop activities',
    },
    '0161': {
        'level': '3',
        'classId': '0161',
        'text': 'Support activities for crop production',
    },
    '0162': {
        'level': '3',
        'classId': '0162',
        'text': 'Support activities for animal production',
    },
    '0163': {
        'level': '3',
        'classId': '0163',
        'text': 'Post-harvest crop activities',
    },
    '0164': {
        'level': '3',
        'classId': '0164',
        'text': 'Seed processing for propagation',
    },
    '017': {
        'level': '2',
        'classId': '017',
        'text': 'Hunting, trapping and related service activities',
    },
    '0170': {
        'level': '3',
        'classId': '0170',
        'text': 'Hunting, trapping and related service activities',
    },
    '02': {
        'level': '1',
        'classId': '02',
        'text': 'Forestry and logging',
    },
    '021': {
        'level': '2',
        'classId': '021',
        'text': 'Silviculture and other forestry activities',
    },
    '0210': {
        'level': '3',
        'classId': '0210',
        'text': 'Silviculture and other forestry activities',
    },
    '022': {
        'level': '2',
        'classId': '022',
        'text': 'Logging',
    },
    '0220': {
        'level': '3',
        'classId': '0220',
        'text': 'Logging',
    },
    '023': {
        'level': '2',
        'classId': '023',
        'text': 'Gathering of non-wood forest products',
    },
    '0230': {
        'level': '3',
        'classId': '0230',
        'text': 'Gathering of non-wood forest products',
    },
    '024': {
        'level': '2',
        'classId': '024',
        'text': 'Support services to forestry',
    },
    '0240': {
        'level': '3',
        'classId': '0240',
        'text': 'Support services to forestry',
    },
    '03': {
        'level': '1',
        'classId': '03',
        'text': 'Fishing and aquaculture',
    },
    '031': {
        'level': '2',
        'classId': '031',
        'text': 'Fishing',
    },
    '0311': {
        'level': '3',
        'classId': '0311',
        'text': 'Marine fishing',
    },
    '0312': {
        'level': '3',
        'classId': '0312',
        'text': 'Freshwater fishing',
    },
    '032': {
        'level': '2',
        'classId': '032',
        'text': 'Aquaculture',
    },
    '0321': {
        'level': '3',
        'classId': '0321',
        'text': 'Marine aquaculture',
    },
    '0322': {
        'level': '3',
        'classId': '0322',
        'text': 'Freshwater aquaculture',
    },
    '033': {
        'level': '2',
        'classId': '033',
        'text': 'Support activities for fishing and aquaculture',
    },
    '0330': {
        'level': '3',
        'classId': '0330',
        'text': 'Support activities for fishing and aquaculture',
    },
    'B': {
        'level': '0',
        'classId': 'B',
        'text': 'Mining and quarrying',
    },
    '05': {
        'level': '1',
        'classId': '05',
        'text': 'Mining of coal and lignite',
    },
    '051': {
        'level': '2',
        'classId': '051',
        'text': 'Mining of hard coal',
    },
    '0510': {
        'level': '3',
        'classId': '0510',
        'text': 'Mining of hard coal',
    },
    '052': {
        'level': '2',
        'classId': '052',
        'text': 'Mining of lignite',
    },
    '0520': {
        'level': '3',
        'classId': '0520',
        'text': 'Mining of lignite',
    },
    '06': {
        'level': '1',
        'classId': '06',
        'text': 'Extraction of crude petroleum and natural gas',
    },
    '061': {
        'level': '2',
        'classId': '061',
        'text': 'Extraction of crude petroleum',
    },
    '0610': {
        'level': '3',
        'classId': '0610',
        'text': 'Extraction of crude petroleum',
    },
    '062': {
        'level': '2',
        'classId': '062',
        'text': 'Extraction of natural gas',
    },
    '0620': {
        'level': '3',
        'classId': '0620',
        'text': 'Extraction of natural gas',
    },
    '07': {
        'level': '1',
        'classId': '07',
        'text': 'Mining of metal ores',
    },
    '071': {
        'level': '2',
        'classId': '071',
        'text': 'Mining of iron ores',
    },
    '0710': {
        'level': '3',
        'classId': '0710',
        'text': 'Mining of iron ores',
    },
    '072': {
        'level': '2',
        'classId': '072',
        'text': 'Mining of non-ferrous metal ores',
    },
    '0721': {
        'level': '3',
        'classId': '0721',
        'text': 'Mining of uranium and thorium ores',
    },
    '0729': {
        'level': '3',
        'classId': '0729',
        'text': 'Mining of other non-ferrous metal ores',
    },
    '08': {
        'level': '1',
        'classId': '08',
        'text': 'Other mining and quarrying',
    },
    '081': {
        'level': '2',
        'classId': '081',
        'text': 'Quarrying of stone, sand and clay',
    },
    '0810': {
        'level': '3',
        'classId': '0810',
        'text': 'Quarrying of stone, sand and clay',
    },
    '089': {
        'level': '2',
        'classId': '089',
        'text': 'Mining and quarrying n.e.c.',
    },
    '0891': {
        'level': '3',
        'classId': '0891',
        'text': 'Mining of chemical and fertilizer minerals',
    },
    '0892': {
        'level': '3',
        'classId': '0892',
        'text': 'Extraction of peat',
    },
    '0893': {
        'level': '3',
        'classId': '0893',
        'text': 'Extraction of salt',
    },
    '0899': {
        'level': '3',
        'classId': '0899',
        'text': 'Other mining and quarrying n.e.c.',
    },
    '09': {
        'level': '1',
        'classId': '09',
        'text': 'Mining support service activities',
    },
    '091': {
        'level': '2',
        'classId': '091',
        'text': 'Support activities for petroleum and natural gas extraction',
    },
    '0910': {
        'level': '3',
        'classId': '0910',
        'text': 'Support activities for petroleum and natural gas extraction',
    },
    '099': {
        'level': '2',
        'classId': '099',
        'text': 'Support activities for other mining and quarrying',
    },
    '0990': {
        'level': '3',
        'classId': '0990',
        'text': 'Support activities for other mining and quarrying',
    },
    'C': {
        'level': '0',
        'classId': 'C',
        'text': 'Manufacturing',
    },
    '10': {
        'level': '1',
        'classId': '10',
        'text': 'Manufacture of food products',
    },
    '101': {
        'level': '2',
        'classId': '101',
        'text': 'Processing and preserving of meat',
    },
    '1010': {
        'level': '3',
        'classId': '1010',
        'text': 'Processing and preserving of meat',
    },
    '102': {
        'level': '2',
        'classId': '102',
        'text': 'Processing and preserving of fish, crustaceans and molluscs',
    },
    '1020': {
        'level': '3',
        'classId': '1020',
        'text': 'Processing and preserving of fish, crustaceans and molluscs',
    },
    '103': {
        'level': '2',
        'classId': '103',
        'text': 'Processing and preserving of fruit and vegetables',
    },
    '1030': {
        'level': '3',
        'classId': '1030',
        'text': 'Processing and preserving of fruit and vegetables',
    },
    '104': {
        'level': '2',
        'classId': '104',
        'text': 'Manufacture of vegetable and animal oils and fats',
    },
    '1040': {
        'level': '3',
        'classId': '1040',
        'text': 'Manufacture of vegetable and animal oils and fats',
    },
    '105': {
        'level': '2',
        'classId': '105',
        'text': 'Manufacture of dairy products',
    },
    '1050': {
        'level': '3',
        'classId': '1050',
        'text': 'Manufacture of dairy products',
    },
    '106': {
        'level': '2',
        'classId': '106',
        'text': 'Manufacture of grain mill products, starches and starch products',
    },
    '1061': {
        'level': '3',
        'classId': '1061',
        'text': 'Manufacture of grain mill products',
    },
    '1062': {
        'level': '3',
        'classId': '1062',
        'text': 'Manufacture of starches and starch products',
    },
    '107': {
        'level': '2',
        'classId': '107',
        'text': 'Manufacture of other food products',
    },
    '1071': {
        'level': '3',
        'classId': '1071',
        'text': 'Manufacture of bakery products',
    },
    '1072': {
        'level': '3',
        'classId': '1072',
        'text': 'Manufacture of sugar',
    },
    '1073': {
        'level': '3',
        'classId': '1073',
        'text': 'Manufacture of cocoa, chocolate and sugar confectionery',
    },
    '1074': {
        'level': '3',
        'classId': '1074',
        'text': 'Manufacture of macaroni, noodles, couscous and similar farinaceous products',
    },
    '1075': {
        'level': '3',
        'classId': '1075',
        'text': 'Manufacture of prepared meals and dishes',
    },
    '1076': {
        'level': '3',
        'classId': '1076',
        'text': 'Processing of coffee and tea',
    },
    '1079': {
        'level': '3',
        'classId': '1079',
        'text': 'Manufacture of other food products n.e.c.',
    },
    '108': {
        'level': '2',
        'classId': '108',
        'text': 'Manufacture of prepared animal feeds',
    },
    '1080': {
        'level': '3',
        'classId': '1080',
        'text': 'Manufacture of prepared animal feeds',
    },
    '11': {
        'level': '1',
        'classId': '11',
        'text': 'Manufacture of beverages',
    },
    '110': {
        'level': '2',
        'classId': '110',
        'text': 'Manufacture of beverages',
    },
    '1101': {
        'level': '3',
        'classId': '1101',
        'text': 'Distilling, rectifying and blending of spirits',
    },
    '1102': {
        'level': '3',
        'classId': '1102',
        'text': 'Manufacture of wines',
    },
    '1103': {
        'level': '3',
        'classId': '1103',
        'text': 'Manufacture of beer',
    },
    '1104': {
        'level': '3',
        'classId': '1104',
        'text': 'Manufacture of malt',
    },
    '1105': {
        'level': '3',
        'classId': '1105',
        'text': 'Manufacture of soft drinks; production of mineral waters and other bottled waters',
    },
    '12': {
        'level': '1',
        'classId': '12',
        'text': 'Manufacture of tobacco products',
    },
    '120': {
        'level': '2',
        'classId': '120',
        'text': 'Manufacture of tobacco products',
    },
    '1200': {
        'level': '3',
        'classId': '1200',
        'text': 'Manufacture of tobacco products',
    },
    '13': {
        'level': '1',
        'classId': '13',
        'text': 'Manufacture of textiles',
    },
    '131': {
        'level': '2',
        'classId': '131',
        'text': 'Spinning, weaving and finishing of textiles',
    },
    '1311': {
        'level': '3',
        'classId': '1311',
        'text': 'Preparation and spinning of textile fibres',
    },
    '1312': {
        'level': '3',
        'classId': '1312',
        'text': 'Weaving of textiles',
    },
    '1313': {
        'level': '3',
        'classId': '1313',
        'text': 'Finishing of textiles',
    },
    '139': {
        'level': '2',
        'classId': '139',
        'text': 'Manufacture of other textiles',
    },
    '1391': {
        'level': '3',
        'classId': '1391',
        'text': 'Manufacture of knitted and crocheted fabrics',
    },
    '1392': {
        'level': '3',
        'classId': '1392',
        'text': 'Manufacture of made-up textile articles, except apparel',
    },
    '1393': {
        'level': '3',
        'classId': '1393',
        'text': 'Manufacture of carpets and rugs',
    },
    '1394': {
        'level': '3',
        'classId': '1394',
        'text': 'Manufacture of cordage, rope, twine and netting',
    },
    '1399': {
        'level': '3',
        'classId': '1399',
        'text': 'Manufacture of other textiles n.e.c.',
    },
    '14': {
        'level': '1',
        'classId': '14',
        'text': 'Manufacture of wearing apparel',
    },
    '141': {
        'level': '2',
        'classId': '141',
        'text': 'Manufacture of wearing apparel, except fur apparel',
    },
    '1410': {
        'level': '3',
        'classId': '1410',
        'text': 'Manufacture of wearing apparel, except fur apparel',
    },
    '142': {
        'level': '2',
        'classId': '142',
        'text': 'Manufacture of articles of fur',
    },
    '1420': {
        'level': '3',
        'classId': '1420',
        'text': 'Manufacture of articles of fur',
    },
    '143': {
        'level': '2',
        'classId': '143',
        'text': 'Manufacture of knitted and crocheted apparel',
    },
    '1430': {
        'level': '3',
        'classId': '1430',
        'text': 'Manufacture of knitted and crocheted apparel',
    },
    '15': {
        'level': '1',
        'classId': '15',
        'text': 'Manufacture of leather and related products',
    },
    '151': {
        'level': '2',
        'classId': '151',
        'text': 'Tanning, dyeing, dressing of leather and fur; manufacture of luggage, handbags, saddlery and harness',
    },
    '1511': {
        'level': '3',
        'classId': '1511',
        'text': 'Tanning and dressing of leather; dressing and dyeing of fur',
    },
    '1512': {
        'level': '3',
        'classId': '1512',
        'text': 'Manufacture of luggage, handbags and the like, saddlery and harness of any material',
    },
    '152': {
        'level': '2',
        'classId': '152',
        'text': 'Manufacture of footwear',
    },
    '1520': {
        'level': '3',
        'classId': '1520',
        'text': 'Manufacture of footwear',
    },
    '16': {
        'level': '1',
        'classId': '16',
        'text': 'Manufacture of wood and of products of wood and cork, except furniture; manufacture of articles of straw and plaiting materials',
    },
    '161': {
        'level': '2',
        'classId': '161',
        'text': 'Sawmilling and planing of wood',
    },
    '1610': {
        'level': '3',
        'classId': '1610',
        'text': 'Sawmilling and planing of wood',
    },
    '162': {
        'level': '2',
        'classId': '162',
        'text': 'Manufacture of products of wood, cork, straw and plaiting materials',
    },
    '1621': {
        'level': '3',
        'classId': '1621',
        'text': 'Manufacture of veneer sheets and wood-based panels',
    },
    '1622': {
        'level': '3',
        'classId': '1622',
        'text': 'Manufacture of builders\' carpentry and joinery',
    },
    '1623': {
        'level': '3',
        'classId': '1623',
        'text': 'Manufacture of wooden containers',
    },
    '1629': {
        'level': '3',
        'classId': '1629',
        'text': 'Manufacture of other products of wood; manufacture of articles of cork, straw and plaiting materials',
    },
    '17': {
        'level': '1',
        'classId': '17',
        'text': 'Manufacture of paper and paper products',
    },
    '170': {
        'level': '2',
        'classId': '170',
        'text': 'Manufacture of paper and paper products',
    },
    '1701': {
        'level': '3',
        'classId': '1701',
        'text': 'Manufacture of pulp, paper and paperboard',
    },
    '1702': {
        'level': '3',
        'classId': '1702',
        'text': 'Manufacture of corrugated paper and paperboard and of containers of paper and paperboard',
    },
    '1709': {
        'level': '3',
        'classId': '1709',
        'text': 'Manufacture of other articles of paper and paperboard',
    },
    '18': {
        'level': '1',
        'classId': '18',
        'text': 'Printing and reproduction of recorded media',
    },
    '181': {
        'level': '2',
        'classId': '181',
        'text': 'Printing and service activities related to printing',
    },
    '1811': {
        'level': '3',
        'classId': '1811',
        'text': 'Printing',
    },
    '1812': {
        'level': '3',
        'classId': '1812',
        'text': 'Service activities related to printing',
    },
    '182': {
        'level': '2',
        'classId': '182',
        'text': 'Reproduction of recorded media',
    },
    '1820': {
        'level': '3',
        'classId': '1820',
        'text': 'Reproduction of recorded media',
    },
    '19': {
        'level': '1',
        'classId': '19',
        'text': 'Manufacture of coke and refined petroleum products',
    },
    '191': {
        'level': '2',
        'classId': '191',
        'text': 'Manufacture of coke oven products',
    },
    '1910': {
        'level': '3',
        'classId': '1910',
        'text': 'Manufacture of coke oven products',
    },
    '192': {
        'level': '2',
        'classId': '192',
        'text': 'Manufacture of refined petroleum products; manufacture of fossil fuel products',
    },
    '1920': {
        'level': '3',
        'classId': '1920',
        'text': 'Manufacture of refined petroleum products; manufacture of fossil fuel products',
    },
    '20': {
        'level': '1',
        'classId': '20',
        'text': 'Manufacture of chemicals and chemical products',
    },
    '201': {
        'level': '2',
        'classId': '201',
        'text': 'Manufacture of basic chemicals, fertilizers and nitrogen compounds, plastics and synthetic rubber in primary forms',
    },
    '2011': {
        'level': '3',
        'classId': '2011',
        'text': 'Manufacture of basic chemicals',
    },
    '2012': {
        'level': '3',
        'classId': '2012',
        'text': 'Manufacture of fertilizers and nitrogen compounds',
    },
    '2013': {
        'level': '3',
        'classId': '2013',
        'text': 'Manufacture of plastics and synthetic rubber in primary forms',
    },
    '202': {
        'level': '2',
        'classId': '202',
        'text': 'Manufacture of other chemical products',
    },
    '2021': {
        'level': '3',
        'classId': '2021',
        'text': 'Manufacture of pesticides and other agrochemical products',
    },
    '2022': {
        'level': '3',
        'classId': '2022',
        'text': 'Manufacture of paints, varnishes and similar coatings, printing ink and mastics',
    },
    '2023': {
        'level': '3',
        'classId': '2023',
        'text': 'Manufacture of soap and detergents, cleaning and polishing preparations, perfumes and toilet preparations',
    },
    '2029': {
        'level': '3',
        'classId': '2029',
        'text': 'Manufacture of other chemical products n.e.c.',
    },
    '203': {
        'level': '2',
        'classId': '203',
        'text': 'Manufacture of man-made fibres',
    },
    '2030': {
        'level': '3',
        'classId': '2030',
        'text': 'Manufacture of man-made fibres',
    },
    '21': {
        'level': '1',
        'classId': '21',
        'text': 'Manufacture of basic pharmaceutical products and pharmaceutical preparations',
    },
    '210': {
        'level': '2',
        'classId': '210',
        'text': 'Manufacture of pharmaceuticals, medicinal chemical and botanical products',
    },
    '2100': {
        'level': '3',
        'classId': '2100',
        'text': 'Manufacture of pharmaceuticals, medicinal chemical and botanical products',
    },
    '22': {
        'level': '1',
        'classId': '22',
        'text': 'Manufacture of rubber and plastic products',
    },
    '221': {
        'level': '2',
        'classId': '221',
        'text': 'Manufacture of rubber products',
    },
    '2211': {
        'level': '3',
        'classId': '2211',
        'text': 'Manufacture of rubber tyres and tubes; retreading and rebuilding of rubber tyres',
    },
    '2219': {
        'level': '3',
        'classId': '2219',
        'text': 'Manufacture of other rubber products',
    },
    '222': {
        'level': '2',
        'classId': '222',
        'text': 'Manufacture of plastics products',
    },
    '2220': {
        'level': '3',
        'classId': '2220',
        'text': 'Manufacture of plastics products',
    },
    '23': {
        'level': '1',
        'classId': '23',
        'text': 'Manufacture of other non-metallic mineral products',
    },
    '231': {
        'level': '2',
        'classId': '231',
        'text': 'Manufacture of glass and glass products',
    },
    '2310': {
        'level': '3',
        'classId': '2310',
        'text': 'Manufacture of glass and glass products',
    },
    '239': {
        'level': '2',
        'classId': '239',
        'text': 'Manufacture of non-metallic mineral products n.e.c.',
    },
    '2391': {
        'level': '3',
        'classId': '2391',
        'text': 'Manufacture of refractory products',
    },
    '2392': {
        'level': '3',
        'classId': '2392',
        'text': 'Manufacture of clay building materials',
    },
    '2393': {
        'level': '3',
        'classId': '2393',
        'text': 'Manufacture of other porcelain and ceramic products',
    },
    '2394': {
        'level': '3',
        'classId': '2394',
        'text': 'Manufacture of cement, lime and plaster',
    },
    '2395': {
        'level': '3',
        'classId': '2395',
        'text': 'Manufacture of articles of concrete, cement and plaster',
    },
    '2396': {
        'level': '3',
        'classId': '2396',
        'text': 'Cutting, shaping and finishing of stone',
    },
    '2399': {
        'level': '3',
        'classId': '2399',
        'text': 'Manufacture of other non-metallic mineral products n.e.c.',
    },
    '24': {
        'level': '1',
        'classId': '24',
        'text': 'Manufacture of basic metals',
    },
    '241': {
        'level': '2',
        'classId': '241',
        'text': 'Manufacture of basic iron and steel',
    },
    '2410': {
        'level': '3',
        'classId': '2410',
        'text': 'Manufacture of basic iron and steel',
    },
    '242': {
        'level': '2',
        'classId': '242',
        'text': 'Manufacture of basic precious and other non-ferrous metals',
    },
    '2420': {
        'level': '3',
        'classId': '2420',
        'text': 'Manufacture of basic precious and other non-ferrous metals',
    },
    '243': {
        'level': '2',
        'classId': '243',
        'text': 'Casting of metals',
    },
    '2431': {
        'level': '3',
        'classId': '2431',
        'text': 'Casting of iron and steel',
    },
    '2432': {
        'level': '3',
        'classId': '2432',
        'text': 'Casting of non-ferrous metals',
    },
    '25': {
        'level': '1',
        'classId': '25',
        'text': 'Manufacture of fabricated metal products, except machinery and equipment',
    },
    '251': {
        'level': '2',
        'classId': '251',
        'text': 'Manufacture of structural metal products, tanks, reservoirs and steam generators',
    },
    '2511': {
        'level': '3',
        'classId': '2511',
        'text': 'Manufacture of structural metal products',
    },
    '2512': {
        'level': '3',
        'classId': '2512',
        'text': 'Manufacture of tanks, reservoirs and containers of metal',
    },
    '2513': {
        'level': '3',
        'classId': '2513',
        'text': 'Manufacture of steam generators, except central heating hot water boilers',
    },
    '252': {
        'level': '2',
        'classId': '252',
        'text': 'Manufacture of weapons and ammunition',
    },
    '2520': {
        'level': '3',
        'classId': '2520',
        'text': 'Manufacture of weapons and ammunition',
    },
    '259': {
        'level': '2',
        'classId': '259',
        'text': 'Manufacture of other fabricated metal products; metalworking service activities',
    },
    '2591': {
        'level': '3',
        'classId': '2591',
        'text': 'Forging, pressing, stamping and roll-forming of metal; powder metallurgy',
    },
    '2592': {
        'level': '3',
        'classId': '2592',
        'text': 'Treatment and coating of metals; machining',
    },
    '2593': {
        'level': '3',
        'classId': '2593',
        'text': 'Manufacture of cutlery, hand tools and general hardware',
    },
    '2599': {
        'level': '3',
        'classId': '2599',
        'text': 'Manufacture of other fabricated metal products n.e.c.',
    },
    '26': {
        'level': '1',
        'classId': '26',
        'text': 'Manufacture of computer, electronic and optical products',
    },
    '261': {
        'level': '2',
        'classId': '261',
        'text': 'Manufacture of electronic components and boards',
    },
    '2611': {
        'level': '3',
        'classId': '2611',
        'text': 'Manufacture of solar cells, solar panels and photovoltaic inverters',
    },
    '2619': {
        'level': '3',
        'classId': '2619',
        'text': 'Manufacture of other electronic components and boards',
    },
    '262': {
        'level': '2',
        'classId': '262',
        'text': 'Manufacture of computers and peripheral equipment',
    },
    '2620': {
        'level': '3',
        'classId': '2620',
        'text': 'Manufacture of computers and peripheral equipment',
    },
    '263': {
        'level': '2',
        'classId': '263',
        'text': 'Manufacture of communication equipment',
    },
    '2630': {
        'level': '3',
        'classId': '2630',
        'text': 'Manufacture of communication equipment',
    },
    '264': {
        'level': '2',
        'classId': '264',
        'text': 'Manufacture of consumer electronics',
    },
    '2640': {
        'level': '3',
        'classId': '2640',
        'text': 'Manufacture of consumer electronics',
    },
    '265': {
        'level': '2',
        'classId': '265',
        'text': 'Manufacture of measuring, testing, navigating and control equipment; watches and clocks',
    },
    '2651': {
        'level': '3',
        'classId': '2651',
        'text': 'Manufacture of measuring, testing, navigating and control equipment',
    },
    '2652': {
        'level': '3',
        'classId': '2652',
        'text': 'Manufacture of watches and clocks',
    },
    '266': {
        'level': '2',
        'classId': '266',
        'text': 'Manufacture of irradiation, electromedical and electrotherapeutic equipment',
    },
    '2660': {
        'level': '3',
        'classId': '2660',
        'text': 'Manufacture of irradiation, electromedical and electrotherapeutic equipment',
    },
    '267': {
        'level': '2',
        'classId': '267',
        'text': 'Manufacture of optical instruments and photographic equipment',
    },
    '2670': {
        'level': '3',
        'classId': '2670',
        'text': 'Manufacture of optical instruments and photographic equipment',
    },
    '268': {
        'level': '2',
        'classId': '268',
        'text': 'Manufacture of magnetic and optical media',
    },
    '2680': {
        'level': '3',
        'classId': '2680',
        'text': 'Manufacture of magnetic and optical media',
    },
    '27': {
        'level': '1',
        'classId': '27',
        'text': 'Manufacture of electrical equipment',
    },
    '271': {
        'level': '2',
        'classId': '271',
        'text': 'Manufacture of electric motors, generators, transformers and electricity distribution and control apparatus',
    },
    '2710': {
        'level': '3',
        'classId': '2710',
        'text': 'Manufacture of electric motors, generators, transformers and electricity distribution and control apparatus',
    },
    '272': {
        'level': '2',
        'classId': '272',
        'text': 'Manufacture of batteries and accumulators',
    },
    '2720': {
        'level': '3',
        'classId': '2720',
        'text': 'Manufacture of batteries and accumulators',
    },
    '273': {
        'level': '2',
        'classId': '273',
        'text': 'Manufacture of wiring and wiring devices',
    },
    '2731': {
        'level': '3',
        'classId': '2731',
        'text': 'Manufacture of fibre optic cables',
    },
    '2732': {
        'level': '3',
        'classId': '2732',
        'text': 'Manufacture of other electronic and electric wires and cables',
    },
    '2733': {
        'level': '3',
        'classId': '2733',
        'text': 'Manufacture of wiring devices',
    },
    '274': {
        'level': '2',
        'classId': '274',
        'text': 'Manufacture of lighting equipment',
    },
    '2740': {
        'level': '3',
        'classId': '2740',
        'text': 'Manufacture of lighting equipment',
    },
    '275': {
        'level': '2',
        'classId': '275',
        'text': 'Manufacture of domestic appliances',
    },
    '2750': {
        'level': '3',
        'classId': '2750',
        'text': 'Manufacture of domestic appliances',
    },
    '279': {
        'level': '2',
        'classId': '279',
        'text': 'Manufacture of other electrical equipment',
    },
    '2790': {
        'level': '3',
        'classId': '2790',
        'text': 'Manufacture of other electrical equipment',
    },
    '28': {
        'level': '1',
        'classId': '28',
        'text': 'Manufacture of machinery and equipment n.e.c.',
    },
    '281': {
        'level': '2',
        'classId': '281',
        'text': 'Manufacture of general-purpose machinery',
    },
    '2811': {
        'level': '3',
        'classId': '2811',
        'text': 'Manufacture of engines and turbines, except aircraft, vehicle and cycle engines',
    },
    '2812': {
        'level': '3',
        'classId': '2812',
        'text': 'Manufacture of fluid power equipment',
    },
    '2813': {
        'level': '3',
        'classId': '2813',
        'text': 'Manufacture of other pumps, compressors, taps and valves',
    },
    '2814': {
        'level': '3',
        'classId': '2814',
        'text': 'Manufacture of bearings, gears, gearing and driving elements',
    },
    '2815': {
        'level': '3',
        'classId': '2815',
        'text': 'Manufacture of ovens, furnaces and permanent household heating equipment',
    },
    '2816': {
        'level': '3',
        'classId': '2816',
        'text': 'Manufacture of lifting and handling equipment',
    },
    '2817': {
        'level': '3',
        'classId': '2817',
        'text': 'Manufacture of office machinery and equipment (except computers and peripheral equipment)',
    },
    '2818': {
        'level': '3',
        'classId': '2818',
        'text': 'Manufacture of power-driven hand tools',
    },
    '2819': {
        'level': '3',
        'classId': '2819',
        'text': 'Manufacture of other general-purpose machinery',
    },
    '282': {
        'level': '2',
        'classId': '282',
        'text': 'Manufacture of special-purpose machinery',
    },
    '2821': {
        'level': '3',
        'classId': '2821',
        'text': 'Manufacture of agricultural and forestry machinery',
    },
    '2822': {
        'level': '3',
        'classId': '2822',
        'text': 'Manufacture of metal-forming machinery and machine tools',
    },
    '2823': {
        'level': '3',
        'classId': '2823',
        'text': 'Manufacture of machinery for metallurgy',
    },
    '2824': {
        'level': '3',
        'classId': '2824',
        'text': 'Manufacture of machinery for mining, quarrying and construction',
    },
    '2825': {
        'level': '3',
        'classId': '2825',
        'text': 'Manufacture of machinery for food, beverage and tobacco processing',
    },
    '2826': {
        'level': '3',
        'classId': '2826',
        'text': 'Manufacture of machinery for textile, apparel and leather production',
    },
    '2829': {
        'level': '3',
        'classId': '2829',
        'text': 'Manufacture of other special-purpose machinery',
    },
    '29': {
        'level': '1',
        'classId': '29',
        'text': 'Manufacture of motor vehicles, trailers and semi-trailers',
    },
    '291': {
        'level': '2',
        'classId': '291',
        'text': 'Manufacture of motor vehicles',
    },
    '2910': {
        'level': '3',
        'classId': '2910',
        'text': 'Manufacture of motor vehicles',
    },
    '292': {
        'level': '2',
        'classId': '292',
        'text': 'Manufacture of bodies (coachwork) for motor vehicles; manufacture of trailers and semi-trailers',
    },
    '2920': {
        'level': '3',
        'classId': '2920',
        'text': 'Manufacture of bodies (coachwork) for motor vehicles; manufacture of trailers and semi-trailers',
    },
    '293': {
        'level': '2',
        'classId': '293',
        'text': 'Manufacture of parts and accessories for motor vehicles',
    },
    '2930': {
        'level': '3',
        'classId': '2930',
        'text': 'Manufacture of parts and accessories for motor vehicles',
    },
    '30': {
        'level': '1',
        'classId': '30',
        'text': 'Manufacture of other transport equipment',
    },
    '301': {
        'level': '2',
        'classId': '301',
        'text': 'Building of ships and boats',
    },
    '3011': {
        'level': '3',
        'classId': '3011',
        'text': 'Building of ships and floating structures',
    },
    '3012': {
        'level': '3',
        'classId': '3012',
        'text': 'Building of pleasure and sporting boats',
    },
    '302': {
        'level': '2',
        'classId': '302',
        'text': 'Manufacture of railway locomotives and rolling stock',
    },
    '3020': {
        'level': '3',
        'classId': '3020',
        'text': 'Manufacture of railway locomotives and rolling stock',
    },
    '303': {
        'level': '2',
        'classId': '303',
        'text': 'Manufacture of air and spacecraft and related machinery',
    },
    '3030': {
        'level': '3',
        'classId': '3030',
        'text': 'Manufacture of air and spacecraft and related machinery',
    },
    '304': {
        'level': '2',
        'classId': '304',
        'text': 'Manufacture of military fighting vehicles',
    },
    '3040': {
        'level': '3',
        'classId': '3040',
        'text': 'Manufacture of military fighting vehicles',
    },
    '309': {
        'level': '2',
        'classId': '309',
        'text': 'Manufacture of transport equipment n.e.c.',
    },
    '3091': {
        'level': '3',
        'classId': '3091',
        'text': 'Manufacture of motorcycles',
    },
    '3092': {
        'level': '3',
        'classId': '3092',
        'text': 'Manufacture of bicycles and invalid carriages',
    },
    '3099': {
        'level': '3',
        'classId': '3099',
        'text': 'Manufacture of other transport equipment n.e.c.',
    },
    '31': {
        'level': '1',
        'classId': '31',
        'text': 'Manufacture of furniture',
    },
    '310': {
        'level': '2',
        'classId': '310',
        'text': 'Manufacture of furniture',
    },
    '3101': {
        'level': '3',
        'classId': '3101',
        'text': 'Manufacture of wooden furniture',
    },
    '3102': {
        'level': '3',
        'classId': '3102',
        'text': 'Manufacture of other furniture',
    },
    '32': {
        'level': '1',
        'classId': '32',
        'text': 'Other manufacturing',
    },
    '321': {
        'level': '2',
        'classId': '321',
        'text': 'Manufacture of jewellery, bijouterie and related articles',
    },
    '3211': {
        'level': '3',
        'classId': '3211',
        'text': 'Manufacture of jewellery and related articles',
    },
    '3212': {
        'level': '3',
        'classId': '3212',
        'text': 'Manufacture of imitation jewellery and related articles',
    },
    '322': {
        'level': '2',
        'classId': '322',
        'text': 'Manufacture of musical instruments',
    },
    '3220': {
        'level': '3',
        'classId': '3220',
        'text': 'Manufacture of musical instruments',
    },
    '323': {
        'level': '2',
        'classId': '323',
        'text': 'Manufacture of sports goods',
    },
    '3230': {
        'level': '3',
        'classId': '3230',
        'text': 'Manufacture of sports goods',
    },
    '324': {
        'level': '2',
        'classId': '324',
        'text': 'Manufacture of games and toys',
    },
    '3240': {
        'level': '3',
        'classId': '3240',
        'text': 'Manufacture of games and toys',
    },
    '325': {
        'level': '2',
        'classId': '325',
        'text': 'Manufacture of medical and dental instruments and supplies',
    },
    '3250': {
        'level': '3',
        'classId': '3250',
        'text': 'Manufacture of medical and dental instruments and supplies',
    },
    '329': {
        'level': '2',
        'classId': '329',
        'text': 'Other manufacturing n.e.c.',
    },
    '3290': {
        'level': '3',
        'classId': '3290',
        'text': 'Other manufacturing n.e.c.',
    },
    '33': {
        'level': '1',
        'classId': '33',
        'text': 'Repair, maintenance and installation of machinery and equipment',
    },
    '331': {
        'level': '2',
        'classId': '331',
        'text': 'Repair and maintenance of fabricated metal products, machinery and equipment',
    },
    '3311': {
        'level': '3',
        'classId': '3311',
        'text': 'Repair and maintenance of fabricated metal products',
    },
    '3312': {
        'level': '3',
        'classId': '3312',
        'text': 'Repair and maintenance of machinery',
    },
    '3313': {
        'level': '3',
        'classId': '3313',
        'text': 'Repair and maintenance of electronic and optical equipment',
    },
    '3314': {
        'level': '3',
        'classId': '3314',
        'text': 'Repair and maintenance of electrical equipment',
    },
    '3315': {
        'level': '3',
        'classId': '3315',
        'text': 'Repair and maintenance of transport equipment, except motor vehicles',
    },
    '3319': {
        'level': '3',
        'classId': '3319',
        'text': 'Repair and maintenance of other equipment',
    },
    '332': {
        'level': '2',
        'classId': '332',
        'text': 'Installation of industrial machinery and equipment',
    },
    '3320': {
        'level': '3',
        'classId': '3320',
        'text': 'Installation of industrial machinery and equipment',
    },
    'D': {
        'level': '0',
        'classId': 'D',
        'text': 'Electricity, gas, steam and air conditioning supply',
    },
    '35': {
        'level': '1',
        'classId': '35',
        'text': 'Electricity, gas, steam and air conditioning supply',
    },
    '351': {
        'level': '2',
        'classId': '351',
        'text': 'Electric power generation, transmission and distribution activities',
    },
    '3511': {
        'level': '3',
        'classId': '3511',
        'text': 'Electric power generation activities from non-renewable sources',
    },
    '3512': {
        'level': '3',
        'classId': '3512',
        'text': 'Electric power generation activities from renewable sources',
    },
    '3513': {
        'level': '3',
        'classId': '3513',
        'text': 'Electric power transmission and distribution activities',
    },
    '352': {
        'level': '2',
        'classId': '352',
        'text': 'Manufacture of gas; distribution of gaseous fuels through mains',
    },
    '3520': {
        'level': '3',
        'classId': '3520',
        'text': 'Manufacture of gas; distribution of gaseous fuels through mains',
    },
    '353': {
        'level': '2',
        'classId': '353',
        'text': 'Steam and air conditioning supply',
    },
    '3530': {
        'level': '3',
        'classId': '3530',
        'text': 'Steam and air conditioning supply',
    },
    '354': {
        'level': '2',
        'classId': '354',
        'text': 'Activities of brokers and agents for electric power and natural gas',
    },
    '3540': {
        'level': '3',
        'classId': '3540',
        'text': 'Activities of brokers and agents for electric power and natural gas',
    },
    'E': {
        'level': '0',
        'classId': 'E',
        'text': 'Water supply; sewerage, waste management and remediation activities',
    },
    '36': {
        'level': '1',
        'classId': '36',
        'text': 'Water collection, treatment and supply',
    },
    '360': {
        'level': '2',
        'classId': '360',
        'text': 'Water collection, treatment and supply',
    },
    '3600': {
        'level': '3',
        'classId': '3600',
        'text': 'Water collection, treatment and supply',
    },
    '37': {
        'level': '1',
        'classId': '37',
        'text': 'Sewerage',
    },
    '370': {
        'level': '2',
        'classId': '370',
        'text': 'Sewerage',
    },
    '3700': {
        'level': '3',
        'classId': '3700',
        'text': 'Sewerage',
    },
    '38': {
        'level': '1',
        'classId': '38',
        'text': 'Waste collection, treatment and disposal, and recovery activities',
    },
    '381': {
        'level': '2',
        'classId': '381',
        'text': 'Waste collection activities',
    },
    '3811': {
        'level': '3',
        'classId': '3811',
        'text': 'Collection of non-hazardous waste',
    },
    '3812': {
        'level': '3',
        'classId': '3812',
        'text': 'Collection of hazardous waste',
    },
    '382': {
        'level': '2',
        'classId': '382',
        'text': 'Waste treatment and disposal',
    },
    '3821': {
        'level': '3',
        'classId': '3821',
        'text': 'Treatment and disposal of non-hazardous waste',
    },
    '3822': {
        'level': '3',
        'classId': '3822',
        'text': 'Treatment and disposal of hazardous waste',
    },
    '383': {
        'level': '2',
        'classId': '383',
        'text': 'Materials and other waste recovery',
    },
    '3830': {
        'level': '3',
        'classId': '3830',
        'text': 'Materials and other waste recovery',
    },
    '39': {
        'level': '1',
        'classId': '39',
        'text': 'Remediation and other waste management service activities',
    },
    '390': {
        'level': '2',
        'classId': '390',
        'text': 'Remediation and other waste management service activities',
    },
    '3900': {
        'level': '3',
        'classId': '3900',
        'text': 'Remediation and other waste management service activities',
    },
    'F': {
        'level': '0',
        'classId': 'F',
        'text': 'Construction',
    },
    '41': {
        'level': '1',
        'classId': '41',
        'text': 'Construction of residential and non-residential buildings',
    },
    '410': {
        'level': '2',
        'classId': '410',
        'text': 'Construction of residential and non-residential buildings',
    },
    '4100': {
        'level': '3',
        'classId': '4100',
        'text': 'Construction of residential and non-residential buildings',
    },
    '42': {
        'level': '1',
        'classId': '42',
        'text': 'Civil engineering',
    },
    '421': {
        'level': '2',
        'classId': '421',
        'text': 'Construction of roads and railways',
    },
    '4210': {
        'level': '3',
        'classId': '4210',
        'text': 'Construction of roads and railways',
    },
    '422': {
        'level': '2',
        'classId': '422',
        'text': 'Construction of utility projects',
    },
    '4220': {
        'level': '3',
        'classId': '4220',
        'text': 'Construction of utility projects',
    },
    '429': {
        'level': '2',
        'classId': '429',
        'text': 'Construction of other civil engineering projects',
    },
    '4290': {
        'level': '3',
        'classId': '4290',
        'text': 'Construction of other civil engineering projects',
    },
    '43': {
        'level': '1',
        'classId': '43',
        'text': 'Specialized construction activities',
    },
    '431': {
        'level': '2',
        'classId': '431',
        'text': 'Demolition and site preparation',
    },
    '4311': {
        'level': '3',
        'classId': '4311',
        'text': 'Demolition',
    },
    '4312': {
        'level': '3',
        'classId': '4312',
        'text': 'Site preparation',
    },
    '432': {
        'level': '2',
        'classId': '432',
        'text': 'Electrical, plumbing and other construction installation activities',
    },
    '4321': {
        'level': '3',
        'classId': '4321',
        'text': 'Electrical installation',
    },
    '4322': {
        'level': '3',
        'classId': '4322',
        'text': 'Plumbing, heat and air-conditioning installation',
    },
    '4329': {
        'level': '3',
        'classId': '4329',
        'text': 'Other construction installation',
    },
    '433': {
        'level': '2',
        'classId': '433',
        'text': 'Building completion and finishing',
    },
    '4330': {
        'level': '3',
        'classId': '4330',
        'text': 'Building completion and finishing',
    },
    '434': {
        'level': '2',
        'classId': '434',
        'text': 'Intermediation service activities for specialized construction services',
    },
    '4340': {
        'level': '3',
        'classId': '4340',
        'text': 'Intermediation service activities for specialized construction services',
    },
    '439': {
        'level': '2',
        'classId': '439',
        'text': 'Other specialized construction activities',
    },
    '4390': {
        'level': '3',
        'classId': '4390',
        'text': 'Other specialized construction activities',
    },
    'G': {
        'level': '0',
        'classId': 'G',
        'text': 'Wholesale and retail trade',
    },
    '46': {
        'level': '1',
        'classId': '46',
        'text': 'Wholesale trade',
    },
    '461': {
        'level': '2',
        'classId': '461',
        'text': 'Wholesale on a fee or contract basis',
    },
    '4610': {
        'level': '3',
        'classId': '4610',
        'text': 'Wholesale on a fee or contract basis',
    },
    '462': {
        'level': '2',
        'classId': '462',
        'text': 'Wholesale of agricultural raw materials and live animals',
    },
    '4620': {
        'level': '3',
        'classId': '4620',
        'text': 'Wholesale of agricultural raw materials and live animals',
    },
    '463': {
        'level': '2',
        'classId': '463',
        'text': 'Wholesale of food, beverages and tobacco',
    },
    '4630': {
        'level': '3',
        'classId': '4630',
        'text': 'Wholesale of food, beverages and tobacco',
    },
    '464': {
        'level': '2',
        'classId': '464',
        'text': 'Wholesale of household goods',
    },
    '4641': {
        'level': '3',
        'classId': '4641',
        'text': 'Wholesale of textiles, clothing and footwear',
    },
    '4642': {
        'level': '3',
        'classId': '4642',
        'text': 'Wholesale of household, office and shop furniture, carpets and lighting equipment',
    },
    '4649': {
        'level': '3',
        'classId': '4649',
        'text': 'Wholesale of other household goods',
    },
    '465': {
        'level': '2',
        'classId': '465',
        'text': 'Wholesale of machinery, equipment and supplies',
    },
    '4651': {
        'level': '3',
        'classId': '4651',
        'text': 'Wholesale of computers, computer peripheral equipment and software',
    },
    '4652': {
        'level': '3',
        'classId': '4652',
        'text': 'Wholesale of electronic and telecommunications equipment and parts',
    },
    '4653': {
        'level': '3',
        'classId': '4653',
        'text': 'Wholesale of agricultural machinery, equipment and supplies',
    },
    '4659': {
        'level': '3',
        'classId': '4659',
        'text': 'Wholesale of other machinery and equipment',
    },
    '466': {
        'level': '2',
        'classId': '466',
        'text': 'Wholesale of motor vehicles, motorcycles and related parts and accessories',
    },
    '4661': {
        'level': '3',
        'classId': '4661',
        'text': 'Wholesale of motor vehicles',
    },
    '4662': {
        'level': '3',
        'classId': '4662',
        'text': 'Wholesale of motor vehicle parts and accessories',
    },
    '4663': {
        'level': '3',
        'classId': '4663',
        'text': 'Wholesale of motorcycles, motorcycle parts and accessories',
    },
    '467': {
        'level': '2',
        'classId': '467',
        'text': 'Other specialized wholesale',
    },
    '4671': {
        'level': '3',
        'classId': '4671',
        'text': 'Wholesale of solid, liquid and gaseous fuels and related products',
    },
    '4672': {
        'level': '3',
        'classId': '4672',
        'text': 'Wholesale of metals and metal ores',
    },
    '4673': {
        'level': '3',
        'classId': '4673',
        'text': 'Wholesale of construction materials, hardware, plumbing and heating equipment and supplies',
    },
    '4679': {
        'level': '3',
        'classId': '4679',
        'text': 'Wholesale of chemicals, waste and scrap and other products n.e.c.',
    },
    '469': {
        'level': '2',
        'classId': '469',
        'text': 'Non-specialized wholesale trade',
    },
    '4690': {
        'level': '3',
        'classId': '4690',
        'text': 'Non-specialized wholesale trade',
    },
    '47': {
        'level': '1',
        'classId': '47',
        'text': 'Retail trade',
    },
    '471': {
        'level': '2',
        'classId': '471',
        'text': 'Non-specialized retail sale',
    },
    '4711': {
        'level': '3',
        'classId': '4711',
        'text': 'Non-specialized retail sale with food, beverages or tobacco predominating',
    },
    '4719': {
        'level': '3',
        'classId': '4719',
        'text': 'Other non-specialized retail sale',
    },
    '472': {
        'level': '2',
        'classId': '472',
        'text': 'Retail sale of food, beverages and tobacco',
    },
    '4721': {
        'level': '3',
        'classId': '4721',
        'text': 'Retail sale of food',
    },
    '4722': {
        'level': '3',
        'classId': '4722',
        'text': 'Retail sale of beverages',
    },
    '4723': {
        'level': '3',
        'classId': '4723',
        'text': 'Retail sale of tobacco products',
    },
    '473': {
        'level': '2',
        'classId': '473',
        'text': 'Retail sale of automotive fuel',
    },
    '4730': {
        'level': '3',
        'classId': '4730',
        'text': 'Retail sale of automotive fuel',
    },
    '474': {
        'level': '2',
        'classId': '474',
        'text': 'Retail sale of information and communication equipment',
    },
    '4740': {
        'level': '3',
        'classId': '4740',
        'text': 'Retail sale of information and communication equipment',
    },
    '475': {
        'level': '2',
        'classId': '475',
        'text': 'Retail sale of other household equipment',
    },
    '4751': {
        'level': '3',
        'classId': '4751',
        'text': 'Retail sale of textiles',
    },
    '4752': {
        'level': '3',
        'classId': '4752',
        'text': 'Retail sale of hardware, building materials, paints and glass',
    },
    '4753': {
        'level': '3',
        'classId': '4753',
        'text': 'Retail sale of carpets, rugs, wall and floor coverings',
    },
    '4759': {
        'level': '3',
        'classId': '4759',
        'text': 'Retail sale of electrical household appliances, furniture, lighting equipment and other household articles',
    },
    '476': {
        'level': '2',
        'classId': '476',
        'text': 'Retail sale of cultural and recreational goods',
    },
    '4761': {
        'level': '3',
        'classId': '4761',
        'text': 'Retail sale of books, newspapers, stationery and office supplies',
    },
    '4762': {
        'level': '3',
        'classId': '4762',
        'text': 'Retail sale of sporting equipment',
    },
    '4763': {
        'level': '3',
        'classId': '4763',
        'text': 'Retail sale of games and toys',
    },
    '4769': {
        'level': '3',
        'classId': '4769',
        'text': 'Retail sale of cultural and recreational goods n.e.c.',
    },
    '477': {
        'level': '2',
        'classId': '477',
        'text': 'Retail sale of other goods, except motor vehicles and motorcycles',
    },
    '4771': {
        'level': '3',
        'classId': '4771',
        'text': 'Retail sale of clothing, footwear and leather articles',
    },
    '4772': {
        'level': '3',
        'classId': '4772',
        'text': 'Retail sale of pharmaceutical and medical goods, cosmetic and toilet articles',
    },
    '4773': {
        'level': '3',
        'classId': '4773',
        'text': 'Retail sale of other new goods n.e.c.',
    },
    '4774': {
        'level': '3',
        'classId': '4774',
        'text': 'Retail sale of second-hand goods',
    },
    '478': {
        'level': '2',
        'classId': '478',
        'text': 'Retail sale of motor vehicles, motorcycles and related parts and accessories',
    },
    '4781': {
        'level': '3',
        'classId': '4781',
        'text': 'Retail sale of motor vehicles',
    },
    '4782': {
        'level': '3',
        'classId': '4782',
        'text': 'Retail sale of motor vehicle parts and accessories',
    },
    '4783': {
        'level': '3',
        'classId': '4783',
        'text': 'Retail sale of motorcycles, motorcycles parts and accessories',
    },
    '479': {
        'level': '2',
        'classId': '479',
        'text': 'Intermediation service activities for retail sale',
    },
    '4790': {
        'level': '3',
        'classId': '4790',
        'text': 'Intermediation service activities for retail sale',
    },
    'H': {
        'level': '0',
        'classId': 'H',
        'text': 'Transportation and storage',
    },
    '49': {
        'level': '1',
        'classId': '49',
        'text': 'Land transport and transport via pipelines',
    },
    '491': {
        'level': '2',
        'classId': '491',
        'text': 'Transport via railways',
    },
    '4911': {
        'level': '3',
        'classId': '4911',
        'text': 'Passenger rail transport, interurban',
    },
    '4912': {
        'level': '3',
        'classId': '4912',
        'text': 'Freight rail transport',
    },
    '492': {
        'level': '2',
        'classId': '492',
        'text': 'Other land transport',
    },
    '4921': {
        'level': '3',
        'classId': '4921',
        'text': 'Urban and suburban passenger land transport',
    },
    '4922': {
        'level': '3',
        'classId': '4922',
        'text': 'Other passenger land transport',
    },
    '4923': {
        'level': '3',
        'classId': '4923',
        'text': 'Freight transport by road',
    },
    '493': {
        'level': '2',
        'classId': '493',
        'text': 'Transport via pipeline',
    },
    '4930': {
        'level': '3',
        'classId': '4930',
        'text': 'Transport via pipeline',
    },
    '50': {
        'level': '1',
        'classId': '50',
        'text': 'Water transport',
    },
    '501': {
        'level': '2',
        'classId': '501',
        'text': 'Sea and coastal water transport',
    },
    '5011': {
        'level': '3',
        'classId': '5011',
        'text': 'Sea and coastal passenger water transport',
    },
    '5012': {
        'level': '3',
        'classId': '5012',
        'text': 'Sea and coastal freight water transport',
    },
    '502': {
        'level': '2',
        'classId': '502',
        'text': 'Inland water transport',
    },
    '5021': {
        'level': '3',
        'classId': '5021',
        'text': 'Inland passenger water transport',
    },
    '5022': {
        'level': '3',
        'classId': '5022',
        'text': 'Inland freight water transport',
    },
    '51': {
        'level': '1',
        'classId': '51',
        'text': 'Air transport',
    },
    '511': {
        'level': '2',
        'classId': '511',
        'text': 'Passenger air transport',
    },
    '5110': {
        'level': '3',
        'classId': '5110',
        'text': 'Passenger air transport',
    },
    '512': {
        'level': '2',
        'classId': '512',
        'text': 'Freight air transport',
    },
    '5120': {
        'level': '3',
        'classId': '5120',
        'text': 'Freight air transport',
    },
    '52': {
        'level': '1',
        'classId': '52',
        'text': 'Warehousing and support activities for transportation',
    },
    '521': {
        'level': '2',
        'classId': '521',
        'text': 'Warehousing and storage',
    },
    '5210': {
        'level': '3',
        'classId': '5210',
        'text': 'Warehousing and storage',
    },
    '522': {
        'level': '2',
        'classId': '522',
        'text': 'Support activities for transportation',
    },
    '5221': {
        'level': '3',
        'classId': '5221',
        'text': 'Service activities incidental to land transportation',
    },
    '5222': {
        'level': '3',
        'classId': '5222',
        'text': 'Service activities incidental to water transportation',
    },
    '5223': {
        'level': '3',
        'classId': '5223',
        'text': 'Service activities incidental to air transportation',
    },
    '5224': {
        'level': '3',
        'classId': '5224',
        'text': 'Cargo handling',
    },
    '5229': {
        'level': '3',
        'classId': '5229',
        'text': 'Other support activities for transportation',
    },
    '523': {
        'level': '2',
        'classId': '523',
        'text': 'Intermediation service activities for transportation',
    },
    '5231': {
        'level': '3',
        'classId': '5231',
        'text': 'Intermediation service activities for freight transportation',
    },
    '5232': {
        'level': '3',
        'classId': '5232',
        'text': 'Intermediation service activities for passenger transportation',
    },
    '53': {
        'level': '1',
        'classId': '53',
        'text': 'Postal and courier activities',
    },
    '531': {
        'level': '2',
        'classId': '531',
        'text': 'Postal activities',
    },
    '5310': {
        'level': '3',
        'classId': '5310',
        'text': 'Postal activities',
    },
    '532': {
        'level': '2',
        'classId': '532',
        'text': 'Courier activities',
    },
    '5320': {
        'level': '3',
        'classId': '5320',
        'text': 'Courier activities',
    },
    '533': {
        'level': '2',
        'classId': '533',
        'text': 'Intermediation service activities for postal and courier activities',
    },
    '5330': {
        'level': '3',
        'classId': '5330',
        'text': 'Intermediation service activities for postal and courier activities',
    },
    'I': {
        'level': '0',
        'classId': 'I',
        'text': 'Accommodation and food service activities',
    },
    '55': {
        'level': '1',
        'classId': '55',
        'text': 'Accommodation',
    },
    '551': {
        'level': '2',
        'classId': '551',
        'text': 'Hotels and similar accommodation activities',
    },
    '5510': {
        'level': '3',
        'classId': '5510',
        'text': 'Hotels and similar accommodation activities',
    },
    '552': {
        'level': '2',
        'classId': '552',
        'text': 'Other short term accommodation activities',
    },
    '5520': {
        'level': '3',
        'classId': '5520',
        'text': 'Other short term accommodation activities',
    },
    '553': {
        'level': '2',
        'classId': '553',
        'text': 'Camping grounds, recreational vehicle parks and trailer parks',
    },
    '5530': {
        'level': '3',
        'classId': '5530',
        'text': 'Camping grounds, recreational vehicle parks and trailer parks',
    },
    '554': {
        'level': '2',
        'classId': '554',
        'text': 'Intermediation service activities for accommodation',
    },
    '5540': {
        'level': '3',
        'classId': '5540',
        'text': 'Intermediation service activities for accommodation',
    },
    '559': {
        'level': '2',
        'classId': '559',
        'text': 'Other accommodation n.e.c.',
    },
    '5590': {
        'level': '3',
        'classId': '5590',
        'text': 'Other accommodation n.e.c.',
    },
    '56': {
        'level': '1',
        'classId': '56',
        'text': 'Food and beverage service activities',
    },
    '561': {
        'level': '2',
        'classId': '561',
        'text': 'Restaurants and mobile food service activities',
    },
    '5610': {
        'level': '3',
        'classId': '5610',
        'text': 'Restaurants and mobile food service activities',
    },
    '562': {
        'level': '2',
        'classId': '562',
        'text': 'Event catering and other food service activities',
    },
    '5621': {
        'level': '3',
        'classId': '5621',
        'text': 'Event catering activities',
    },
    '5629': {
        'level': '3',
        'classId': '5629',
        'text': 'Other food service activities',
    },
    '563': {
        'level': '2',
        'classId': '563',
        'text': 'Beverage serving activities',
    },
    '5630': {
        'level': '3',
        'classId': '5630',
        'text': 'Beverage serving activities',
    },
    '564': {
        'level': '2',
        'classId': '564',
        'text': 'Intermediation service activities for food and beverage services activities',
    },
    '5640': {
        'level': '3',
        'classId': '5640',
        'text': 'Intermediation service activities for food and beverage services activities',
    },
    'J': {
        'level': '0',
        'classId': 'J',
        'text': 'Publishing, broadcasting, and content production and distribution activities',
    },
    '58': {
        'level': '1',
        'classId': '58',
        'text': 'Publishing activities',
    },
    '581': {
        'level': '2',
        'classId': '581',
        'text': 'Publishing of books, newspapers, periodicals and other publishing activities',
    },
    '5811': {
        'level': '3',
        'classId': '5811',
        'text': 'Publishing of books',
    },
    '5812': {
        'level': '3',
        'classId': '5812',
        'text': 'Publishing of newspapers',
    },
    '5813': {
        'level': '3',
        'classId': '5813',
        'text': 'Publishing of journals and periodicals',
    },
    '5819': {
        'level': '3',
        'classId': '5819',
        'text': 'Other publishing activities',
    },
    '582': {
        'level': '2',
        'classId': '582',
        'text': 'Software publishing',
    },
    '5821': {
        'level': '3',
        'classId': '5821',
        'text': 'Publishing of video games',
    },
    '5829': {
        'level': '3',
        'classId': '5829',
        'text': 'Other software publishing',
    },
    '59': {
        'level': '1',
        'classId': '59',
        'text': 'Motion picture, video and television programme production, sound recording and music publishing activities',
    },
    '591': {
        'level': '2',
        'classId': '591',
        'text': 'Motion picture, video and television programme activities',
    },
    '5911': {
        'level': '3',
        'classId': '5911',
        'text': 'Motion picture, video and television programme production activities',
    },
    '5912': {
        'level': '3',
        'classId': '5912',
        'text': 'Motion picture, video and television programme post-production activities',
    },
    '5913': {
        'level': '3',
        'classId': '5913',
        'text': 'Motion picture, video and television programme distribution activities',
    },
    '5914': {
        'level': '3',
        'classId': '5914',
        'text': 'Motion picture projection activities',
    },
    '592': {
        'level': '2',
        'classId': '592',
        'text': 'Sound recording and music publishing activities',
    },
    '5920': {
        'level': '3',
        'classId': '5920',
        'text': 'Sound recording and music publishing activities',
    },
    '60': {
        'level': '1',
        'classId': '60',
        'text': 'Programming, broadcasting, news agency and other content distribution activities',
    },
    '601': {
        'level': '2',
        'classId': '601',
        'text': 'Radio broadcasting and audio distribution activities',
    },
    '6010': {
        'level': '3',
        'classId': '6010',
        'text': 'Radio broadcasting and audio distribution activities',
    },
    '602': {
        'level': '2',
        'classId': '602',
        'text': 'Television programming, broadcasting and video distribution activities',
    },
    '6020': {
        'level': '3',
        'classId': '6020',
        'text': 'Television programming, broadcasting and video distribution activities',
    },
    '603': {
        'level': '2',
        'classId': '603',
        'text': 'News agency and other content distribution activities',
    },
    '6031': {
        'level': '3',
        'classId': '6031',
        'text': 'News agency activities',
    },
    '6039': {
        'level': '3',
        'classId': '6039',
        'text': 'Social network sites and other content distribution activities',
    },
    'K': {
        'level': '0',
        'classId': 'K',
        'text': 'Telecommunications, computer programming, consultancy, computing infrastructure, and other information service activities',
    },
    '61': {
        'level': '1',
        'classId': '61',
        'text': 'Telecommunications',
    },
    '611': {
        'level': '2',
        'classId': '611',
        'text': 'Wired, wireless, and satellite telecommunication activities',
    },
    '6110': {
        'level': '3',
        'classId': '6110',
        'text': 'Wired, wireless, and satellite telecommunication activities',
    },
    '612': {
        'level': '2',
        'classId': '612',
        'text': 'Telecommunication reselling activities and intermediation service activities for telecommunication',
    },
    '6120': {
        'level': '3',
        'classId': '6120',
        'text': 'Telecommunication reselling activities and intermediation service activities for telecommunication',
    },
    '619': {
        'level': '2',
        'classId': '619',
        'text': 'Other telecommunication activities',
    },
    '6190': {
        'level': '3',
        'classId': '6190',
        'text': 'Other telecommunication activities',
    },
    '62': {
        'level': '1',
        'classId': '62',
        'text': 'Computer programming, consultancy and related activities',
    },
    '621': {
        'level': '2',
        'classId': '621',
        'text': 'Computer programming activities',
    },
    '6211': {
        'level': '3',
        'classId': '6211',
        'text': 'Development of video games, video game software, and video game software tools',
    },
    '6219': {
        'level': '3',
        'classId': '6219',
        'text': 'Other computer programming activities',
    },
    '622': {
        'level': '2',
        'classId': '622',
        'text': 'Computer consultancy and computer facilities management activities',
    },
    '6220': {
        'level': '3',
        'classId': '6220',
        'text': 'Computer consultancy and computer facilities management activities',
    },
    '629': {
        'level': '2',
        'classId': '629',
        'text': 'Other information technology and computer service activities',
    },
    '6290': {
        'level': '3',
        'classId': '6290',
        'text': 'Other information technology and computer service activities',
    },
    '63': {
        'level': '1',
        'classId': '63',
        'text': 'Computing infrastructure, data processing, hosting, and other information service activities',
    },
    '631': {
        'level': '2',
        'classId': '631',
        'text': 'Computing infrastructure, data processing, hosting and related activities',
    },
    '6310': {
        'level': '3',
        'classId': '6310',
        'text': 'Computing infrastructure, data processing, hosting and related activities',
    },
    '639': {
        'level': '2',
        'classId': '639',
        'text': 'Web search portals activities and other information service activities',
    },
    '6390': {
        'level': '3',
        'classId': '6390',
        'text': 'Web search portals activities and other information service activities',
    },
    'L': {
        'level': '0',
        'classId': 'L',
        'text': 'Financial and insurance activities',
    },
    '64': {
        'level': '1',
        'classId': '64',
        'text': 'Financial service activities, except insurance and pension funding',
    },
    '641': {
        'level': '2',
        'classId': '641',
        'text': 'Monetary intermediation',
    },
    '6411': {
        'level': '3',
        'classId': '6411',
        'text': 'Central banking',
    },
    '6419': {
        'level': '3',
        'classId': '6419',
        'text': 'Other monetary intermediation',
    },
    '642': {
        'level': '2',
        'classId': '642',
        'text': 'Activities of holding companies and financing conduits',
    },
    '6421': {
        'level': '3',
        'classId': '6421',
        'text': 'Activities of holding companies',
    },
    '6422': {
        'level': '3',
        'classId': '6422',
        'text': 'Activities of financing conduits',
    },
    '643': {
        'level': '2',
        'classId': '643',
        'text': 'Activities of trusts, funds and similar financial entities',
    },
    '6431': {
        'level': '3',
        'classId': '6431',
        'text': 'Activities of money market funds',
    },
    '6432': {
        'level': '3',
        'classId': '6432',
        'text': 'Activities of non-money market investments funds',
    },
    '6433': {
        'level': '3',
        'classId': '6433',
        'text': 'Activities of trust, estate and agency accounts',
    },
    '649': {
        'level': '2',
        'classId': '649',
        'text': 'Other financial service activities, except insurance and pension funding activities',
    },
    '6491': {
        'level': '3',
        'classId': '6491',
        'text': 'Financial leasing activities',
    },
    '6492': {
        'level': '3',
        'classId': '6492',
        'text': 'International trade financing activities',
    },
    '6493': {
        'level': '3',
        'classId': '6493',
        'text': 'Factoring activities',
    },
    '6494': {
        'level': '3',
        'classId': '6494',
        'text': 'Securitisation activities',
    },
    '6495': {
        'level': '3',
        'classId': '6495',
        'text': 'Other credit granting activities',
    },
    '6499': {
        'level': '3',
        'classId': '6499',
        'text': 'Other financial service activities n.e.c., except insurance and pension funding activities',
    },
    '65': {
        'level': '1',
        'classId': '65',
        'text': 'Insurance, reinsurance and pension funding, except compulsory social security',
    },
    '651': {
        'level': '2',
        'classId': '651',
        'text': 'Insurance',
    },
    '6511': {
        'level': '3',
        'classId': '6511',
        'text': 'Life insurance',
    },
    '6512': {
        'level': '3',
        'classId': '6512',
        'text': 'Non-life insurance',
    },
    '652': {
        'level': '2',
        'classId': '652',
        'text': 'Reinsurance',
    },
    '6520': {
        'level': '3',
        'classId': '6520',
        'text': 'Reinsurance',
    },
    '653': {
        'level': '2',
        'classId': '653',
        'text': 'Pension funding',
    },
    '6530': {
        'level': '3',
        'classId': '6530',
        'text': 'Pension funding',
    },
    '66': {
        'level': '1',
        'classId': '66',
        'text': 'Activities auxiliary to financial service and insurance activities',
    },
    '661': {
        'level': '2',
        'classId': '661',
        'text': 'Activities auxiliary to financial services, except insurance and pension funding',
    },
    '6611': {
        'level': '3',
        'classId': '6611',
        'text': 'Administration of financial markets',
    },
    '6612': {
        'level': '3',
        'classId': '6612',
        'text': 'Security and commodity contracts brokerage',
    },
    '6619': {
        'level': '3',
        'classId': '6619',
        'text': 'Other activities auxiliary to financial service activities, except insurance and pension funding',
    },
    '662': {
        'level': '2',
        'classId': '662',
        'text': 'Activities auxiliary to insurance and pension funding',
    },
    '6621': {
        'level': '3',
        'classId': '6621',
        'text': 'Risk and damage evaluation',
    },
    '6622': {
        'level': '3',
        'classId': '6622',
        'text': 'Activities of insurance agents and brokers',
    },
    '6629': {
        'level': '3',
        'classId': '6629',
        'text': 'Other activities auxiliary to insurance and pension funding',
    },
    '663': {
        'level': '2',
        'classId': '663',
        'text': 'Fund management activities',
    },
    '6630': {
        'level': '3',
        'classId': '6630',
        'text': 'Fund management activities',
    },
    'M': {
        'level': '0',
        'classId': 'M',
        'text': 'Real estate activities',
    },
    '68': {
        'level': '1',
        'classId': '68',
        'text': 'Real estate activities',
    },
    '681': {
        'level': '2',
        'classId': '681',
        'text': 'Real estate activities with own or leased property',
    },
    '6810': {
        'level': '3',
        'classId': '6810',
        'text': 'Real estate activities with own or leased property',
    },
    '682': {
        'level': '2',
        'classId': '682',
        'text': 'Real estate activities on a fee or contract basis',
    },
    '6821': {
        'level': '3',
        'classId': '6821',
        'text': 'Intermediation service activities for real estate',
    },
    '6829': {
        'level': '3',
        'classId': '6829',
        'text': 'Other real estate activities on a fee or contract basis',
    },
    'N': {
        'level': '0',
        'classId': 'N',
        'text': 'Professional, scientific and technical activities',
    },
    '69': {
        'level': '1',
        'classId': '69',
        'text': 'Legal and accounting activities',
    },
    '691': {
        'level': '2',
        'classId': '691',
        'text': 'Legal activities',
    },
    '6910': {
        'level': '3',
        'classId': '6910',
        'text': 'Legal activities',
    },
    '692': {
        'level': '2',
        'classId': '692',
        'text': 'Accounting, bookkeeping and auditing activities; tax consultancy',
    },
    '6920': {
        'level': '3',
        'classId': '6920',
        'text': 'Accounting, bookkeeping and auditing activities; tax consultancy',
    },
    '70': {
        'level': '1',
        'classId': '70',
        'text': 'Activities of head offices; management consultancy activities',
    },
    '701': {
        'level': '2',
        'classId': '701',
        'text': 'Activities of head offices',
    },
    '7010': {
        'level': '3',
        'classId': '7010',
        'text': 'Activities of head offices',
    },
    '702': {
        'level': '2',
        'classId': '702',
        'text': 'Business and other management consultancy activities',
    },
    '7020': {
        'level': '3',
        'classId': '7020',
        'text': 'Business and other management consultancy activities',
    },
    '71': {
        'level': '1',
        'classId': '71',
        'text': 'Architectural and engineering activities; technical testing and analysis',
    },
    '711': {
        'level': '2',
        'classId': '711',
        'text': 'Architectural and engineering, and related technical consultancy activities',
    },
    '7110': {
        'level': '3',
        'classId': '7110',
        'text': 'Architectural and engineering, and related technical consultancy activities',
    },
    '712': {
        'level': '2',
        'classId': '712',
        'text': 'Technical testing and analysis',
    },
    '7120': {
        'level': '3',
        'classId': '7120',
        'text': 'Technical testing and analysis',
    },
    '72': {
        'level': '1',
        'classId': '72',
        'text': 'Scientific research and development',
    },
    '721': {
        'level': '2',
        'classId': '721',
        'text': 'Research and experimental development on natural sciences and engineering',
    },
    '7210': {
        'level': '3',
        'classId': '7210',
        'text': 'Research and experimental development on natural sciences and engineering',
    },
    '722': {
        'level': '2',
        'classId': '722',
        'text': 'Research and experimental development on social sciences and humanities',
    },
    '7220': {
        'level': '3',
        'classId': '7220',
        'text': 'Research and experimental development on social sciences and humanities',
    },
    '73': {
        'level': '1',
        'classId': '73',
        'text': 'Activities of advertising, market research and public relations',
    },
    '731': {
        'level': '2',
        'classId': '731',
        'text': 'Advertising activities',
    },
    '7310': {
        'level': '3',
        'classId': '7310',
        'text': 'Advertising activities',
    },
    '732': {
        'level': '2',
        'classId': '732',
        'text': 'Market research and public opinion polling activities',
    },
    '7320': {
        'level': '3',
        'classId': '7320',
        'text': 'Market research and public opinion polling activities',
    },
    '733': {
        'level': '2',
        'classId': '733',
        'text': 'Public relations activities',
    },
    '7330': {
        'level': '3',
        'classId': '7330',
        'text': 'Public relations activities',
    },
    '74': {
        'level': '1',
        'classId': '74',
        'text': 'Other professional, scientific and technical activities',
    },
    '741': {
        'level': '2',
        'classId': '741',
        'text': 'Specialized design activities',
    },
    '7410': {
        'level': '3',
        'classId': '7410',
        'text': 'Specialized design activities',
    },
    '742': {
        'level': '2',
        'classId': '742',
        'text': 'Photographic activities',
    },
    '7420': {
        'level': '3',
        'classId': '7420',
        'text': 'Photographic activities',
    },
    '743': {
        'level': '2',
        'classId': '743',
        'text': 'Translation and interpretation activities',
    },
    '7430': {
        'level': '3',
        'classId': '7430',
        'text': 'Translation and interpretation activities',
    },
    '749': {
        'level': '2',
        'classId': '749',
        'text': 'Other professional, scientific and technical activities n.e.c.',
    },
    '7491': {
        'level': '3',
        'classId': '7491',
        'text': 'Patent brokering and marketing service activities',
    },
    '7499': {
        'level': '3',
        'classId': '7499',
        'text': 'All other professional, scientific and technical activities n.e.c.',
    },
    '75': {
        'level': '1',
        'classId': '75',
        'text': 'Veterinary activities',
    },
    '750': {
        'level': '2',
        'classId': '750',
        'text': 'Veterinary activities',
    },
    '7500': {
        'level': '3',
        'classId': '7500',
        'text': 'Veterinary activities',
    },
    'O': {
        'level': '0',
        'classId': 'O',
        'text': 'Administrative and support service activities',
    },
    '77': {
        'level': '1',
        'classId': '77',
        'text': 'Rental and leasing activities',
    },
    '771': {
        'level': '2',
        'classId': '771',
        'text': 'Rental and leasing of motor vehicles',
    },
    '7710': {
        'level': '3',
        'classId': '7710',
        'text': 'Rental and leasing of motor vehicles',
    },
    '772': {
        'level': '2',
        'classId': '772',
        'text': 'Rental and leasing of personal and household goods',
    },
    '7721': {
        'level': '3',
        'classId': '7721',
        'text': 'Rental and leasing of recreational and sports goods',
    },
    '7729': {
        'level': '3',
        'classId': '7729',
        'text': 'Rental and leasing of other personal and household goods',
    },
    '773': {
        'level': '2',
        'classId': '773',
        'text': 'Rental and leasing of other machinery, equipment and tangible goods',
    },
    '7730': {
        'level': '3',
        'classId': '7730',
        'text': 'Rental and leasing of other machinery, equipment and tangible goods',
    },
    '774': {
        'level': '2',
        'classId': '774',
        'text': 'Leasing of intellectual property and similar products, except copyrighted works',
    },
    '7740': {
        'level': '3',
        'classId': '7740',
        'text': 'Leasing of intellectual property and similar products, except copyrighted works',
    },
    '775': {
        'level': '2',
        'classId': '775',
        'text': 'Intermediation service activities for rental and leasing of tangible goods and non-financial intangible assets',
    },
    '7751': {
        'level': '3',
        'classId': '7751',
        'text': 'Intermediation service activities for rental and leasing of cars, motorhomes and trailers',
    },
    '7752': {
        'level': '3',
        'classId': '7752',
        'text': 'Intermediation service activities for rental and leasing of other tangible goods and non-financial intangible assets',
    },
    '78': {
        'level': '1',
        'classId': '78',
        'text': 'Employment activities',
    },
    '781': {
        'level': '2',
        'classId': '781',
        'text': 'Activities of employment placement agencies',
    },
    '7810': {
        'level': '3',
        'classId': '7810',
        'text': 'Activities of employment placement agencies',
    },
    '782': {
        'level': '2',
        'classId': '782',
        'text': 'Temporary employment agency activities and other human resource provisions',
    },
    '7820': {
        'level': '3',
        'classId': '7820',
        'text': 'Temporary employment agency activities and other human resource provisions',
    },
    '79': {
        'level': '1',
        'classId': '79',
        'text': 'Travel agency, tour operator, and other travel related activities',
    },
    '791': {
        'level': '2',
        'classId': '791',
        'text': 'Travel agency and tour operator activities',
    },
    '7911': {
        'level': '3',
        'classId': '7911',
        'text': 'Travel agency activities',
    },
    '7912': {
        'level': '3',
        'classId': '7912',
        'text': 'Tour operator activities',
    },
    '799': {
        'level': '2',
        'classId': '799',
        'text': 'Other travel related activities',
    },
    '7990': {
        'level': '3',
        'classId': '7990',
        'text': 'Other travel related activities',
    },
    '80': {
        'level': '1',
        'classId': '80',
        'text': 'Investigation and security activities',
    },
    '801': {
        'level': '2',
        'classId': '801',
        'text': 'Investigation and security activities',
    },
    '8011': {
        'level': '3',
        'classId': '8011',
        'text': 'Investigation and private security activities',
    },
    '8019': {
        'level': '3',
        'classId': '8019',
        'text': 'Security activities n.e.c.',
    },
    '81': {
        'level': '1',
        'classId': '81',
        'text': 'Services to buildings and landscape activities',
    },
    '811': {
        'level': '2',
        'classId': '811',
        'text': 'Combined facilities support activities',
    },
    '8110': {
        'level': '3',
        'classId': '8110',
        'text': 'Combined facilities support activities',
    },
    '812': {
        'level': '2',
        'classId': '812',
        'text': 'Cleaning activities',
    },
    '8121': {
        'level': '3',
        'classId': '8121',
        'text': 'General cleaning of buildings',
    },
    '8129': {
        'level': '3',
        'classId': '8129',
        'text': 'Other cleaning activities',
    },
    '813': {
        'level': '2',
        'classId': '813',
        'text': 'Landscape service activities',
    },
    '8130': {
        'level': '3',
        'classId': '8130',
        'text': 'Landscape service activities',
    },
    '82': {
        'level': '1',
        'classId': '82',
        'text': 'Office administrative, office support and other business support activities',
    },
    '821': {
        'level': '2',
        'classId': '821',
        'text': 'Office administrative and support activities',
    },
    '8210': {
        'level': '3',
        'classId': '8210',
        'text': 'Office administrative and support activities',
    },
    '822': {
        'level': '2',
        'classId': '822',
        'text': 'Activities of call centres',
    },
    '8220': {
        'level': '3',
        'classId': '8220',
        'text': 'Activities of call centres',
    },
    '823': {
        'level': '2',
        'classId': '823',
        'text': 'Organization of conventions and trade shows',
    },
    '8230': {
        'level': '3',
        'classId': '8230',
        'text': 'Organization of conventions and trade shows',
    },
    '824': {
        'level': '2',
        'classId': '824',
        'text': 'Intermediation service activities for business support activities n.e.c., except financial intermediation',
    },
    '8240': {
        'level': '3',
        'classId': '8240',
        'text': 'Intermediation service activities for business support activities n.e.c., except financial intermediation',
    },
    '829': {
        'level': '2',
        'classId': '829',
        'text': 'Business support service activities n.e.c.',
    },
    '8291': {
        'level': '3',
        'classId': '8291',
        'text': 'Activities of collection agencies and credit bureaus',
    },
    '8292': {
        'level': '3',
        'classId': '8292',
        'text': 'Packaging activities',
    },
    '8299': {
        'level': '3',
        'classId': '8299',
        'text': 'Other business support service activities n.e.c.',
    },
    'P': {
        'level': '0',
        'classId': 'P',
        'text': 'Public administration and defence; compulsory social security',
    },
    '84': {
        'level': '1',
        'classId': '84',
        'text': 'Public administration and defence; compulsory social security',
    },
    '841': {
        'level': '2',
        'classId': '841',
        'text': 'Administration of the State and the economic, social and environmental policies of the community',
    },
    '8411': {
        'level': '3',
        'classId': '8411',
        'text': 'General public administration activities',
    },
    '8412': {
        'level': '3',
        'classId': '8412',
        'text': 'Regulation of the activities of providing health care, education, cultural services and other social services, excluding social security and environment',
    },
    '8413': {
        'level': '3',
        'classId': '8413',
        'text': 'Regulation of the activities of providing environmental services',
    },
    '8414': {
        'level': '3',
        'classId': '8414',
        'text': 'Regulation of and contribution to more efficient operation of businesses',
    },
    '842': {
        'level': '2',
        'classId': '842',
        'text': 'Provision of services to the community as a whole',
    },
    '8421': {
        'level': '3',
        'classId': '8421',
        'text': 'Foreign affairs',
    },
    '8422': {
        'level': '3',
        'classId': '8422',
        'text': 'Defence activities',
    },
    '8423': {
        'level': '3',
        'classId': '8423',
        'text': 'Public order and safety activities',
    },
    '843': {
        'level': '2',
        'classId': '843',
        'text': 'Compulsory social security activities',
    },
    '8430': {
        'level': '3',
        'classId': '8430',
        'text': 'Compulsory social security activities',
    },
    'Q': {
        'level': '0',
        'classId': 'Q',
        'text': 'Education',
    },
    '85': {
        'level': '1',
        'classId': '85',
        'text': 'Education',
    },
    '851': {
        'level': '2',
        'classId': '851',
        'text': 'Pre-primary education',
    },
    '8510': {
        'level': '3',
        'classId': '8510',
        'text': 'Pre-primary education',
    },
    '852': {
        'level': '2',
        'classId': '852',
        'text': 'Primary education',
    },
    '8520': {
        'level': '3',
        'classId': '8520',
        'text': 'Primary education',
    },
    '853': {
        'level': '2',
        'classId': '853',
        'text': 'Secondary and post-secondary non-tertiary education',
    },
    '8531': {
        'level': '3',
        'classId': '8531',
        'text': 'General secondary education',
    },
    '8532': {
        'level': '3',
        'classId': '8532',
        'text': 'Vocational secondary education',
    },
    '8533': {
        'level': '3',
        'classId': '8533',
        'text': 'Post-secondary non-tertiary education',
    },
    '854': {
        'level': '2',
        'classId': '854',
        'text': 'Tertiary education',
    },
    '8540': {
        'level': '3',
        'classId': '8540',
        'text': 'Tertiary education',
    },
    '855': {
        'level': '2',
        'classId': '855',
        'text': 'Other education',
    },
    '8551': {
        'level': '3',
        'classId': '8551',
        'text': 'Sports and recreation education',
    },
    '8552': {
        'level': '3',
        'classId': '8552',
        'text': 'Cultural education',
    },
    '8553': {
        'level': '3',
        'classId': '8553',
        'text': 'Driving school activities',
    },
    '8559': {
        'level': '3',
        'classId': '8559',
        'text': 'Other education n.e.c.',
    },
    '856': {
        'level': '2',
        'classId': '856',
        'text': 'Educational support activities',
    },
    '8561': {
        'level': '3',
        'classId': '8561',
        'text': 'Intermediation service activities for courses and tutors',
    },
    '8569': {
        'level': '3',
        'classId': '8569',
        'text': 'Other educational support activities',
    },
    'R': {
        'level': '0',
        'classId': 'R',
        'text': 'Human health and social work activities',
    },
    '86': {
        'level': '1',
        'classId': '86',
        'text': 'Human health activities',
    },
    '861': {
        'level': '2',
        'classId': '861',
        'text': 'Hospital activities',
    },
    '8610': {
        'level': '3',
        'classId': '8610',
        'text': 'Hospital activities',
    },
    '862': {
        'level': '2',
        'classId': '862',
        'text': 'Medical and dental practice activities',
    },
    '8620': {
        'level': '3',
        'classId': '8620',
        'text': 'Medical and dental practice activities',
    },
    '869': {
        'level': '2',
        'classId': '869',
        'text': 'Other human health activities',
    },
    '8691': {
        'level': '3',
        'classId': '8691',
        'text': 'Intermediation service activities for medical, dental, and other human health services',
    },
    '8699': {
        'level': '3',
        'classId': '8699',
        'text': 'Other human health activities n.e.c',
    },
    '87': {
        'level': '1',
        'classId': '87',
        'text': 'Residential care activities',
    },
    '871': {
        'level': '2',
        'classId': '871',
        'text': 'Residential nursing care activities',
    },
    '8710': {
        'level': '3',
        'classId': '8710',
        'text': 'Residential nursing care activities',
    },
    '872': {
        'level': '2',
        'classId': '872',
        'text': 'Residential care activities for persons living with or having a diagnosis of a mental illness or substance abuse',
    },
    '8720': {
        'level': '3',
        'classId': '8720',
        'text': 'Residential care activities for persons living with or having a diagnosis of a mental illness or substance abuse',
    },
    '873': {
        'level': '2',
        'classId': '873',
        'text': 'Residential care activities for older persons or persons with physical disabilities',
    },
    '8730': {
        'level': '3',
        'classId': '8730',
        'text': 'Residential care activities for older persons or persons with physical disabilities',
    },
    '879': {
        'level': '2',
        'classId': '879',
        'text': 'Other residential care activities',
    },
    '8791': {
        'level': '3',
        'classId': '8791',
        'text': 'Intermediation service activities for residential care activities',
    },
    '8799': {
        'level': '3',
        'classId': '8799',
        'text': 'Other residential care activities n.e.c.',
    },
    '88': {
        'level': '1',
        'classId': '88',
        'text': 'Social work activities without accommodation',
    },
    '881': {
        'level': '2',
        'classId': '881',
        'text': 'Social work activities without accommodation for older persons or persons with disabilities',
    },
    '8810': {
        'level': '3',
        'classId': '8810',
        'text': 'Social work activities without accommodation for older persons or persons with disabilities',
    },
    '889': {
        'level': '2',
        'classId': '889',
        'text': 'Other social work activities without accommodation',
    },
    '8890': {
        'level': '3',
        'classId': '8890',
        'text': 'Other social work activities without accommodation',
    },
    'S': {
        'level': '0',
        'classId': 'S',
        'text': 'Arts, sports and recreation',
    },
    '90': {
        'level': '1',
        'classId': '90',
        'text': 'Arts creation and performing arts activities',
    },
    '901': {
        'level': '2',
        'classId': '901',
        'text': 'Arts creation activities',
    },
    '9011': {
        'level': '3',
        'classId': '9011',
        'text': 'Literary creation and musical composition activities',
    },
    '9012': {
        'level': '3',
        'classId': '9012',
        'text': 'Visual arts creation activities',
    },
    '9013': {
        'level': '3',
        'classId': '9013',
        'text': 'Other arts creation activities',
    },
    '902': {
        'level': '2',
        'classId': '902',
        'text': 'Activities of performing arts',
    },
    '9020': {
        'level': '3',
        'classId': '9020',
        'text': 'Activities of performing arts',
    },
    '903': {
        'level': '2',
        'classId': '903',
        'text': 'Support activities to arts creation and performing arts',
    },
    '9031': {
        'level': '3',
        'classId': '9031',
        'text': 'Operation of arts facilities and sites',
    },
    '9039': {
        'level': '3',
        'classId': '9039',
        'text': 'Other support activities to arts creation and performing arts',
    },
    '91': {
        'level': '1',
        'classId': '91',
        'text': 'Library, archives, museum and other cultural activities',
    },
    '911': {
        'level': '2',
        'classId': '911',
        'text': 'Library and archive activities',
    },
    '9111': {
        'level': '3',
        'classId': '9111',
        'text': 'Library activities',
    },
    '9112': {
        'level': '3',
        'classId': '9112',
        'text': 'Archive activities',
    },
    '912': {
        'level': '2',
        'classId': '912',
        'text': 'Museum, collection, historical site and monument activities',
    },
    '9121': {
        'level': '3',
        'classId': '9121',
        'text': 'Museum and collection activities',
    },
    '9122': {
        'level': '3',
        'classId': '9122',
        'text': 'Historical site and monument activities',
    },
    '913': {
        'level': '2',
        'classId': '913',
        'text': 'Conservation, restoration and other support activities for cultural heritage',
    },
    '9130': {
        'level': '3',
        'classId': '9130',
        'text': 'Conservation, restoration and other support activities for cultural heritage',
    },
    '914': {
        'level': '2',
        'classId': '914',
        'text': 'Botanical and zoological garden and nature reserve activities',
    },
    '9141': {
        'level': '3',
        'classId': '9141',
        'text': 'Botanical and zoological garden activities',
    },
    '9142': {
        'level': '3',
        'classId': '9142',
        'text': 'Nature reserve activities',
    },
    '92': {
        'level': '1',
        'classId': '92',
        'text': 'Gambling and betting activities',
    },
    '920': {
        'level': '2',
        'classId': '920',
        'text': 'Gambling and betting activities',
    },
    '9200': {
        'level': '3',
        'classId': '9200',
        'text': 'Gambling and betting activities',
    },
    '93': {
        'level': '1',
        'classId': '93',
        'text': 'Sports activities and amusement and recreation activities',
    },
    '931': {
        'level': '2',
        'classId': '931',
        'text': 'Sports activities',
    },
    '9311': {
        'level': '3',
        'classId': '9311',
        'text': 'Operation of sports facilities',
    },
    '9312': {
        'level': '3',
        'classId': '9312',
        'text': 'Activities of sports clubs',
    },
    '9319': {
        'level': '3',
        'classId': '9319',
        'text': 'Other sports activities',
    },
    '932': {
        'level': '2',
        'classId': '932',
        'text': 'Amusement and recreation activities',
    },
    '9321': {
        'level': '3',
        'classId': '9321',
        'text': 'Activities of amusement parks and theme parks',
    },
    '9329': {
        'level': '3',
        'classId': '9329',
        'text': 'Other amusement and recreation activities',
    },
    'T': {
        'level': '0',
        'classId': 'T',
        'text': 'Other service activities',
    },
    '94': {
        'level': '1',
        'classId': '94',
        'text': 'Activities of membership organizations',
    },
    '941': {
        'level': '2',
        'classId': '941',
        'text': 'Activities of business, employers and professional membership organizations',
    },
    '9411': {
        'level': '3',
        'classId': '9411',
        'text': 'Activities of business and employers membership organizations',
    },
    '9412': {
        'level': '3',
        'classId': '9412',
        'text': 'Activities of professional membership organizations',
    },
    '942': {
        'level': '2',
        'classId': '942',
        'text': 'Activities of trade unions',
    },
    '9420': {
        'level': '3',
        'classId': '9420',
        'text': 'Activities of trade unions',
    },
    '949': {
        'level': '2',
        'classId': '949',
        'text': 'Activities of other membership organizations',
    },
    '9491': {
        'level': '3',
        'classId': '9491',
        'text': 'Activities of religious organizations',
    },
    '9492': {
        'level': '3',
        'classId': '9492',
        'text': 'Activities of political organizations',
    },
    '9499': {
        'level': '3',
        'classId': '9499',
        'text': 'Activities of other membership organizations n.e.c.',
    },
    '95': {
        'level': '1',
        'classId': '95',
        'text': 'Repair and maintenance of computers, personal and household goods, and motor vehicles and motorcycles',
    },
    '951': {
        'level': '2',
        'classId': '951',
        'text': 'Repair and maintenance of computers and communication equipment',
    },
    '9510': {
        'level': '3',
        'classId': '9510',
        'text': 'Repair and maintenance of computers and communication equipment',
    },
    '952': {
        'level': '2',
        'classId': '952',
        'text': 'Repair and maintenance of personal and household goods',
    },
    '9521': {
        'level': '3',
        'classId': '9521',
        'text': 'Repair and maintenance of consumer electronics',
    },
    '9522': {
        'level': '3',
        'classId': '9522',
        'text': 'Repair and maintenance of household appliances and home and garden equipment',
    },
    '9523': {
        'level': '3',
        'classId': '9523',
        'text': 'Repair and maintenance of footwear and leather goods',
    },
    '9524': {
        'level': '3',
        'classId': '9524',
        'text': 'Repair and maintenance of furniture and home furnishings',
    },
    '9529': {
        'level': '3',
        'classId': '9529',
        'text': 'Repair and maintenance of other personal and household goods',
    },
    '953': {
        'level': '2',
        'classId': '953',
        'text': 'Repair and maintenance of motor vehicles and motorcycles',
    },
    '9531': {
        'level': '3',
        'classId': '9531',
        'text': 'Repair and maintenance of motor vehicles',
    },
    '9532': {
        'level': '3',
        'classId': '9532',
        'text': 'Repair and maintenance of motorcycles',
    },
    '954': {
        'level': '2',
        'classId': '954',
        'text': 'Intermediation service activities for repair and maintenance of computers, personal and household goods, and motor vehicles and motorcycles',
    },
    '9540': {
        'level': '3',
        'classId': '9540',
        'text': 'Intermediation service activities for repair and maintenance of computers, personal and household goods, and motor vehicles and motorcycles',
    },
    '96': {
        'level': '1',
        'classId': '96',
        'text': 'Personal service activities',
    },
    '961': {
        'level': '2',
        'classId': '961',
        'text': 'Washing and cleaning of textile and fur products',
    },
    '9610': {
        'level': '3',
        'classId': '9610',
        'text': 'Washing and cleaning of textile and fur products',
    },
    '962': {
        'level': '2',
        'classId': '962',
        'text': 'Hairdressing, beauty treatment, day spa and similar activities',
    },
    '9621': {
        'level': '3',
        'classId': '9621',
        'text': 'Hairdressing and barber activities',
    },
    '9622': {
        'level': '3',
        'classId': '9622',
        'text': 'Beauty care and other beauty treatment activities',
    },
    '9623': {
        'level': '3',
        'classId': '9623',
        'text': 'Day spa, sauna and steam bath activities',
    },
    '963': {
        'level': '2',
        'classId': '963',
        'text': 'Funeral and related activities',
    },
    '9630': {
        'level': '3',
        'classId': '9630',
        'text': 'Funeral and related activities',
    },
    '964': {
        'level': '2',
        'classId': '964',
        'text': 'Intermediation service activities for personal services',
    },
    '9640': {
        'level': '3',
        'classId': '9640',
        'text': 'Intermediation service activities for personal services',
    },
    '969': {
        'level': '2',
        'classId': '969',
        'text': 'Other personal service activities n.e.c.',
    },
    '9690': {
        'level': '3',
        'classId': '9690',
        'text': 'Other personal service activities n.e.c.',
    },
    'U': {
        'level': '0',
        'classId': 'U',
        'text': 'Activities of households as employers; undifferentiated goods- and services-producing activities of households for own use',
    },
    '97': {
        'level': '1',
        'classId': '97',
        'text': 'Activities of households as employers of domestic personnel',
    },
    '970': {
        'level': '2',
        'classId': '970',
        'text': 'Activities of households as employers of domestic personnel',
    },
    '9700': {
        'level': '3',
        'classId': '9700',
        'text': 'Activities of households as employers of domestic personnel',
    },
    '98': {
        'level': '1',
        'classId': '98',
        'text': 'Undifferentiated goods- and services-producing activities of private households for own use',
    },
    '981': {
        'level': '2',
        'classId': '981',
        'text': 'Undifferentiated goods-producing activities of private households for own use',
    },
    '9810': {
        'level': '3',
        'classId': '9810',
        'text': 'Undifferentiated goods-producing activities of private households for own use',
    },
    '982': {
        'level': '2',
        'classId': '982',
        'text': 'Undifferentiated service-producing activities of private households for own use',
    },
    '9820': {
        'level': '3',
        'classId': '9820',
        'text': 'Undifferentiated service-producing activities of private households for own use',
    },
    'V': {
        'level': '0',
        'classId': 'V',
        'text': 'Activities of extraterritorial organizations and bodies',
    },
    '99': {
        'level': '1',
        'classId': '99',
        'text': 'Activities of extraterritorial organizations and bodies',
    },
    '990': {
        'level': '2',
        'classId': '990',
        'text': 'Activities of extraterritorial organizations and bodies',
    },
    '9900': {
        'level': '3',
        'classId': '9900',
        'text': 'Activities of extraterritorial organizations and bodies',
    },
}


__all__ = ['Processes', 'TidasProcessesText', 'ProcessesCategoryData', 'PROCESSES_CATEGORIES']
