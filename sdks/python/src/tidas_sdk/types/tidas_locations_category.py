"""
Locations classification categories.

Clean implementation using Literal types (matches TypeScript SDK pattern).
DO NOT auto-generate - regenerate using generate_category_types.py
"""

from typing import Literal, TypedDict


class LocationsCategoryData(TypedDict):
    """Locations category metadata."""

    level: Literal['0']
    classId: str
    text: str


# Type-safe union of all locations category IDs
Locations = Literal[
    'NULL',  # None
    'GLO',  # Global
    'RAF',  # Africa
    'RAM',  # Americas
    'RAS',  # Asia and Pacific
    'RER',  # Europe
    'OCE',  # Oceania
    'MEA',  # Middle East and North Africa
    'AFR',  # Sub-Saharan Africa
    'RLA',  # Latin America & the Caribbean
    'RNA',  # Northern America
    'CPA',  # Centrally Planned Asia and China
    'EAS',  # Eastern Asia
    'PAS',  # Other Pacific Asia
    'SAS',  # South Asia
    'EEU',  # Central and Eastern Europe
    'WEU',  # Western Europe
    'RNE',  # Near East
    'RME',  # Middle East
    'EU-15',  # EU 15
    'EU-NMC',  # EU New Member Countries 2004
    'EU-25',  # EU 25
    'EC-CC',  # EU Candidate Countries 2005
    'EU-25&CC',  # EU 25 Plus Candidate Countries 2005
    'EU-AC',  # EU Associated Countries 2005
    'EU-25&CC&AC',  # EU 25 Plus Candidate Countries and Associated Countries 2005
    'EU-27',  # EU 27
    'PAO',  # Pacific OECD (Japan, Australia, New Zealand)
    'FSU',  # Independent States of the Former Soviet Union
    'UCTE',  # Union for the Co-ordination of Transmission of Electricity
    'CENTREL',  # Central european power association
    'NORDEL',  # Nordic countries power association
    'EU+EFTA+UK',  # complete EU
    'AD',  # Andorra
    'AE',  # United Arab Emirates
    'AF',  # Afghanistan
    'AG',  # Antigua and Barbuda
    'AI',  # Anguilla
    'AL',  # Albania
    'AM',  # Armenia
    'AO',  # Angola
    'AQ',  # Antarctica
    'AR',  # Argentina
    'AS',  # American Samoa
    'AT',  # Austria
    'AU',  # Australia
    'AW',  # Aruba
    'AX',  # Åland Islands
    'AZ',  # Azerbaijan
    'BA',  # Bosnia and Herzegovina
    'BB',  # Barbados
    'BD',  # Bangladesh
    'BE',  # Belgium
    'BF',  # Burkina Faso
    'BG',  # Bulgaria
    'BH',  # Bahrain
    'BI',  # Burundi
    'BJ',  # Benin
    'BL',  # Saint Barthélemy
    'BM',  # Bermuda
    'BN',  # Brunei Darussalam
    'BO',  # Bolivia (Plurinational State of)
    'BQ',  # Bonaire, Sint Eustatius and Saba
    'BR',  # Brazil
    'BS',  # Bahamas
    'BT',  # Bhutan
    'BV',  # Bouvet Island
    'BW',  # Botswana
    'BY',  # Belarus
    'BZ',  # Belize
    'CA',  # Canada
    'CC',  # Cocos (Keeling) Islands
    'CD',  # Congo, Democratic Republic of the
    'CF',  # Central African Republic
    'CG',  # Congo
    'CH',  # Switzerland
    'CI',  # Côte d'Ivoire
    'CK',  # Cook Islands
    'CL',  # Chile
    'CM',  # Cameroon
    'CO',  # Colombia
    'CR',  # Costa Rica
    'CU',  # Cuba
    'CV',  # Cabo Verde
    'CW',  # Curaçao
    'CX',  # Christmas Island
    'CY',  # Cyprus
    'CZ',  # Czechia
    'DE',  # Germany
    'DJ',  # Djibouti
    'DK',  # Denmark
    'DM',  # Dominica
    'DO',  # Dominican Republic
    'DZ',  # Algeria
    'EC',  # Ecuador
    'EE',  # Estonia
    'EG',  # Egypt
    'EH',  # Western Sahara
    'ER',  # Eritrea
    'ES',  # Spain
    'ET',  # Ethiopia
    'FI',  # Finland
    'FJ',  # Fiji
    'FK',  # Falkland Islands (Malvinas)
    'FM',  # Micronesia (Federated States of)
    'FO',  # Faroe Islands
    'FR',  # France
    'GA',  # Gabon
    'GB',  # United Kingdom of Great Britain and Northern Ireland
    'GD',  # Grenada
    'GE',  # Georgia
    'GF',  # French Guiana
    'GG',  # Guernsey
    'GH',  # Ghana
    'GI',  # Gibraltar
    'GL',  # Greenland
    'GM',  # Gambia
    'GN',  # Guinea
    'GP',  # Guadeloupe
    'GQ',  # Equatorial Guinea
    'GR',  # Greece
    'GS',  # South Georgia and the South Sandwich Islands
    'GT',  # Guatemala
    'GU',  # Guam
    'GW',  # Guinea-Bissau
    'GY',  # Guyana
    'HM',  # Heard Island and McDonald Islands
    'HN',  # Honduras
    'HR',  # Croatia
    'HT',  # Haiti
    'HU',  # Hungary
    'ID',  # Indonesia
    'IE',  # Ireland
    'IL',  # Israel
    'IM',  # Isle of Man
    'IN',  # India
    'IO',  # British Indian Ocean Territory
    'IQ',  # Iraq
    'IR',  # Iran (Islamic Republic of)
    'IS',  # Iceland
    'IT',  # Italy
    'JE',  # Jersey
    'JM',  # Jamaica
    'JO',  # Jordan
    'JP',  # Japan
    'KE',  # Kenya
    'KG',  # Kyrgyzstan
    'KH',  # Cambodia
    'KI',  # Kiribati
    'KM',  # Comoros
    'KN',  # Saint Kitts and Nevis
    'KP',  # Korea (Democratic People's Republic of)
    'KR',  # Korea, Republic of
    'KW',  # Kuwait
    'KY',  # Cayman Islands
    'KZ',  # Kazakhstan
    'LA',  # Lao People's Democratic Republic
    'LB',  # Lebanon
    'LC',  # Saint Lucia
    'LI',  # Liechtenstein
    'LK',  # Sri Lanka
    'LR',  # Liberia
    'LS',  # Lesotho
    'LT',  # Lithuania
    'LU',  # Luxembourg
    'LV',  # Latvia
    'LY',  # Libya
    'MA',  # Morocco
    'MC',  # Monaco
    'MD',  # Moldova, Republic of
    'ME',  # Montenegro
    'MF',  # Saint Martin (French part)
    'MG',  # Madagascar
    'MH',  # Marshall Islands
    'MK',  # North Macedonia
    'ML',  # Mali
    'MM',  # Myanmar
    'MN',  # Mongolia
    'MP',  # Northern Mariana Islands
    'MQ',  # Martinique
    'MR',  # Mauritania
    'MS',  # Montserrat
    'MT',  # Malta
    'MU',  # Mauritius
    'MV',  # Maldives
    'MW',  # Malawi
    'MX',  # Mexico
    'MY',  # Malaysia
    'MZ',  # Mozambique
    'NA',  # Namibia
    'NC',  # New Caledonia
    'NE',  # Niger
    'NF',  # Norfolk Island
    'NG',  # Nigeria
    'NI',  # Nicaragua
    'NL',  # Netherlands
    'NO',  # Norway
    'NP',  # Nepal
    'NR',  # Nauru
    'NU',  # Niue
    'NZ',  # New Zealand
    'OM',  # Oman
    'PA',  # Panama
    'PE',  # Peru
    'PF',  # French Polynesia
    'PG',  # Papua New Guinea
    'PH',  # Philippines
    'PK',  # Pakistan
    'PL',  # Poland
    'PM',  # Saint Pierre and Miquelon
    'PN',  # Pitcairn
    'PR',  # Puerto Rico
    'PS',  # Palestine, State of
    'PT',  # Portugal
    'PW',  # Palau
    'PY',  # Paraguay
    'QA',  # Qatar
    'RE',  # Réunion
    'RO',  # Romania
    'RS',  # Serbia
    'RU',  # Russian Federation
    'RW',  # Rwanda
    'SA',  # Saudi Arabia
    'SB',  # Solomon Islands
    'SC',  # Seychelles
    'SD',  # Sudan
    'SE',  # Sweden
    'SG',  # Singapore
    'SH',  # Saint Helena, Ascension and Tristan da Cunha
    'SI',  # Slovenia
    'SJ',  # Svalbard and Jan Mayen
    'SK',  # Slovakia
    'SL',  # Sierra Leone
    'SM',  # San Marino
    'SN',  # Senegal
    'SO',  # Somalia
    'SR',  # Suriname
    'SS',  # South Sudan
    'ST',  # Sao Tome and Principe
    'SV',  # El Salvador
    'SX',  # Sint Maarten (Dutch part)
    'SY',  # Syrian Arab Republic
    'SZ',  # Eswatini
    'TC',  # Turks and Caicos Islands
    'TD',  # Chad
    'TF',  # French Southern Territories
    'TG',  # Togo
    'TH',  # Thailand
    'TJ',  # Tajikistan
    'TK',  # Tokelau
    'TL',  # Timor-Leste
    'TM',  # Turkmenistan
    'TN',  # Tunisia
    'TO',  # Tonga
    'TR',  # Türkiye
    'TT',  # Trinidad and Tobago
    'TV',  # Tuvalu
    'TZ',  # Tanzania, United Republic of
    'UA',  # Ukraine
    'UG',  # Uganda
    'UM',  # United States Minor Outlying Islands
    'US',  # United States of America
    'UY',  # Uruguay
    'UZ',  # Uzbekistan
    'VA',  # Holy See
    'VC',  # Saint Vincent and the Grenadines
    'VE',  # Venezuela (Bolivarian Republic of)
    'VG',  # Virgin Islands (British)
    'VI',  # Virgin Islands (U.S.)
    'VN',  # Viet Nam
    'VU',  # Vanuatu
    'WF',  # Wallis and Futuna
    'WS',  # Samoa
    'YE',  # Yemen
    'YT',  # Mayotte
    'ZA',  # South Africa
    'ZM',  # Zambia
    'ZW',  # Zimbabwe
    'CIS',  # Commonwealth of Independent States
    'CN',  # China
    'CN-BJ',  # Beijing City,China
    'CN-TJ',  # Tianjin City,China
    'CN-HE',  # Hebei Province,China
    'CN-HE-SJW',  # Shijiazhuang City,Hebei Province,China
    'CN-HE-TGS',  # Tangshan City,Hebei Province,China
    'CN-HE-SHP',  # Qinhuangdao City,Hebei Province,China
    'CN-HE-HDS',  # Handan City,Hebei Province,China
    'CN-HE-XTS',  # Xingtai City,Hebei Province,China
    'CN-HE-BDS',  # Baoding City,Hebei Province,China
    'CN-HE-ZJK',  # Zhangjiakou City,Hebei Province,China
    'CN-HE-CDS',  # Chengde City,Hebei Province,China
    'CN-HE-CGZ',  # Cangzhou City,Hebei Province,China
    'CN-HE-LFS',  # Langfang City,Hebei Province,China
    'CN-HE-HGS',  # Hengshui City,Hebei Province,China
    'CN-SX',  # Shanxi Province,China
    'CN-SX-TYN',  # Taiyuan City,Shanxi Province,China
    'CN-SX-DTG',  # Datong City,Shanxi Province,China
    'CN-SX-YQS',  # Yangquan City,Shanxi Province,China
    'CN-SX-CZS',  # Changzhi City,Shanxi Province,China
    'CN-SX-JCG',  # Jincheng City,Shanxi Province,China
    'CN-SX-SZJ',  # Shuozhou City,Shanxi Province,China
    'CN-SX-JZN',  # Jinzhong City,Shanxi Province,China
    'CN-SX-YCE',  # Yuncheng City,Shanxi Province,China
    'CN-SX-XZS',  # Xinzhou City,Shanxi Province,China
    'CN-SX-LFN',  # Linfen City,Shanxi Province,China
    'CN-SX-LLH',  # Lüliang City,Shanxi Province,China
    'CN-NM',  # Inner Mongolia Autonomous Region,China
    'CN-NM-HET',  # Hohhot City,Inner Mongolia Autonomous Region,China
    'CN-NM-BTS',  # Baotou City,Inner Mongolia Autonomous Region,China
    'CN-NM-WHM',  # Wuhai City,Inner Mongolia Autonomous Region,China
    'CN-NM-CFS',  # Chifeng(Ulanhad)City,Inner Mongolia Autonomous Region,China
    'CN-NM-TLO',  # Tongliao City,Inner Mongolia Autonomous Region,China
    'CN-NM-ODS',  # Ordos City,Inner Mongolia Autonomous Region,China
    'CN-NM-HBR',  # Hulun Buir City,Inner Mongolia Autonomous Region,China
    'CN-NM-BYR',  # Bayannur City,Inner Mongolia Autonomous Region,China
    'CN-NM-ULS',  # Ulanqab City,Inner Mongolia Autonomous Region,China
    'CN-NM-HIN',  # Hinggan Meng,Inner Mongolia Autonomous Region,China
    'CN-NM-XGO',  # Xilin Gol Meng,Inner Mongolia Autonomous Region,China
    'CN-NM-ALM',  # Alxa Meng,Inner Mongolia Autonomous Region,China
    'CN-LN',  # Liaoning Province,China
    'CN-LN-SHE',  # Shenyang City,Liaoning Province,China
    'CN-LN-DLC',  # Dalian City,Liaoning Province,China
    'CN-LN-ASN',  # Anshan City,Liaoning Province,China
    'CN-LN-FSN',  # Fushun City,Liaoning Province,China
    'CN-LN-BXS',  # Benxi City,Liaoning Province,China
    'CN-LN-DDG',  # Dandong City,Liaoning Province,China
    'CN-LN-JNZ',  # Jinzhou City,Liaoning Province,China
    'CN-LN-YIK',  # Yingkou City,Liaoning Province,China
    'CN-LN-FXS',  # Fuxin City,Liaoning Province,China
    'CN-LN-LYL',  # Liaoyang City,Liaoning Province,China
    'CN-LN-PJS',  # Panjin City,Liaoning Province,China
    'CN-LN-TLS',  # Tieling City,Liaoning Province,China
    'CN-LN-CYS',  # Chaoyang City,Liaoning Province,China
    'CN-LN-HLD',  # Huludao City,Liaoning Province,China
    'CN-JL',  # Jilin Province,China
    'CN-JL-CGQ',  # Changchun City,Jilin Province,China
    'CN-JL-JLS',  # Jilin City,Jilin Province,China
    'CN-JL-SPS',  # Siping City,Jilin Province,China
    'CN-JL-LYH',  # Liaoyuan City,Jilin Province,China
    'CN-JL-THS',  # Tonghua City,Jilin Province,China
    'CN-JL-BSN',  # Baishan City,Jilin Province,China
    'CN-JL-SYU',  # Songyuan City,Jilin Province,China
    'CN-JL-BCS',  # Baicheng City,Jilin Province,China
    'CN-JL-YBZ',  # Yanbian Korean Autonomous Prefecture,Jilin Province,China
    'CN-HL',  # Heilongjiang Province,China
    'CN-HL-HRB',  # Harbin City,Heilongjiang Province,China
    'CN-HL-NDG',  # Qiqihar City,Heilongjiang Province,China
    'CN-HL-JXI',  # Jixi City,Heilongjiang Province,China
    'CN-HL-HEG',  # Hegang City,Heilongjiang Province,China
    'CN-HL-SYS',  # Shuangyashan City,Heilongjiang Province,China
    'CN-HL-DQG',  # Daqing City,Heilongjiang Province,China
    'CN-HL-YCH',  # Yichun City,Heilongjiang Province,China
    'CN-HL-JMU',  # Jiamusi City,Heilongjiang Province,China
    'CN-HL-QTH',  # Qitaihe City,Heilongjiang Province,China
    'CN-HL-MDG',  # Mudanjiang City,Heilongjiang Province,China
    'CN-HL-HEK',  # Heihe City,Heilongjiang Province,China
    'CN-HL-SUH',  # Suihua City,Heilongjiang Province,China
    'CN-HL-DHL',  # Da Hinggan Ling Diqu,Heilongjiang Province,China
    'CN-SH',  # Shanghai City,China
    'CN-JS',  # Jiangsu Province,China
    'CN-JS-NKG',  # Nanjing City,Jiangsu Province,China
    'CN-JS-WUX',  # Wuxi City,Jiangsu Province,China
    'CN-JS-XUZ',  # Xuzhou City,Jiangsu Province,China
    'CN-JS-CZX',  # Changzhou City,Jiangsu Province,China
    'CN-JS-SZH',  # Suzhou City,Jiangsu Province,China
    'CN-JS-NTG',  # Nantong City,Jiangsu Province,China
    'CN-JS-LYG',  # Lianyungang City,Jiangsu Province,China
    'CN-JS-HAS',  # Huai'an City,Jiangsu Province,China
    'CN-JS-YCK',  # Yancheng City,Jiangsu Province,China
    'CN-JS-YZH',  # Yangzhou City,Jiangsu Province,China
    'CN-JS-ZHE',  # Zhenjiang City,Jiangsu Province,China
    'CN-JS-TZS',  # Taizhou City,Jiangsu Province,China
    'CN-JS-SUQ',  # Suqian City,Jiangsu Province,China
    'CN-ZJ',  # Zhejiang Province,China
    'CN-ZJ-HGH',  # Hangzhou City,Zhejiang Province,China
    'CN-ZJ-NGB',  # Ningbo City,Zhejiang Province,China
    'CN-ZJ-WNZ',  # Wenzhou City,Zhejiang Province,China
    'CN-ZJ-JIX',  # Jiaxing City,Zhejiang Province,China
    'CN-ZJ-HZH',  # Huzhou City,Zhejiang Province,China
    'CN-ZJ-SXG',  # Shaoxing City,Zhejiang Province,China
    'CN-ZJ-JHA',  # Jinhua City,Zhejiang Province,China
    'CN-ZJ-QUZ',  # Quzhou City,Zhejiang Province,China
    'CN-ZJ-ZOS',  # Zhoushan City,Zhejiang Province,China
    'CN-ZJ-TZZ',  # Taizhou City,Zhejiang Province,China
    'CN-ZJ-LSS',  # Lishui City,Zhejiang Province,China
    'CN-AH',  # Anhui Province,China
    'CN-AH-HFE',  # Hefei City,Anhui Province,China
    'CN-AH-WHI',  # Wuhu City,Anhui Province,China
    'CN-AH-BBU',  # Bengbu City,Anhui Province,China
    'CN-AH-HNS',  # Huainan City,Anhui Province,China
    'CN-AH-MAA',  # Ma'anshan City,Anhui Province,China
    'CN-AH-HBE',  # Huaibei City,Anhui Province,China
    'CN-AH-TOL',  # Tongling City,Anhui Province,China
    'CN-AH-AQG',  # Anqing City,Anhui Province,China
    'CN-AH-HSN',  # Huangshan City,Anhui Province,China
    'CN-AH-CUZ',  # Chuzhou City,Anhui Province,China
    'CN-AH-FYS',  # Fuyang City,Anhui Province,China
    'CN-AH-SUZ',  # Suzhou City,Anhui Province,China
    'CN-AH-CAH',  # Chaohu City,Anhui Province,China
    'CN-AH-LAW',  # Lu'an City,Anhui Province,China
    'CN-AH-BOZ',  # Bozhou City,Anhui Province,China
    'CN-AH-CIZ',  # Chizhou City,Anhui Province,China
    'CN-AH-XCI',  # Xuancheng City,Anhui Province,China
    'CN-FJ',  # Fujian Province,China
    'CN-FJ-FOC',  # Fuzhou City,Fujian Province,China
    'CN-FJ-XMN',  # Xiamen City,Fujian Province,China
    'CN-FJ-PUT',  # Putian City,Fujian Province,China
    'CN-FJ-SMS',  # Sanming City,Fujian Province,China
    'CN-FJ-QZJ',  # Quanzhou City,Fujian Province,China
    'CN-FJ-ZZU',  # Zhangzhou City,Fujian Province,China
    'CN-FJ-NPS',  # Nanping City,Fujian Province,China
    'CN-FJ-LYF',  # Longyan City,Fujian Province,China
    'CN-FJ-NDS',  # Ningde City,Fujian Province,China
    'CN-JX',  # Jiangxi Province,China
    'CN-JX-KHN',  # Nanchang City,Jiangxi Province,China
    'CN-JX-JDZ',  # Jingdezhen City,Jiangxi Province,China
    'CN-JX-PXS',  # Pingxiang City,Jiangxi Province,China
    'CN-JX-JIU',  # Jiujiang City,Jiangxi Province,China
    'CN-JX-XYU',  # Xinyu City,Jiangxi Province,China
    'CN-JX-YTS',  # Yingtan City,Jiangxi Province,China
    'CN-JX-GZH',  # Ganzhou City,Jiangxi Province,China
    'CN-JX-JAS',  # Ji'an City,Jiangxi Province,China
    'CN-JX-YCN',  # Yichun City,Jiangxi Province,China
    'CN-JX-FUZ',  # Fuzhou City,Jiangxi Province,China
    'CN-JX-SRS',  # Shangrao City,Jiangxi Province,China
    'CN-SD',  # Shandong Province,China
    'CN-SD-TNA',  # Jinan City,Shandong Province,China
    'CN-SD-TAO',  # Qingdao City,Shandong Province,China
    'CN-SD-ZBO',  # Zibo City,Shandong Province,China
    'CN-SD-ZZG',  # Zaozhuang City,Shandong Province,China
    'CN-SD-DYG',  # Dongying City,Shandong Province,China
    'CN-SD-YNT',  # Yantai City,Shandong Province,China
    'CN-SD-WEF',  # Weifang City,Shandong Province,China
    'CN-SD-JNG',  # Jining City,Shandong Province,China
    'CN-SD-TAI',  # Tai'an City,Shandong Province,China
    'CN-SD-WEH',  # Weihai City,Shandong Province,China
    'CN-SD-RZH',  # Rizhao City,Shandong Province,China
    'CN-SD-LWS',  # Laiwu City,Shandong Province,China
    'CN-SD-LYI',  # Linyi City,Shandong Province,China
    'CN-SD-DZS',  # Dezhou City,Shandong Province,China
    'CN-SD-LCH',  # Liaocheng City,Shandong Province,China
    'CN-SD-BZH',  # Binzhou City,Shandong Province,China
    'CN-SD-HZS',  # Heze City,Shandong Province,China
    'CN-HA',  # Henan Province,China
    'CN-HA-CGO',  # Zhengzhou City,Henan Province,China
    'CN-HA-KFS',  # Kaifeng City,Henan Province,China
    'CN-HA-LYA',  # Luoyang City,Henan Province,China
    'CN-HA-PDS',  # Pingdingshan City,Henan Province,China
    'CN-HA-AYS',  # Anyang City,Henan Province,China
    'CN-HA-HBS',  # Hebi City,Henan Province,China
    'CN-HA-XXS',  # Xinxiang City,Henan Province,China
    'CN-HA-JZY',  # Jiaozuo City,Henan Province,China
    'CN-HA-PYS',  # Puyang City,Henan Province,China
    'CN-HA-XCS',  # Xuchang City,Henan Province,China
    'CN-HA-LHS',  # Luohe City,Henan Province,China
    'CN-HA-SMX',  # Sanmenxia City,Henan Province,China
    'CN-HA-NYS',  # Nanyang City,Henan Province,China
    'CN-HA-SQS',  # Shangqiu City,Henan Province,China
    'CN-HA-XYG',  # Xinyang City,Henan Province,China
    'CN-HA-ZKS',  # Zhoukou City,Henan Province,China
    'CN-HA-ZMD',  # Zhumadian City,Henan Province,China
    'CN-HB',  # Hubei Province,China
    'CN-HB-WUH',  # Wuhan City,Hubei Province,China
    'CN-HB-HSI',  # Huangshi City,Hubei Province,China
    'CN-HB-SYE',  # Shiyan City,Hubei Province,China
    'CN-HB-YCO',  # Yichang City,Hubei Province,China
    'CN-HB-XFN',  # Xiangfan City,Hubei Province,China
    'CN-HB-EZS',  # Ezhou City,Hubei Province,China
    'CN-HB-JMS',  # Jingmen City,Hubei Province,China
    'CN-HB-XGE',  # Xiaogan City,Hubei Province,China
    'CN-HB-JGZ',  # Jingzhou City,Hubei Province,China
    'CN-HB-HGE',  # Huanggang City,Hubei Province,China
    'CN-HB-XNS',  # Xianning City,Hubei Province,China
    'CN-HB-SZR',  # Suizhou City,Hubei Province,China
    'CN-HB-ESH',  # Enshi Tujia&Miao Autonomous Prefecture,Hubei Province,China
    'CN-HN',  # Hunan Province,China
    'CN-HN-CSX',  # Changsha City,Hunan Province,China
    'CN-HN-ZZS',  # Zhuzhou City,Hunan Province,China
    'CN-HN-XGT',  # Xiangtan City,Hunan Province,China
    'CN-HN-HNY',  # Hengyang City,Hunan Province,China
    'CN-HN-SYR',  # Shaoyang City,Hunan Province,China
    'CN-HN-YYG',  # Yueyang City,Hunan Province,China
    'CN-HN-CDE',  # Changde City,Hunan Province,China
    'CN-HN-ZJJ',  # Zhangjiajie City,Hunan Province,China
    'CN-HN-YYS',  # Yiyang City,Hunan Province,China
    'CN-HN-CNZ',  # Chenzhou City,Hunan Province,China
    'CN-HN-YZS',  # Yongzhou City,Hunan Province,China
    'CN-HN-HHS',  # Huaihua City,Hunan Province,China
    'CN-HN-LDI',  # Loudi City,Hunan Province,China
    'CN-HN-XXZ',  # ​Xiangxi Tujia&Miao Autonomous Prefecture​,Hunan Province,China
    'CN-GD',  # Guangdong Province,China
    'CN-GD-CAN',  # Guangzhou City,Guangdong Province,China
    'CN-GD-HSC',  # Shaoguan City,Guangdong Province,China
    'CN-GD-SZX',  # Shenzhen City,Guangdong Province,China
    'CN-GD-ZUH',  # Zhuhai City,Guangdong Province,China
    'CN-GD-SWA',  # Shantou City,Guangdong Province,China
    'CN-GD-FOS',  # Foshan City,Guangdong Province,China
    'CN-GD-JMN',  # Jiangmen City,Guangdong Province,China
    'CN-GD-ZHA',  # Zhanjiang City,Guangdong Province,China
    'CN-GD-MMI',  # Maoming City,Guangdong Province,China
    'CN-GD-ZQG',  # Zhaoqing City,Guangdong Province,China
    'CN-GD-HUI',  # Huizhou City,Guangdong Province,China
    'CN-GD-MXZ',  # Meizhou City,Guangdong Province,China
    'CN-GD-SWE',  # Shanwei City,Guangdong Province,China
    'CN-GD-HEY',  # Heyuan City,Guangdong Province,China
    'CN-GD-YJI',  # Yangjiang City,Guangdong Province,China
    'CN-GD-QYN',  # Qingyuan City,Guangdong Province,China
    'CN-GD-DGG',  # Dongguan City,Guangdong Province,China
    'CN-GD-ZSN',  # Zhongshan City,Guangdong Province,China
    'CN-GD-CZY',  # Chaozhou City,Guangdong Province,China
    'CN-GD-JIY',  # Jieyang City,Guangdong Province,China
    'CN-GD-YFS',  # Yunfu City,Guangdong Province,China
    'CN-GX',  # Guangxi Zhuang Autonomous Region,China
    'CN-GX-NNG',  # Nanning City,Guangxi Zhuang Autonomous Region,China
    'CN-GX-LZH',  # Liuzhou City,Guangxi Zhuang Autonomous Region,China
    'CN-GX-KWL',  # Guilin City,Guangxi Zhuang Autonomous Region,China
    'CN-GX-WUZ',  # Wuzhou City,Guangxi Zhuang Autonomous Region,China
    'CN-GX-BHY',  # Beihai City,Guangxi Zhuang Autonomous Region,China
    'CN-GX-FAN',  # Fangchenggang City,Guangxi Zhuang Autonomous Region,China
    'CN-GX-QZH',  # Qinzhou City,Guangxi Zhuang Autonomous Region,China
    'CN-GX-GUG',  # Guigang City,Guangxi Zhuang Autonomous Region,China
    'CN-GX-YUL',  # Yulin City,Guangxi Zhuang Autonomous Region,China
    'CN-GX-BSS',  # Bose City,Guangxi Zhuang Autonomous Region,China
    'CN-GX-HZO',  # Hezhou City,Guangxi Zhuang Autonomous Region,China
    'CN-GX-HCS',  # Hechi City,Guangxi Zhuang Autonomous Region,China
    'CN-GX-LIB',  # Laibin City,Guangxi Zhuang Autonomous Region,China
    'CN-GX-COZ',  # Chongzuo City,Guangxi Zhuang Autonomous Region,China
    'CN-HI',  # Hainan Province,China
    'CN-HI-HAK',  # Haikou City,Hainan Province,China
    'CN-HI-SYX',  # Sanva City,Hainan Province,China
    'CN-CQ',  # Chongqing City,China
    'CN-SC',  # Sichuan Province,China
    'CN-SC-CTU',  # Chengdu City,Sichuan Province,China
    'CN-SC-ZGS',  # Zigong City,Sichuan Province,China
    'CN-SC-PZH',  # Panzhihua City,Sichuan Province,China
    'CN-SC-LUZ',  # Luzhou City,Sichuan Province,China
    'CN-SC-DEY',  # Deyang City,Sichuan Province,China
    'CN-SC-MYG',  # Mianyang City,Sichuan Province,China
    'CN-SC-GYC',  # Guangyuan City,Sichuan Province,China
    'CN-SC-SNS',  # Suining City,Sichuan Province,China
    'CN-SC-NJS',  # Neijiang City,Sichuan Province,China
    'CN-SC-LES',  # Leshan City,Sichuan Province,China
    'CN-SC-NCO',  # Nanchong City,Sichuan Province,China
    'CN-SC-MSS',  # Meishan City,Sichuan Province,China
    'CN-SC-YBS',  # Yibin City,Sichuan Province,China
    'CN-SC-GAC',  # Guang'an City,Sichuan Province,China
    'CN-SC-DAZ',  # Dazhou City,Sichuan Province,China
    'CN-SC-YAS',  # Ya'an City,Sichuan Province,China
    'CN-SC-BZS',  # Bazhong City,Sichuan Province,China
    'CN-SC-ZYS',  # Ziyang City,Sichuan Province,China
    'CN-SC-ABA',  # Aba Tibetan&Qiang Autonomous Prefecture,Sichuan Province,China
    'CN-SC-GAZ',  # Garzê Tibetan Autonomous Prefecture,Sichuan Province,China
    'CN-SC-LSY',  # Liangshan Yi Autonomous Prefecture​,Sichuan Province,China
    'CN-GZ',  # Guizhou Province,China
    'CN-GZ-KWE',  # Guiyang City,Guizhou Province,China
    'CN-GZ-LPS',  # Lupanshui City,Guizhou Province,China
    'CN-GZ-ZNY',  # Zunyi City,Guizhou Province,China
    'CN-GZ-ASS',  # Anshun City,Guizhou Province,China
    'CN-GZ-TRD',  # Tongren Diqu,Guizhou Province,China
    'CN-GZ-QXZ',  # Qianxinan Buyei&Miao Autonomous Prefecture,Guizhou Province,China
    'CN-GZ-BJD',  # Bijie Diqu,Guizhou Province,China
    'CN-GZ-QND',  # Qiandongnan Miao&Dong Autonomous Prefecture,Guizhou Province,China
    'CN-GZ-QNZ',  # ​Qiannan Buyei&Miao Autonomous Prefecture,Guizhou Province,China
    'CN-YN',  # Yunnan Province,China
    'CN-YN-KMG',  # Kunming City,Yunnan Province,China
    'CN-YN-QJS',  # Qujing City,Yunnan Province,China
    'CN-YN-YXS',  # Yuxi City,Yunnan Province,China
    'CN-YN-BOS',  # Baoshan City,Yunnan Province,China
    'CN-YN-ZTS',  # Zhaotong City,Yunnan Province,China
    'CN-YN-LJH',  # Lijiang City,Yunnan Province,China
    'CN-YN-PRS',  # Pu'er City,Yunnan Province,China
    'CN-YN-LIH',  # Lincang City,Yunnan Province,China
    'CN-YN-CXD',  # ​Chuxiong Yi Autonomous Prefecture,Yunnan Province,China
    'CN-YN-HHZ',  # ​Honghe Hani&Yi Autonomous Prefecture,Yunnan Province,China
    'CN-YN-WSZ',  # ​Wenshan Zhuang&Miao Autonomous Prefecture,Yunnan Province,China
    'CN-YN-XSB',  # Xishuangbanna Dai Autonomous Prefecture,Yunnan Province,China
    'CN-YN-DLZ',  # ​Dali Bai Autonomous Prefecture,Yunnan Province,China
    'CN-YN-DHG',  # Dehong Dai&Jingpo Autonomous Prefecture,Yunnan Province,China
    'CN-YN-NUJ',  # Nujiang Lisu Autonomous Prefecture,Yunnan Province,China
    'CN-YN-DEZ',  # Deqên Tibetan Autonomous Prefecture,Yunnan Province,China
    'CN-XZ',  # Tibet Autonomous Region,China
    'CN-XZ-LXA',  # Lhasa City,Tibet Autonomous Region,China
    'CN-XZ-QAD',  # Qamdo Diqu,Tibet Autonomous Region,China
    'CN-XZ-SND',  # Shannan Diqu,Tibet Autonomous Region,China
    'CN-XZ-XID',  # Xigaze Diqu,Tibet Autonomous Region,China
    'CN-XZ-NAD',  # Nagqu Diqu,Tibet Autonomous Region,China
    'CN-XZ-NGD',  # Ngari Diqu,Tibet Autonomous Region,China
    'CN-XZ-NYD',  # Nyingchi Diqu,Tibet Autonomous Region,China
    'CN-SN',  # Shaanxi Province,China
    'CN-SN-SIA',  # Xi'an City,Shaanxi Province,China
    'CN-SN-TCN',  # Tongchuan City,Shaanxi Province,China
    'CN-SN-BJI',  # Baoji City,Shaanxi Province,China
    'CN-SN-XYS',  # Xianyang City,Shaanxi Province,China
    'CN-SN-WNA',  # Weinan City,Shaanxi Province,China
    'CN-SN-YNA',  # Yan'an City,Shaanxi Province,China
    'CN-SN-HZJ',  # Hanzhong City,Shaanxi Province,China
    'CN-SN-YLN',  # Yulin City,Shaanxi Province,China
    'CN-SN-ANK',  # Ankang City,Shaanxi Province,China
    'CN-SN-SLH',  # Shangluo City,Shaanxi Province,China
    'CN-GS',  # Gansu Province,China
    'CN-GS-LHW',  # Lanzhou City,Gansu Province,China
    'CN-GS-JYG',  # Jiayuguan City,Gansu Province,China
    'CN-GS-JCS',  # Jinchang City,Gansu Province,China
    'CN-GS-BYS',  # Baiyin City,Gansu Province,China
    'CN-GS-TSU',  # Tianshui City,Gansu Province,China
    'CN-GS-WWS',  # Wuwei City,Gansu Province,China
    'CN-GS-ZYE',  # Zhangye City,Gansu Province,China
    'CN-GS-PLS',  # Pingliang City,Gansu Province,China
    'CN-GS-JQG',  # Jiuquan City,Gansu Province,China
    'CN-GS-QYI',  # Qingyang City,Gansu Province,China
    'CN-GS-DNX',  # Dingxi City,Gansu Province,China
    'CN-GS-LGN',  # Longnan City,Gansu Province,China
    'CN-GS-LXH',  # ​Linxia Hui Autonomous Prefecture,Gansu Province,China
    'CN-GS-GNZ',  # Gannan Tibetan Autonomous Prefecture,Gansu Province,China
    'CN-QH',  # Qinghai Province,China
    'CN-QH-XNN',  # Xining City,Qinghai Province,China
    'CN-QH-HDD',  # Haidong Diqu,Qinghai Province,China
    'CN-QH-HBZ',  # Haibei Tibetan Autonomous Prefecture,Qinghai Province,China
    'CN-QH-HN7',  # Huangnan Tibetan Autonomous Prefecture,Qinghai Province,China
    'CN-QH-HNN',  # Hainan Tibetan Autonomous Prefecture,Qinghai Province,China
    'CN-QH-GOL',  # Golog Tibetan Autonomous Prefecture,Qinghai Province,China
    'CN-QH-YSZ',  # Yushu Tibetan Autonomous Prefecture,Qinghai Province,China
    'CN-QH-HXZ',  # Haixi Mongol&Tibetan Autonomous Prefecture,Qinghai Province,China
    'CN-NX',  # Ningxia Hui Autonomous Region,China
    'CN-NX-INC',  # Yinchuan City,Ningxia Hui Autonomous Region,China
    'CN-NX-SZS',  # Shizuishan City,Ningxia Hui Autonomous Region,China
    'CN-NX-WZS',  # Wuzhong City,Ningxia Hui Autonomous Region,China
    'CN-NX-GYN',  # Guyuan City,Ningxia Hui Autonomous Region,China
    'CN-NX-ZWS',  # Zhongwei City,Ningxia Hui Autonomous Region,China
    'CN-XJ',  # Xinjiang Uygur Autonomous Region,China
    'CN-XJ-URC',  # Urümqi City,Xinjiang Uygur Autonomous Region,China
    'CN-XJ-KAR',  # Karamay City,Xinjiang Uygur Autonomous Region,China
    'CN-XJ-TUD',  # Turpan Diqu,Xinjiang Uygur Autonomous Region,China
    'CN-XJ-HMD',  # Hami(Kumul)Diqu,Xinjiang Uygur Autonomous Region,China
    'CN-XJ-CJZ',  # Changji Hui Autonomous Prefecture,Xinjiang Uygur Autonomous Region,China
    'CN-XJ-BOR',  # Bortala Mongol Autonomous Prefecture,Xinjiang Uygur Autonomous Region,China
    'CN-XJ-BAG',  # Bayingolin Mongol Autonomous Prefecture,Xinjiang Uygur Autonomous Region,China
    'CN-XJ-AKD',  # Aksu Diqu,Xinjiang Uygur Autonomous Region,China
    'CN-XJ-KIZ',  # ​Kizilsu Kirgiz Autonomous Prefecture,Xinjiang Uygur Autonomous Region,China
    'CN-XJ-KSI',  # Kashi(Kaxgar)Diqu,Xinjiang Uygur Autonomous Region,China
    'CN-XJ-HOD',  # Hotan Diqu,Xinjiang Uygur Autonomous Region,China
    'CN-XJ-ILD',  # ​Ili Kazak Autonomous Prefecture,Xinjiang Uygur Autonomous Region,China
    'CN-XJ-TCD',  # Tacheng(Qoqek)Diqu,Xinjiang Uygur Autonomous Region,China
    'CN-XJ-ALD',  # Altay Diqu,Xinjiang Uygur Autonomous Region,China
    'CN-TW',  # Taiwan Province,China
    'CN-HK',  # Hong Kong Special Administrative Region of the People's Republic of China
    'CN-MO',  # Macao Special Administrative Region of the People's Republic of China
]


# Type-safe union of all locations category text values
# Note: This is a very large Literal type with ~647 values.
# The full list is generated from LOCATIONS_CATEGORIES.
# For type checking purposes, we use str as the actual type since
# Python's type checker may have issues with such large Literal types.
# In practice, the values are validated at runtime using LOCATIONS_CATEGORIES.
TidasLocationsText = str  # Effectively all text values from LOCATIONS_CATEGORIES


# Runtime metadata for lookups
LOCATIONS_CATEGORIES: dict[str, LocationsCategoryData] = {
    'NULL': {
        'level': '0',
        'classId': 'NULL',
        'text': 'None',
    },
    'GLO': {
        'level': '0',
        'classId': 'GLO',
        'text': 'Global',
    },
    'RAF': {
        'level': '0',
        'classId': 'RAF',
        'text': 'Africa',
    },
    'RAM': {
        'level': '0',
        'classId': 'RAM',
        'text': 'Americas',
    },
    'RAS': {
        'level': '0',
        'classId': 'RAS',
        'text': 'Asia and Pacific',
    },
    'RER': {
        'level': '0',
        'classId': 'RER',
        'text': 'Europe',
    },
    'OCE': {
        'level': '0',
        'classId': 'OCE',
        'text': 'Oceania',
    },
    'MEA': {
        'level': '0',
        'classId': 'MEA',
        'text': 'Middle East and North Africa',
    },
    'AFR': {
        'level': '0',
        'classId': 'AFR',
        'text': 'Sub-Saharan Africa',
    },
    'RLA': {
        'level': '0',
        'classId': 'RLA',
        'text': 'Latin America & the Caribbean',
    },
    'RNA': {
        'level': '0',
        'classId': 'RNA',
        'text': 'Northern America',
    },
    'CPA': {
        'level': '0',
        'classId': 'CPA',
        'text': 'Centrally Planned Asia and China',
    },
    'EAS': {
        'level': '0',
        'classId': 'EAS',
        'text': 'Eastern Asia',
    },
    'PAS': {
        'level': '0',
        'classId': 'PAS',
        'text': 'Other Pacific Asia',
    },
    'SAS': {
        'level': '0',
        'classId': 'SAS',
        'text': 'South Asia',
    },
    'EEU': {
        'level': '0',
        'classId': 'EEU',
        'text': 'Central and Eastern Europe',
    },
    'WEU': {
        'level': '0',
        'classId': 'WEU',
        'text': 'Western Europe',
    },
    'RNE': {
        'level': '0',
        'classId': 'RNE',
        'text': 'Near East',
    },
    'RME': {
        'level': '0',
        'classId': 'RME',
        'text': 'Middle East',
    },
    'EU-15': {
        'level': '0',
        'classId': 'EU-15',
        'text': 'EU 15',
    },
    'EU-NMC': {
        'level': '0',
        'classId': 'EU-NMC',
        'text': 'EU New Member Countries 2004',
    },
    'EU-25': {
        'level': '0',
        'classId': 'EU-25',
        'text': 'EU 25',
    },
    'EC-CC': {
        'level': '0',
        'classId': 'EC-CC',
        'text': 'EU Candidate Countries 2005',
    },
    'EU-25&CC': {
        'level': '0',
        'classId': 'EU-25&CC',
        'text': 'EU 25 Plus Candidate Countries 2005',
    },
    'EU-AC': {
        'level': '0',
        'classId': 'EU-AC',
        'text': 'EU Associated Countries 2005',
    },
    'EU-25&CC&AC': {
        'level': '0',
        'classId': 'EU-25&CC&AC',
        'text': 'EU 25 Plus Candidate Countries and Associated Countries 2005',
    },
    'EU-27': {
        'level': '0',
        'classId': 'EU-27',
        'text': 'EU 27',
    },
    'PAO': {
        'level': '0',
        'classId': 'PAO',
        'text': 'Pacific OECD (Japan, Australia, New Zealand)',
    },
    'FSU': {
        'level': '0',
        'classId': 'FSU',
        'text': 'Independent States of the Former Soviet Union',
    },
    'UCTE': {
        'level': '0',
        'classId': 'UCTE',
        'text': 'Union for the Co-ordination of Transmission of Electricity',
    },
    'CENTREL': {
        'level': '0',
        'classId': 'CENTREL',
        'text': 'Central european power association',
    },
    'NORDEL': {
        'level': '0',
        'classId': 'NORDEL',
        'text': 'Nordic countries power association',
    },
    'EU+EFTA+UK': {
        'level': '0',
        'classId': 'EU+EFTA+UK',
        'text': 'complete EU',
    },
    'AD': {
        'level': '0',
        'classId': 'AD',
        'text': 'Andorra',
    },
    'AE': {
        'level': '0',
        'classId': 'AE',
        'text': 'United Arab Emirates',
    },
    'AF': {
        'level': '0',
        'classId': 'AF',
        'text': 'Afghanistan',
    },
    'AG': {
        'level': '0',
        'classId': 'AG',
        'text': 'Antigua and Barbuda',
    },
    'AI': {
        'level': '0',
        'classId': 'AI',
        'text': 'Anguilla',
    },
    'AL': {
        'level': '0',
        'classId': 'AL',
        'text': 'Albania',
    },
    'AM': {
        'level': '0',
        'classId': 'AM',
        'text': 'Armenia',
    },
    'AO': {
        'level': '0',
        'classId': 'AO',
        'text': 'Angola',
    },
    'AQ': {
        'level': '0',
        'classId': 'AQ',
        'text': 'Antarctica',
    },
    'AR': {
        'level': '0',
        'classId': 'AR',
        'text': 'Argentina',
    },
    'AS': {
        'level': '0',
        'classId': 'AS',
        'text': 'American Samoa',
    },
    'AT': {
        'level': '0',
        'classId': 'AT',
        'text': 'Austria',
    },
    'AU': {
        'level': '0',
        'classId': 'AU',
        'text': 'Australia',
    },
    'AW': {
        'level': '0',
        'classId': 'AW',
        'text': 'Aruba',
    },
    'AX': {
        'level': '0',
        'classId': 'AX',
        'text': 'Åland Islands',
    },
    'AZ': {
        'level': '0',
        'classId': 'AZ',
        'text': 'Azerbaijan',
    },
    'BA': {
        'level': '0',
        'classId': 'BA',
        'text': 'Bosnia and Herzegovina',
    },
    'BB': {
        'level': '0',
        'classId': 'BB',
        'text': 'Barbados',
    },
    'BD': {
        'level': '0',
        'classId': 'BD',
        'text': 'Bangladesh',
    },
    'BE': {
        'level': '0',
        'classId': 'BE',
        'text': 'Belgium',
    },
    'BF': {
        'level': '0',
        'classId': 'BF',
        'text': 'Burkina Faso',
    },
    'BG': {
        'level': '0',
        'classId': 'BG',
        'text': 'Bulgaria',
    },
    'BH': {
        'level': '0',
        'classId': 'BH',
        'text': 'Bahrain',
    },
    'BI': {
        'level': '0',
        'classId': 'BI',
        'text': 'Burundi',
    },
    'BJ': {
        'level': '0',
        'classId': 'BJ',
        'text': 'Benin',
    },
    'BL': {
        'level': '0',
        'classId': 'BL',
        'text': 'Saint Barthélemy',
    },
    'BM': {
        'level': '0',
        'classId': 'BM',
        'text': 'Bermuda',
    },
    'BN': {
        'level': '0',
        'classId': 'BN',
        'text': 'Brunei Darussalam',
    },
    'BO': {
        'level': '0',
        'classId': 'BO',
        'text': 'Bolivia (Plurinational State of)',
    },
    'BQ': {
        'level': '0',
        'classId': 'BQ',
        'text': 'Bonaire, Sint Eustatius and Saba',
    },
    'BR': {
        'level': '0',
        'classId': 'BR',
        'text': 'Brazil',
    },
    'BS': {
        'level': '0',
        'classId': 'BS',
        'text': 'Bahamas',
    },
    'BT': {
        'level': '0',
        'classId': 'BT',
        'text': 'Bhutan',
    },
    'BV': {
        'level': '0',
        'classId': 'BV',
        'text': 'Bouvet Island',
    },
    'BW': {
        'level': '0',
        'classId': 'BW',
        'text': 'Botswana',
    },
    'BY': {
        'level': '0',
        'classId': 'BY',
        'text': 'Belarus',
    },
    'BZ': {
        'level': '0',
        'classId': 'BZ',
        'text': 'Belize',
    },
    'CA': {
        'level': '0',
        'classId': 'CA',
        'text': 'Canada',
    },
    'CC': {
        'level': '0',
        'classId': 'CC',
        'text': 'Cocos (Keeling) Islands',
    },
    'CD': {
        'level': '0',
        'classId': 'CD',
        'text': 'Congo, Democratic Republic of the',
    },
    'CF': {
        'level': '0',
        'classId': 'CF',
        'text': 'Central African Republic',
    },
    'CG': {
        'level': '0',
        'classId': 'CG',
        'text': 'Congo',
    },
    'CH': {
        'level': '0',
        'classId': 'CH',
        'text': 'Switzerland',
    },
    'CI': {
        'level': '0',
        'classId': 'CI',
        'text': 'Côte d\'Ivoire',
    },
    'CK': {
        'level': '0',
        'classId': 'CK',
        'text': 'Cook Islands',
    },
    'CL': {
        'level': '0',
        'classId': 'CL',
        'text': 'Chile',
    },
    'CM': {
        'level': '0',
        'classId': 'CM',
        'text': 'Cameroon',
    },
    'CO': {
        'level': '0',
        'classId': 'CO',
        'text': 'Colombia',
    },
    'CR': {
        'level': '0',
        'classId': 'CR',
        'text': 'Costa Rica',
    },
    'CU': {
        'level': '0',
        'classId': 'CU',
        'text': 'Cuba',
    },
    'CV': {
        'level': '0',
        'classId': 'CV',
        'text': 'Cabo Verde',
    },
    'CW': {
        'level': '0',
        'classId': 'CW',
        'text': 'Curaçao',
    },
    'CX': {
        'level': '0',
        'classId': 'CX',
        'text': 'Christmas Island',
    },
    'CY': {
        'level': '0',
        'classId': 'CY',
        'text': 'Cyprus',
    },
    'CZ': {
        'level': '0',
        'classId': 'CZ',
        'text': 'Czechia',
    },
    'DE': {
        'level': '0',
        'classId': 'DE',
        'text': 'Germany',
    },
    'DJ': {
        'level': '0',
        'classId': 'DJ',
        'text': 'Djibouti',
    },
    'DK': {
        'level': '0',
        'classId': 'DK',
        'text': 'Denmark',
    },
    'DM': {
        'level': '0',
        'classId': 'DM',
        'text': 'Dominica',
    },
    'DO': {
        'level': '0',
        'classId': 'DO',
        'text': 'Dominican Republic',
    },
    'DZ': {
        'level': '0',
        'classId': 'DZ',
        'text': 'Algeria',
    },
    'EC': {
        'level': '0',
        'classId': 'EC',
        'text': 'Ecuador',
    },
    'EE': {
        'level': '0',
        'classId': 'EE',
        'text': 'Estonia',
    },
    'EG': {
        'level': '0',
        'classId': 'EG',
        'text': 'Egypt',
    },
    'EH': {
        'level': '0',
        'classId': 'EH',
        'text': 'Western Sahara',
    },
    'ER': {
        'level': '0',
        'classId': 'ER',
        'text': 'Eritrea',
    },
    'ES': {
        'level': '0',
        'classId': 'ES',
        'text': 'Spain',
    },
    'ET': {
        'level': '0',
        'classId': 'ET',
        'text': 'Ethiopia',
    },
    'FI': {
        'level': '0',
        'classId': 'FI',
        'text': 'Finland',
    },
    'FJ': {
        'level': '0',
        'classId': 'FJ',
        'text': 'Fiji',
    },
    'FK': {
        'level': '0',
        'classId': 'FK',
        'text': 'Falkland Islands (Malvinas)',
    },
    'FM': {
        'level': '0',
        'classId': 'FM',
        'text': 'Micronesia (Federated States of)',
    },
    'FO': {
        'level': '0',
        'classId': 'FO',
        'text': 'Faroe Islands',
    },
    'FR': {
        'level': '0',
        'classId': 'FR',
        'text': 'France',
    },
    'GA': {
        'level': '0',
        'classId': 'GA',
        'text': 'Gabon',
    },
    'GB': {
        'level': '0',
        'classId': 'GB',
        'text': 'United Kingdom of Great Britain and Northern Ireland',
    },
    'GD': {
        'level': '0',
        'classId': 'GD',
        'text': 'Grenada',
    },
    'GE': {
        'level': '0',
        'classId': 'GE',
        'text': 'Georgia',
    },
    'GF': {
        'level': '0',
        'classId': 'GF',
        'text': 'French Guiana',
    },
    'GG': {
        'level': '0',
        'classId': 'GG',
        'text': 'Guernsey',
    },
    'GH': {
        'level': '0',
        'classId': 'GH',
        'text': 'Ghana',
    },
    'GI': {
        'level': '0',
        'classId': 'GI',
        'text': 'Gibraltar',
    },
    'GL': {
        'level': '0',
        'classId': 'GL',
        'text': 'Greenland',
    },
    'GM': {
        'level': '0',
        'classId': 'GM',
        'text': 'Gambia',
    },
    'GN': {
        'level': '0',
        'classId': 'GN',
        'text': 'Guinea',
    },
    'GP': {
        'level': '0',
        'classId': 'GP',
        'text': 'Guadeloupe',
    },
    'GQ': {
        'level': '0',
        'classId': 'GQ',
        'text': 'Equatorial Guinea',
    },
    'GR': {
        'level': '0',
        'classId': 'GR',
        'text': 'Greece',
    },
    'GS': {
        'level': '0',
        'classId': 'GS',
        'text': 'South Georgia and the South Sandwich Islands',
    },
    'GT': {
        'level': '0',
        'classId': 'GT',
        'text': 'Guatemala',
    },
    'GU': {
        'level': '0',
        'classId': 'GU',
        'text': 'Guam',
    },
    'GW': {
        'level': '0',
        'classId': 'GW',
        'text': 'Guinea-Bissau',
    },
    'GY': {
        'level': '0',
        'classId': 'GY',
        'text': 'Guyana',
    },
    'HM': {
        'level': '0',
        'classId': 'HM',
        'text': 'Heard Island and McDonald Islands',
    },
    'HN': {
        'level': '0',
        'classId': 'HN',
        'text': 'Honduras',
    },
    'HR': {
        'level': '0',
        'classId': 'HR',
        'text': 'Croatia',
    },
    'HT': {
        'level': '0',
        'classId': 'HT',
        'text': 'Haiti',
    },
    'HU': {
        'level': '0',
        'classId': 'HU',
        'text': 'Hungary',
    },
    'ID': {
        'level': '0',
        'classId': 'ID',
        'text': 'Indonesia',
    },
    'IE': {
        'level': '0',
        'classId': 'IE',
        'text': 'Ireland',
    },
    'IL': {
        'level': '0',
        'classId': 'IL',
        'text': 'Israel',
    },
    'IM': {
        'level': '0',
        'classId': 'IM',
        'text': 'Isle of Man',
    },
    'IN': {
        'level': '0',
        'classId': 'IN',
        'text': 'India',
    },
    'IO': {
        'level': '0',
        'classId': 'IO',
        'text': 'British Indian Ocean Territory',
    },
    'IQ': {
        'level': '0',
        'classId': 'IQ',
        'text': 'Iraq',
    },
    'IR': {
        'level': '0',
        'classId': 'IR',
        'text': 'Iran (Islamic Republic of)',
    },
    'IS': {
        'level': '0',
        'classId': 'IS',
        'text': 'Iceland',
    },
    'IT': {
        'level': '0',
        'classId': 'IT',
        'text': 'Italy',
    },
    'JE': {
        'level': '0',
        'classId': 'JE',
        'text': 'Jersey',
    },
    'JM': {
        'level': '0',
        'classId': 'JM',
        'text': 'Jamaica',
    },
    'JO': {
        'level': '0',
        'classId': 'JO',
        'text': 'Jordan',
    },
    'JP': {
        'level': '0',
        'classId': 'JP',
        'text': 'Japan',
    },
    'KE': {
        'level': '0',
        'classId': 'KE',
        'text': 'Kenya',
    },
    'KG': {
        'level': '0',
        'classId': 'KG',
        'text': 'Kyrgyzstan',
    },
    'KH': {
        'level': '0',
        'classId': 'KH',
        'text': 'Cambodia',
    },
    'KI': {
        'level': '0',
        'classId': 'KI',
        'text': 'Kiribati',
    },
    'KM': {
        'level': '0',
        'classId': 'KM',
        'text': 'Comoros',
    },
    'KN': {
        'level': '0',
        'classId': 'KN',
        'text': 'Saint Kitts and Nevis',
    },
    'KP': {
        'level': '0',
        'classId': 'KP',
        'text': 'Korea (Democratic People\'s Republic of)',
    },
    'KR': {
        'level': '0',
        'classId': 'KR',
        'text': 'Korea, Republic of',
    },
    'KW': {
        'level': '0',
        'classId': 'KW',
        'text': 'Kuwait',
    },
    'KY': {
        'level': '0',
        'classId': 'KY',
        'text': 'Cayman Islands',
    },
    'KZ': {
        'level': '0',
        'classId': 'KZ',
        'text': 'Kazakhstan',
    },
    'LA': {
        'level': '0',
        'classId': 'LA',
        'text': 'Lao People\'s Democratic Republic',
    },
    'LB': {
        'level': '0',
        'classId': 'LB',
        'text': 'Lebanon',
    },
    'LC': {
        'level': '0',
        'classId': 'LC',
        'text': 'Saint Lucia',
    },
    'LI': {
        'level': '0',
        'classId': 'LI',
        'text': 'Liechtenstein',
    },
    'LK': {
        'level': '0',
        'classId': 'LK',
        'text': 'Sri Lanka',
    },
    'LR': {
        'level': '0',
        'classId': 'LR',
        'text': 'Liberia',
    },
    'LS': {
        'level': '0',
        'classId': 'LS',
        'text': 'Lesotho',
    },
    'LT': {
        'level': '0',
        'classId': 'LT',
        'text': 'Lithuania',
    },
    'LU': {
        'level': '0',
        'classId': 'LU',
        'text': 'Luxembourg',
    },
    'LV': {
        'level': '0',
        'classId': 'LV',
        'text': 'Latvia',
    },
    'LY': {
        'level': '0',
        'classId': 'LY',
        'text': 'Libya',
    },
    'MA': {
        'level': '0',
        'classId': 'MA',
        'text': 'Morocco',
    },
    'MC': {
        'level': '0',
        'classId': 'MC',
        'text': 'Monaco',
    },
    'MD': {
        'level': '0',
        'classId': 'MD',
        'text': 'Moldova, Republic of',
    },
    'ME': {
        'level': '0',
        'classId': 'ME',
        'text': 'Montenegro',
    },
    'MF': {
        'level': '0',
        'classId': 'MF',
        'text': 'Saint Martin (French part)',
    },
    'MG': {
        'level': '0',
        'classId': 'MG',
        'text': 'Madagascar',
    },
    'MH': {
        'level': '0',
        'classId': 'MH',
        'text': 'Marshall Islands',
    },
    'MK': {
        'level': '0',
        'classId': 'MK',
        'text': 'North Macedonia',
    },
    'ML': {
        'level': '0',
        'classId': 'ML',
        'text': 'Mali',
    },
    'MM': {
        'level': '0',
        'classId': 'MM',
        'text': 'Myanmar',
    },
    'MN': {
        'level': '0',
        'classId': 'MN',
        'text': 'Mongolia',
    },
    'MP': {
        'level': '0',
        'classId': 'MP',
        'text': 'Northern Mariana Islands',
    },
    'MQ': {
        'level': '0',
        'classId': 'MQ',
        'text': 'Martinique',
    },
    'MR': {
        'level': '0',
        'classId': 'MR',
        'text': 'Mauritania',
    },
    'MS': {
        'level': '0',
        'classId': 'MS',
        'text': 'Montserrat',
    },
    'MT': {
        'level': '0',
        'classId': 'MT',
        'text': 'Malta',
    },
    'MU': {
        'level': '0',
        'classId': 'MU',
        'text': 'Mauritius',
    },
    'MV': {
        'level': '0',
        'classId': 'MV',
        'text': 'Maldives',
    },
    'MW': {
        'level': '0',
        'classId': 'MW',
        'text': 'Malawi',
    },
    'MX': {
        'level': '0',
        'classId': 'MX',
        'text': 'Mexico',
    },
    'MY': {
        'level': '0',
        'classId': 'MY',
        'text': 'Malaysia',
    },
    'MZ': {
        'level': '0',
        'classId': 'MZ',
        'text': 'Mozambique',
    },
    'NA': {
        'level': '0',
        'classId': 'NA',
        'text': 'Namibia',
    },
    'NC': {
        'level': '0',
        'classId': 'NC',
        'text': 'New Caledonia',
    },
    'NE': {
        'level': '0',
        'classId': 'NE',
        'text': 'Niger',
    },
    'NF': {
        'level': '0',
        'classId': 'NF',
        'text': 'Norfolk Island',
    },
    'NG': {
        'level': '0',
        'classId': 'NG',
        'text': 'Nigeria',
    },
    'NI': {
        'level': '0',
        'classId': 'NI',
        'text': 'Nicaragua',
    },
    'NL': {
        'level': '0',
        'classId': 'NL',
        'text': 'Netherlands',
    },
    'NO': {
        'level': '0',
        'classId': 'NO',
        'text': 'Norway',
    },
    'NP': {
        'level': '0',
        'classId': 'NP',
        'text': 'Nepal',
    },
    'NR': {
        'level': '0',
        'classId': 'NR',
        'text': 'Nauru',
    },
    'NU': {
        'level': '0',
        'classId': 'NU',
        'text': 'Niue',
    },
    'NZ': {
        'level': '0',
        'classId': 'NZ',
        'text': 'New Zealand',
    },
    'OM': {
        'level': '0',
        'classId': 'OM',
        'text': 'Oman',
    },
    'PA': {
        'level': '0',
        'classId': 'PA',
        'text': 'Panama',
    },
    'PE': {
        'level': '0',
        'classId': 'PE',
        'text': 'Peru',
    },
    'PF': {
        'level': '0',
        'classId': 'PF',
        'text': 'French Polynesia',
    },
    'PG': {
        'level': '0',
        'classId': 'PG',
        'text': 'Papua New Guinea',
    },
    'PH': {
        'level': '0',
        'classId': 'PH',
        'text': 'Philippines',
    },
    'PK': {
        'level': '0',
        'classId': 'PK',
        'text': 'Pakistan',
    },
    'PL': {
        'level': '0',
        'classId': 'PL',
        'text': 'Poland',
    },
    'PM': {
        'level': '0',
        'classId': 'PM',
        'text': 'Saint Pierre and Miquelon',
    },
    'PN': {
        'level': '0',
        'classId': 'PN',
        'text': 'Pitcairn',
    },
    'PR': {
        'level': '0',
        'classId': 'PR',
        'text': 'Puerto Rico',
    },
    'PS': {
        'level': '0',
        'classId': 'PS',
        'text': 'Palestine, State of',
    },
    'PT': {
        'level': '0',
        'classId': 'PT',
        'text': 'Portugal',
    },
    'PW': {
        'level': '0',
        'classId': 'PW',
        'text': 'Palau',
    },
    'PY': {
        'level': '0',
        'classId': 'PY',
        'text': 'Paraguay',
    },
    'QA': {
        'level': '0',
        'classId': 'QA',
        'text': 'Qatar',
    },
    'RE': {
        'level': '0',
        'classId': 'RE',
        'text': 'Réunion',
    },
    'RO': {
        'level': '0',
        'classId': 'RO',
        'text': 'Romania',
    },
    'RS': {
        'level': '0',
        'classId': 'RS',
        'text': 'Serbia',
    },
    'RU': {
        'level': '0',
        'classId': 'RU',
        'text': 'Russian Federation',
    },
    'RW': {
        'level': '0',
        'classId': 'RW',
        'text': 'Rwanda',
    },
    'SA': {
        'level': '0',
        'classId': 'SA',
        'text': 'Saudi Arabia',
    },
    'SB': {
        'level': '0',
        'classId': 'SB',
        'text': 'Solomon Islands',
    },
    'SC': {
        'level': '0',
        'classId': 'SC',
        'text': 'Seychelles',
    },
    'SD': {
        'level': '0',
        'classId': 'SD',
        'text': 'Sudan',
    },
    'SE': {
        'level': '0',
        'classId': 'SE',
        'text': 'Sweden',
    },
    'SG': {
        'level': '0',
        'classId': 'SG',
        'text': 'Singapore',
    },
    'SH': {
        'level': '0',
        'classId': 'SH',
        'text': 'Saint Helena, Ascension and Tristan da Cunha',
    },
    'SI': {
        'level': '0',
        'classId': 'SI',
        'text': 'Slovenia',
    },
    'SJ': {
        'level': '0',
        'classId': 'SJ',
        'text': 'Svalbard and Jan Mayen',
    },
    'SK': {
        'level': '0',
        'classId': 'SK',
        'text': 'Slovakia',
    },
    'SL': {
        'level': '0',
        'classId': 'SL',
        'text': 'Sierra Leone',
    },
    'SM': {
        'level': '0',
        'classId': 'SM',
        'text': 'San Marino',
    },
    'SN': {
        'level': '0',
        'classId': 'SN',
        'text': 'Senegal',
    },
    'SO': {
        'level': '0',
        'classId': 'SO',
        'text': 'Somalia',
    },
    'SR': {
        'level': '0',
        'classId': 'SR',
        'text': 'Suriname',
    },
    'SS': {
        'level': '0',
        'classId': 'SS',
        'text': 'South Sudan',
    },
    'ST': {
        'level': '0',
        'classId': 'ST',
        'text': 'Sao Tome and Principe',
    },
    'SV': {
        'level': '0',
        'classId': 'SV',
        'text': 'El Salvador',
    },
    'SX': {
        'level': '0',
        'classId': 'SX',
        'text': 'Sint Maarten (Dutch part)',
    },
    'SY': {
        'level': '0',
        'classId': 'SY',
        'text': 'Syrian Arab Republic',
    },
    'SZ': {
        'level': '0',
        'classId': 'SZ',
        'text': 'Eswatini',
    },
    'TC': {
        'level': '0',
        'classId': 'TC',
        'text': 'Turks and Caicos Islands',
    },
    'TD': {
        'level': '0',
        'classId': 'TD',
        'text': 'Chad',
    },
    'TF': {
        'level': '0',
        'classId': 'TF',
        'text': 'French Southern Territories',
    },
    'TG': {
        'level': '0',
        'classId': 'TG',
        'text': 'Togo',
    },
    'TH': {
        'level': '0',
        'classId': 'TH',
        'text': 'Thailand',
    },
    'TJ': {
        'level': '0',
        'classId': 'TJ',
        'text': 'Tajikistan',
    },
    'TK': {
        'level': '0',
        'classId': 'TK',
        'text': 'Tokelau',
    },
    'TL': {
        'level': '0',
        'classId': 'TL',
        'text': 'Timor-Leste',
    },
    'TM': {
        'level': '0',
        'classId': 'TM',
        'text': 'Turkmenistan',
    },
    'TN': {
        'level': '0',
        'classId': 'TN',
        'text': 'Tunisia',
    },
    'TO': {
        'level': '0',
        'classId': 'TO',
        'text': 'Tonga',
    },
    'TR': {
        'level': '0',
        'classId': 'TR',
        'text': 'Türkiye',
    },
    'TT': {
        'level': '0',
        'classId': 'TT',
        'text': 'Trinidad and Tobago',
    },
    'TV': {
        'level': '0',
        'classId': 'TV',
        'text': 'Tuvalu',
    },
    'TZ': {
        'level': '0',
        'classId': 'TZ',
        'text': 'Tanzania, United Republic of',
    },
    'UA': {
        'level': '0',
        'classId': 'UA',
        'text': 'Ukraine',
    },
    'UG': {
        'level': '0',
        'classId': 'UG',
        'text': 'Uganda',
    },
    'UM': {
        'level': '0',
        'classId': 'UM',
        'text': 'United States Minor Outlying Islands',
    },
    'US': {
        'level': '0',
        'classId': 'US',
        'text': 'United States of America',
    },
    'UY': {
        'level': '0',
        'classId': 'UY',
        'text': 'Uruguay',
    },
    'UZ': {
        'level': '0',
        'classId': 'UZ',
        'text': 'Uzbekistan',
    },
    'VA': {
        'level': '0',
        'classId': 'VA',
        'text': 'Holy See',
    },
    'VC': {
        'level': '0',
        'classId': 'VC',
        'text': 'Saint Vincent and the Grenadines',
    },
    'VE': {
        'level': '0',
        'classId': 'VE',
        'text': 'Venezuela (Bolivarian Republic of)',
    },
    'VG': {
        'level': '0',
        'classId': 'VG',
        'text': 'Virgin Islands (British)',
    },
    'VI': {
        'level': '0',
        'classId': 'VI',
        'text': 'Virgin Islands (U.S.)',
    },
    'VN': {
        'level': '0',
        'classId': 'VN',
        'text': 'Viet Nam',
    },
    'VU': {
        'level': '0',
        'classId': 'VU',
        'text': 'Vanuatu',
    },
    'WF': {
        'level': '0',
        'classId': 'WF',
        'text': 'Wallis and Futuna',
    },
    'WS': {
        'level': '0',
        'classId': 'WS',
        'text': 'Samoa',
    },
    'YE': {
        'level': '0',
        'classId': 'YE',
        'text': 'Yemen',
    },
    'YT': {
        'level': '0',
        'classId': 'YT',
        'text': 'Mayotte',
    },
    'ZA': {
        'level': '0',
        'classId': 'ZA',
        'text': 'South Africa',
    },
    'ZM': {
        'level': '0',
        'classId': 'ZM',
        'text': 'Zambia',
    },
    'ZW': {
        'level': '0',
        'classId': 'ZW',
        'text': 'Zimbabwe',
    },
    'CIS': {
        'level': '0',
        'classId': 'CIS',
        'text': 'Commonwealth of Independent States',
    },
    'CN': {
        'level': '0',
        'classId': 'CN',
        'text': 'China',
    },
    'CN-BJ': {
        'level': '0',
        'classId': 'CN-BJ',
        'text': 'Beijing City,China',
    },
    'CN-TJ': {
        'level': '0',
        'classId': 'CN-TJ',
        'text': 'Tianjin City,China',
    },
    'CN-HE': {
        'level': '0',
        'classId': 'CN-HE',
        'text': 'Hebei Province,China',
    },
    'CN-HE-SJW': {
        'level': '0',
        'classId': 'CN-HE-SJW',
        'text': 'Shijiazhuang City,Hebei Province,China',
    },
    'CN-HE-TGS': {
        'level': '0',
        'classId': 'CN-HE-TGS',
        'text': 'Tangshan City,Hebei Province,China',
    },
    'CN-HE-SHP': {
        'level': '0',
        'classId': 'CN-HE-SHP',
        'text': 'Qinhuangdao City,Hebei Province,China',
    },
    'CN-HE-HDS': {
        'level': '0',
        'classId': 'CN-HE-HDS',
        'text': 'Handan City,Hebei Province,China',
    },
    'CN-HE-XTS': {
        'level': '0',
        'classId': 'CN-HE-XTS',
        'text': 'Xingtai City,Hebei Province,China',
    },
    'CN-HE-BDS': {
        'level': '0',
        'classId': 'CN-HE-BDS',
        'text': 'Baoding City,Hebei Province,China',
    },
    'CN-HE-ZJK': {
        'level': '0',
        'classId': 'CN-HE-ZJK',
        'text': 'Zhangjiakou City,Hebei Province,China',
    },
    'CN-HE-CDS': {
        'level': '0',
        'classId': 'CN-HE-CDS',
        'text': 'Chengde City,Hebei Province,China',
    },
    'CN-HE-CGZ': {
        'level': '0',
        'classId': 'CN-HE-CGZ',
        'text': 'Cangzhou City,Hebei Province,China',
    },
    'CN-HE-LFS': {
        'level': '0',
        'classId': 'CN-HE-LFS',
        'text': 'Langfang City,Hebei Province,China',
    },
    'CN-HE-HGS': {
        'level': '0',
        'classId': 'CN-HE-HGS',
        'text': 'Hengshui City,Hebei Province,China',
    },
    'CN-SX': {
        'level': '0',
        'classId': 'CN-SX',
        'text': 'Shanxi Province,China',
    },
    'CN-SX-TYN': {
        'level': '0',
        'classId': 'CN-SX-TYN',
        'text': 'Taiyuan City,Shanxi Province,China',
    },
    'CN-SX-DTG': {
        'level': '0',
        'classId': 'CN-SX-DTG',
        'text': 'Datong City,Shanxi Province,China',
    },
    'CN-SX-YQS': {
        'level': '0',
        'classId': 'CN-SX-YQS',
        'text': 'Yangquan City,Shanxi Province,China',
    },
    'CN-SX-CZS': {
        'level': '0',
        'classId': 'CN-SX-CZS',
        'text': 'Changzhi City,Shanxi Province,China',
    },
    'CN-SX-JCG': {
        'level': '0',
        'classId': 'CN-SX-JCG',
        'text': 'Jincheng City,Shanxi Province,China',
    },
    'CN-SX-SZJ': {
        'level': '0',
        'classId': 'CN-SX-SZJ',
        'text': 'Shuozhou City,Shanxi Province,China',
    },
    'CN-SX-JZN': {
        'level': '0',
        'classId': 'CN-SX-JZN',
        'text': 'Jinzhong City,Shanxi Province,China',
    },
    'CN-SX-YCE': {
        'level': '0',
        'classId': 'CN-SX-YCE',
        'text': 'Yuncheng City,Shanxi Province,China',
    },
    'CN-SX-XZS': {
        'level': '0',
        'classId': 'CN-SX-XZS',
        'text': 'Xinzhou City,Shanxi Province,China',
    },
    'CN-SX-LFN': {
        'level': '0',
        'classId': 'CN-SX-LFN',
        'text': 'Linfen City,Shanxi Province,China',
    },
    'CN-SX-LLH': {
        'level': '0',
        'classId': 'CN-SX-LLH',
        'text': 'Lüliang City,Shanxi Province,China',
    },
    'CN-NM': {
        'level': '0',
        'classId': 'CN-NM',
        'text': 'Inner Mongolia Autonomous Region,China',
    },
    'CN-NM-HET': {
        'level': '0',
        'classId': 'CN-NM-HET',
        'text': 'Hohhot City,Inner Mongolia Autonomous Region,China',
    },
    'CN-NM-BTS': {
        'level': '0',
        'classId': 'CN-NM-BTS',
        'text': 'Baotou City,Inner Mongolia Autonomous Region,China',
    },
    'CN-NM-WHM': {
        'level': '0',
        'classId': 'CN-NM-WHM',
        'text': 'Wuhai City,Inner Mongolia Autonomous Region,China',
    },
    'CN-NM-CFS': {
        'level': '0',
        'classId': 'CN-NM-CFS',
        'text': 'Chifeng(Ulanhad)City,Inner Mongolia Autonomous Region,China',
    },
    'CN-NM-TLO': {
        'level': '0',
        'classId': 'CN-NM-TLO',
        'text': 'Tongliao City,Inner Mongolia Autonomous Region,China',
    },
    'CN-NM-ODS': {
        'level': '0',
        'classId': 'CN-NM-ODS',
        'text': 'Ordos City,Inner Mongolia Autonomous Region,China',
    },
    'CN-NM-HBR': {
        'level': '0',
        'classId': 'CN-NM-HBR',
        'text': 'Hulun Buir City,Inner Mongolia Autonomous Region,China',
    },
    'CN-NM-BYR': {
        'level': '0',
        'classId': 'CN-NM-BYR',
        'text': 'Bayannur City,Inner Mongolia Autonomous Region,China',
    },
    'CN-NM-ULS': {
        'level': '0',
        'classId': 'CN-NM-ULS',
        'text': 'Ulanqab City,Inner Mongolia Autonomous Region,China',
    },
    'CN-NM-HIN': {
        'level': '0',
        'classId': 'CN-NM-HIN',
        'text': 'Hinggan Meng,Inner Mongolia Autonomous Region,China',
    },
    'CN-NM-XGO': {
        'level': '0',
        'classId': 'CN-NM-XGO',
        'text': 'Xilin Gol Meng,Inner Mongolia Autonomous Region,China',
    },
    'CN-NM-ALM': {
        'level': '0',
        'classId': 'CN-NM-ALM',
        'text': 'Alxa Meng,Inner Mongolia Autonomous Region,China',
    },
    'CN-LN': {
        'level': '0',
        'classId': 'CN-LN',
        'text': 'Liaoning Province,China',
    },
    'CN-LN-SHE': {
        'level': '0',
        'classId': 'CN-LN-SHE',
        'text': 'Shenyang City,Liaoning Province,China',
    },
    'CN-LN-DLC': {
        'level': '0',
        'classId': 'CN-LN-DLC',
        'text': 'Dalian City,Liaoning Province,China',
    },
    'CN-LN-ASN': {
        'level': '0',
        'classId': 'CN-LN-ASN',
        'text': 'Anshan City,Liaoning Province,China',
    },
    'CN-LN-FSN': {
        'level': '0',
        'classId': 'CN-LN-FSN',
        'text': 'Fushun City,Liaoning Province,China',
    },
    'CN-LN-BXS': {
        'level': '0',
        'classId': 'CN-LN-BXS',
        'text': 'Benxi City,Liaoning Province,China',
    },
    'CN-LN-DDG': {
        'level': '0',
        'classId': 'CN-LN-DDG',
        'text': 'Dandong City,Liaoning Province,China',
    },
    'CN-LN-JNZ': {
        'level': '0',
        'classId': 'CN-LN-JNZ',
        'text': 'Jinzhou City,Liaoning Province,China',
    },
    'CN-LN-YIK': {
        'level': '0',
        'classId': 'CN-LN-YIK',
        'text': 'Yingkou City,Liaoning Province,China',
    },
    'CN-LN-FXS': {
        'level': '0',
        'classId': 'CN-LN-FXS',
        'text': 'Fuxin City,Liaoning Province,China',
    },
    'CN-LN-LYL': {
        'level': '0',
        'classId': 'CN-LN-LYL',
        'text': 'Liaoyang City,Liaoning Province,China',
    },
    'CN-LN-PJS': {
        'level': '0',
        'classId': 'CN-LN-PJS',
        'text': 'Panjin City,Liaoning Province,China',
    },
    'CN-LN-TLS': {
        'level': '0',
        'classId': 'CN-LN-TLS',
        'text': 'Tieling City,Liaoning Province,China',
    },
    'CN-LN-CYS': {
        'level': '0',
        'classId': 'CN-LN-CYS',
        'text': 'Chaoyang City,Liaoning Province,China',
    },
    'CN-LN-HLD': {
        'level': '0',
        'classId': 'CN-LN-HLD',
        'text': 'Huludao City,Liaoning Province,China',
    },
    'CN-JL': {
        'level': '0',
        'classId': 'CN-JL',
        'text': 'Jilin Province,China',
    },
    'CN-JL-CGQ': {
        'level': '0',
        'classId': 'CN-JL-CGQ',
        'text': 'Changchun City,Jilin Province,China',
    },
    'CN-JL-JLS': {
        'level': '0',
        'classId': 'CN-JL-JLS',
        'text': 'Jilin City,Jilin Province,China',
    },
    'CN-JL-SPS': {
        'level': '0',
        'classId': 'CN-JL-SPS',
        'text': 'Siping City,Jilin Province,China',
    },
    'CN-JL-LYH': {
        'level': '0',
        'classId': 'CN-JL-LYH',
        'text': 'Liaoyuan City,Jilin Province,China',
    },
    'CN-JL-THS': {
        'level': '0',
        'classId': 'CN-JL-THS',
        'text': 'Tonghua City,Jilin Province,China',
    },
    'CN-JL-BSN': {
        'level': '0',
        'classId': 'CN-JL-BSN',
        'text': 'Baishan City,Jilin Province,China',
    },
    'CN-JL-SYU': {
        'level': '0',
        'classId': 'CN-JL-SYU',
        'text': 'Songyuan City,Jilin Province,China',
    },
    'CN-JL-BCS': {
        'level': '0',
        'classId': 'CN-JL-BCS',
        'text': 'Baicheng City,Jilin Province,China',
    },
    'CN-JL-YBZ': {
        'level': '0',
        'classId': 'CN-JL-YBZ',
        'text': 'Yanbian Korean Autonomous Prefecture,Jilin Province,China',
    },
    'CN-HL': {
        'level': '0',
        'classId': 'CN-HL',
        'text': 'Heilongjiang Province,China',
    },
    'CN-HL-HRB': {
        'level': '0',
        'classId': 'CN-HL-HRB',
        'text': 'Harbin City,Heilongjiang Province,China',
    },
    'CN-HL-NDG': {
        'level': '0',
        'classId': 'CN-HL-NDG',
        'text': 'Qiqihar City,Heilongjiang Province,China',
    },
    'CN-HL-JXI': {
        'level': '0',
        'classId': 'CN-HL-JXI',
        'text': 'Jixi City,Heilongjiang Province,China',
    },
    'CN-HL-HEG': {
        'level': '0',
        'classId': 'CN-HL-HEG',
        'text': 'Hegang City,Heilongjiang Province,China',
    },
    'CN-HL-SYS': {
        'level': '0',
        'classId': 'CN-HL-SYS',
        'text': 'Shuangyashan City,Heilongjiang Province,China',
    },
    'CN-HL-DQG': {
        'level': '0',
        'classId': 'CN-HL-DQG',
        'text': 'Daqing City,Heilongjiang Province,China',
    },
    'CN-HL-YCH': {
        'level': '0',
        'classId': 'CN-HL-YCH',
        'text': 'Yichun City,Heilongjiang Province,China',
    },
    'CN-HL-JMU': {
        'level': '0',
        'classId': 'CN-HL-JMU',
        'text': 'Jiamusi City,Heilongjiang Province,China',
    },
    'CN-HL-QTH': {
        'level': '0',
        'classId': 'CN-HL-QTH',
        'text': 'Qitaihe City,Heilongjiang Province,China',
    },
    'CN-HL-MDG': {
        'level': '0',
        'classId': 'CN-HL-MDG',
        'text': 'Mudanjiang City,Heilongjiang Province,China',
    },
    'CN-HL-HEK': {
        'level': '0',
        'classId': 'CN-HL-HEK',
        'text': 'Heihe City,Heilongjiang Province,China',
    },
    'CN-HL-SUH': {
        'level': '0',
        'classId': 'CN-HL-SUH',
        'text': 'Suihua City,Heilongjiang Province,China',
    },
    'CN-HL-DHL': {
        'level': '0',
        'classId': 'CN-HL-DHL',
        'text': 'Da Hinggan Ling Diqu,Heilongjiang Province,China',
    },
    'CN-SH': {
        'level': '0',
        'classId': 'CN-SH',
        'text': 'Shanghai City,China',
    },
    'CN-JS': {
        'level': '0',
        'classId': 'CN-JS',
        'text': 'Jiangsu Province,China',
    },
    'CN-JS-NKG': {
        'level': '0',
        'classId': 'CN-JS-NKG',
        'text': 'Nanjing City,Jiangsu Province,China',
    },
    'CN-JS-WUX': {
        'level': '0',
        'classId': 'CN-JS-WUX',
        'text': 'Wuxi City,Jiangsu Province,China',
    },
    'CN-JS-XUZ': {
        'level': '0',
        'classId': 'CN-JS-XUZ',
        'text': 'Xuzhou City,Jiangsu Province,China',
    },
    'CN-JS-CZX': {
        'level': '0',
        'classId': 'CN-JS-CZX',
        'text': 'Changzhou City,Jiangsu Province,China',
    },
    'CN-JS-SZH': {
        'level': '0',
        'classId': 'CN-JS-SZH',
        'text': 'Suzhou City,Jiangsu Province,China',
    },
    'CN-JS-NTG': {
        'level': '0',
        'classId': 'CN-JS-NTG',
        'text': 'Nantong City,Jiangsu Province,China',
    },
    'CN-JS-LYG': {
        'level': '0',
        'classId': 'CN-JS-LYG',
        'text': 'Lianyungang City,Jiangsu Province,China',
    },
    'CN-JS-HAS': {
        'level': '0',
        'classId': 'CN-JS-HAS',
        'text': 'Huai\'an City,Jiangsu Province,China',
    },
    'CN-JS-YCK': {
        'level': '0',
        'classId': 'CN-JS-YCK',
        'text': 'Yancheng City,Jiangsu Province,China',
    },
    'CN-JS-YZH': {
        'level': '0',
        'classId': 'CN-JS-YZH',
        'text': 'Yangzhou City,Jiangsu Province,China',
    },
    'CN-JS-ZHE': {
        'level': '0',
        'classId': 'CN-JS-ZHE',
        'text': 'Zhenjiang City,Jiangsu Province,China',
    },
    'CN-JS-TZS': {
        'level': '0',
        'classId': 'CN-JS-TZS',
        'text': 'Taizhou City,Jiangsu Province,China',
    },
    'CN-JS-SUQ': {
        'level': '0',
        'classId': 'CN-JS-SUQ',
        'text': 'Suqian City,Jiangsu Province,China',
    },
    'CN-ZJ': {
        'level': '0',
        'classId': 'CN-ZJ',
        'text': 'Zhejiang Province,China',
    },
    'CN-ZJ-HGH': {
        'level': '0',
        'classId': 'CN-ZJ-HGH',
        'text': 'Hangzhou City,Zhejiang Province,China',
    },
    'CN-ZJ-NGB': {
        'level': '0',
        'classId': 'CN-ZJ-NGB',
        'text': 'Ningbo City,Zhejiang Province,China',
    },
    'CN-ZJ-WNZ': {
        'level': '0',
        'classId': 'CN-ZJ-WNZ',
        'text': 'Wenzhou City,Zhejiang Province,China',
    },
    'CN-ZJ-JIX': {
        'level': '0',
        'classId': 'CN-ZJ-JIX',
        'text': 'Jiaxing City,Zhejiang Province,China',
    },
    'CN-ZJ-HZH': {
        'level': '0',
        'classId': 'CN-ZJ-HZH',
        'text': 'Huzhou City,Zhejiang Province,China',
    },
    'CN-ZJ-SXG': {
        'level': '0',
        'classId': 'CN-ZJ-SXG',
        'text': 'Shaoxing City,Zhejiang Province,China',
    },
    'CN-ZJ-JHA': {
        'level': '0',
        'classId': 'CN-ZJ-JHA',
        'text': 'Jinhua City,Zhejiang Province,China',
    },
    'CN-ZJ-QUZ': {
        'level': '0',
        'classId': 'CN-ZJ-QUZ',
        'text': 'Quzhou City,Zhejiang Province,China',
    },
    'CN-ZJ-ZOS': {
        'level': '0',
        'classId': 'CN-ZJ-ZOS',
        'text': 'Zhoushan City,Zhejiang Province,China',
    },
    'CN-ZJ-TZZ': {
        'level': '0',
        'classId': 'CN-ZJ-TZZ',
        'text': 'Taizhou City,Zhejiang Province,China',
    },
    'CN-ZJ-LSS': {
        'level': '0',
        'classId': 'CN-ZJ-LSS',
        'text': 'Lishui City,Zhejiang Province,China',
    },
    'CN-AH': {
        'level': '0',
        'classId': 'CN-AH',
        'text': 'Anhui Province,China',
    },
    'CN-AH-HFE': {
        'level': '0',
        'classId': 'CN-AH-HFE',
        'text': 'Hefei City,Anhui Province,China',
    },
    'CN-AH-WHI': {
        'level': '0',
        'classId': 'CN-AH-WHI',
        'text': 'Wuhu City,Anhui Province,China',
    },
    'CN-AH-BBU': {
        'level': '0',
        'classId': 'CN-AH-BBU',
        'text': 'Bengbu City,Anhui Province,China',
    },
    'CN-AH-HNS': {
        'level': '0',
        'classId': 'CN-AH-HNS',
        'text': 'Huainan City,Anhui Province,China',
    },
    'CN-AH-MAA': {
        'level': '0',
        'classId': 'CN-AH-MAA',
        'text': 'Ma\'anshan City,Anhui Province,China',
    },
    'CN-AH-HBE': {
        'level': '0',
        'classId': 'CN-AH-HBE',
        'text': 'Huaibei City,Anhui Province,China',
    },
    'CN-AH-TOL': {
        'level': '0',
        'classId': 'CN-AH-TOL',
        'text': 'Tongling City,Anhui Province,China',
    },
    'CN-AH-AQG': {
        'level': '0',
        'classId': 'CN-AH-AQG',
        'text': 'Anqing City,Anhui Province,China',
    },
    'CN-AH-HSN': {
        'level': '0',
        'classId': 'CN-AH-HSN',
        'text': 'Huangshan City,Anhui Province,China',
    },
    'CN-AH-CUZ': {
        'level': '0',
        'classId': 'CN-AH-CUZ',
        'text': 'Chuzhou City,Anhui Province,China',
    },
    'CN-AH-FYS': {
        'level': '0',
        'classId': 'CN-AH-FYS',
        'text': 'Fuyang City,Anhui Province,China',
    },
    'CN-AH-SUZ': {
        'level': '0',
        'classId': 'CN-AH-SUZ',
        'text': 'Suzhou City,Anhui Province,China',
    },
    'CN-AH-CAH': {
        'level': '0',
        'classId': 'CN-AH-CAH',
        'text': 'Chaohu City,Anhui Province,China',
    },
    'CN-AH-LAW': {
        'level': '0',
        'classId': 'CN-AH-LAW',
        'text': 'Lu\'an City,Anhui Province,China',
    },
    'CN-AH-BOZ': {
        'level': '0',
        'classId': 'CN-AH-BOZ',
        'text': 'Bozhou City,Anhui Province,China',
    },
    'CN-AH-CIZ': {
        'level': '0',
        'classId': 'CN-AH-CIZ',
        'text': 'Chizhou City,Anhui Province,China',
    },
    'CN-AH-XCI': {
        'level': '0',
        'classId': 'CN-AH-XCI',
        'text': 'Xuancheng City,Anhui Province,China',
    },
    'CN-FJ': {
        'level': '0',
        'classId': 'CN-FJ',
        'text': 'Fujian Province,China',
    },
    'CN-FJ-FOC': {
        'level': '0',
        'classId': 'CN-FJ-FOC',
        'text': 'Fuzhou City,Fujian Province,China',
    },
    'CN-FJ-XMN': {
        'level': '0',
        'classId': 'CN-FJ-XMN',
        'text': 'Xiamen City,Fujian Province,China',
    },
    'CN-FJ-PUT': {
        'level': '0',
        'classId': 'CN-FJ-PUT',
        'text': 'Putian City,Fujian Province,China',
    },
    'CN-FJ-SMS': {
        'level': '0',
        'classId': 'CN-FJ-SMS',
        'text': 'Sanming City,Fujian Province,China',
    },
    'CN-FJ-QZJ': {
        'level': '0',
        'classId': 'CN-FJ-QZJ',
        'text': 'Quanzhou City,Fujian Province,China',
    },
    'CN-FJ-ZZU': {
        'level': '0',
        'classId': 'CN-FJ-ZZU',
        'text': 'Zhangzhou City,Fujian Province,China',
    },
    'CN-FJ-NPS': {
        'level': '0',
        'classId': 'CN-FJ-NPS',
        'text': 'Nanping City,Fujian Province,China',
    },
    'CN-FJ-LYF': {
        'level': '0',
        'classId': 'CN-FJ-LYF',
        'text': 'Longyan City,Fujian Province,China',
    },
    'CN-FJ-NDS': {
        'level': '0',
        'classId': 'CN-FJ-NDS',
        'text': 'Ningde City,Fujian Province,China',
    },
    'CN-JX': {
        'level': '0',
        'classId': 'CN-JX',
        'text': 'Jiangxi Province,China',
    },
    'CN-JX-KHN': {
        'level': '0',
        'classId': 'CN-JX-KHN',
        'text': 'Nanchang City,Jiangxi Province,China',
    },
    'CN-JX-JDZ': {
        'level': '0',
        'classId': 'CN-JX-JDZ',
        'text': 'Jingdezhen City,Jiangxi Province,China',
    },
    'CN-JX-PXS': {
        'level': '0',
        'classId': 'CN-JX-PXS',
        'text': 'Pingxiang City,Jiangxi Province,China',
    },
    'CN-JX-JIU': {
        'level': '0',
        'classId': 'CN-JX-JIU',
        'text': 'Jiujiang City,Jiangxi Province,China',
    },
    'CN-JX-XYU': {
        'level': '0',
        'classId': 'CN-JX-XYU',
        'text': 'Xinyu City,Jiangxi Province,China',
    },
    'CN-JX-YTS': {
        'level': '0',
        'classId': 'CN-JX-YTS',
        'text': 'Yingtan City,Jiangxi Province,China',
    },
    'CN-JX-GZH': {
        'level': '0',
        'classId': 'CN-JX-GZH',
        'text': 'Ganzhou City,Jiangxi Province,China',
    },
    'CN-JX-JAS': {
        'level': '0',
        'classId': 'CN-JX-JAS',
        'text': 'Ji\'an City,Jiangxi Province,China',
    },
    'CN-JX-YCN': {
        'level': '0',
        'classId': 'CN-JX-YCN',
        'text': 'Yichun City,Jiangxi Province,China',
    },
    'CN-JX-FUZ': {
        'level': '0',
        'classId': 'CN-JX-FUZ',
        'text': 'Fuzhou City,Jiangxi Province,China',
    },
    'CN-JX-SRS': {
        'level': '0',
        'classId': 'CN-JX-SRS',
        'text': 'Shangrao City,Jiangxi Province,China',
    },
    'CN-SD': {
        'level': '0',
        'classId': 'CN-SD',
        'text': 'Shandong Province,China',
    },
    'CN-SD-TNA': {
        'level': '0',
        'classId': 'CN-SD-TNA',
        'text': 'Jinan City,Shandong Province,China',
    },
    'CN-SD-TAO': {
        'level': '0',
        'classId': 'CN-SD-TAO',
        'text': 'Qingdao City,Shandong Province,China',
    },
    'CN-SD-ZBO': {
        'level': '0',
        'classId': 'CN-SD-ZBO',
        'text': 'Zibo City,Shandong Province,China',
    },
    'CN-SD-ZZG': {
        'level': '0',
        'classId': 'CN-SD-ZZG',
        'text': 'Zaozhuang City,Shandong Province,China',
    },
    'CN-SD-DYG': {
        'level': '0',
        'classId': 'CN-SD-DYG',
        'text': 'Dongying City,Shandong Province,China',
    },
    'CN-SD-YNT': {
        'level': '0',
        'classId': 'CN-SD-YNT',
        'text': 'Yantai City,Shandong Province,China',
    },
    'CN-SD-WEF': {
        'level': '0',
        'classId': 'CN-SD-WEF',
        'text': 'Weifang City,Shandong Province,China',
    },
    'CN-SD-JNG': {
        'level': '0',
        'classId': 'CN-SD-JNG',
        'text': 'Jining City,Shandong Province,China',
    },
    'CN-SD-TAI': {
        'level': '0',
        'classId': 'CN-SD-TAI',
        'text': 'Tai\'an City,Shandong Province,China',
    },
    'CN-SD-WEH': {
        'level': '0',
        'classId': 'CN-SD-WEH',
        'text': 'Weihai City,Shandong Province,China',
    },
    'CN-SD-RZH': {
        'level': '0',
        'classId': 'CN-SD-RZH',
        'text': 'Rizhao City,Shandong Province,China',
    },
    'CN-SD-LWS': {
        'level': '0',
        'classId': 'CN-SD-LWS',
        'text': 'Laiwu City,Shandong Province,China',
    },
    'CN-SD-LYI': {
        'level': '0',
        'classId': 'CN-SD-LYI',
        'text': 'Linyi City,Shandong Province,China',
    },
    'CN-SD-DZS': {
        'level': '0',
        'classId': 'CN-SD-DZS',
        'text': 'Dezhou City,Shandong Province,China',
    },
    'CN-SD-LCH': {
        'level': '0',
        'classId': 'CN-SD-LCH',
        'text': 'Liaocheng City,Shandong Province,China',
    },
    'CN-SD-BZH': {
        'level': '0',
        'classId': 'CN-SD-BZH',
        'text': 'Binzhou City,Shandong Province,China',
    },
    'CN-SD-HZS': {
        'level': '0',
        'classId': 'CN-SD-HZS',
        'text': 'Heze City,Shandong Province,China',
    },
    'CN-HA': {
        'level': '0',
        'classId': 'CN-HA',
        'text': 'Henan Province,China',
    },
    'CN-HA-CGO': {
        'level': '0',
        'classId': 'CN-HA-CGO',
        'text': 'Zhengzhou City,Henan Province,China',
    },
    'CN-HA-KFS': {
        'level': '0',
        'classId': 'CN-HA-KFS',
        'text': 'Kaifeng City,Henan Province,China',
    },
    'CN-HA-LYA': {
        'level': '0',
        'classId': 'CN-HA-LYA',
        'text': 'Luoyang City,Henan Province,China',
    },
    'CN-HA-PDS': {
        'level': '0',
        'classId': 'CN-HA-PDS',
        'text': 'Pingdingshan City,Henan Province,China',
    },
    'CN-HA-AYS': {
        'level': '0',
        'classId': 'CN-HA-AYS',
        'text': 'Anyang City,Henan Province,China',
    },
    'CN-HA-HBS': {
        'level': '0',
        'classId': 'CN-HA-HBS',
        'text': 'Hebi City,Henan Province,China',
    },
    'CN-HA-XXS': {
        'level': '0',
        'classId': 'CN-HA-XXS',
        'text': 'Xinxiang City,Henan Province,China',
    },
    'CN-HA-JZY': {
        'level': '0',
        'classId': 'CN-HA-JZY',
        'text': 'Jiaozuo City,Henan Province,China',
    },
    'CN-HA-PYS': {
        'level': '0',
        'classId': 'CN-HA-PYS',
        'text': 'Puyang City,Henan Province,China',
    },
    'CN-HA-XCS': {
        'level': '0',
        'classId': 'CN-HA-XCS',
        'text': 'Xuchang City,Henan Province,China',
    },
    'CN-HA-LHS': {
        'level': '0',
        'classId': 'CN-HA-LHS',
        'text': 'Luohe City,Henan Province,China',
    },
    'CN-HA-SMX': {
        'level': '0',
        'classId': 'CN-HA-SMX',
        'text': 'Sanmenxia City,Henan Province,China',
    },
    'CN-HA-NYS': {
        'level': '0',
        'classId': 'CN-HA-NYS',
        'text': 'Nanyang City,Henan Province,China',
    },
    'CN-HA-SQS': {
        'level': '0',
        'classId': 'CN-HA-SQS',
        'text': 'Shangqiu City,Henan Province,China',
    },
    'CN-HA-XYG': {
        'level': '0',
        'classId': 'CN-HA-XYG',
        'text': 'Xinyang City,Henan Province,China',
    },
    'CN-HA-ZKS': {
        'level': '0',
        'classId': 'CN-HA-ZKS',
        'text': 'Zhoukou City,Henan Province,China',
    },
    'CN-HA-ZMD': {
        'level': '0',
        'classId': 'CN-HA-ZMD',
        'text': 'Zhumadian City,Henan Province,China',
    },
    'CN-HB': {
        'level': '0',
        'classId': 'CN-HB',
        'text': 'Hubei Province,China',
    },
    'CN-HB-WUH': {
        'level': '0',
        'classId': 'CN-HB-WUH',
        'text': 'Wuhan City,Hubei Province,China',
    },
    'CN-HB-HSI': {
        'level': '0',
        'classId': 'CN-HB-HSI',
        'text': 'Huangshi City,Hubei Province,China',
    },
    'CN-HB-SYE': {
        'level': '0',
        'classId': 'CN-HB-SYE',
        'text': 'Shiyan City,Hubei Province,China',
    },
    'CN-HB-YCO': {
        'level': '0',
        'classId': 'CN-HB-YCO',
        'text': 'Yichang City,Hubei Province,China',
    },
    'CN-HB-XFN': {
        'level': '0',
        'classId': 'CN-HB-XFN',
        'text': 'Xiangfan City,Hubei Province,China',
    },
    'CN-HB-EZS': {
        'level': '0',
        'classId': 'CN-HB-EZS',
        'text': 'Ezhou City,Hubei Province,China',
    },
    'CN-HB-JMS': {
        'level': '0',
        'classId': 'CN-HB-JMS',
        'text': 'Jingmen City,Hubei Province,China',
    },
    'CN-HB-XGE': {
        'level': '0',
        'classId': 'CN-HB-XGE',
        'text': 'Xiaogan City,Hubei Province,China',
    },
    'CN-HB-JGZ': {
        'level': '0',
        'classId': 'CN-HB-JGZ',
        'text': 'Jingzhou City,Hubei Province,China',
    },
    'CN-HB-HGE': {
        'level': '0',
        'classId': 'CN-HB-HGE',
        'text': 'Huanggang City,Hubei Province,China',
    },
    'CN-HB-XNS': {
        'level': '0',
        'classId': 'CN-HB-XNS',
        'text': 'Xianning City,Hubei Province,China',
    },
    'CN-HB-SZR': {
        'level': '0',
        'classId': 'CN-HB-SZR',
        'text': 'Suizhou City,Hubei Province,China',
    },
    'CN-HB-ESH': {
        'level': '0',
        'classId': 'CN-HB-ESH',
        'text': 'Enshi Tujia&Miao Autonomous Prefecture,Hubei Province,China',
    },
    'CN-HN': {
        'level': '0',
        'classId': 'CN-HN',
        'text': 'Hunan Province,China',
    },
    'CN-HN-CSX': {
        'level': '0',
        'classId': 'CN-HN-CSX',
        'text': 'Changsha City,Hunan Province,China',
    },
    'CN-HN-ZZS': {
        'level': '0',
        'classId': 'CN-HN-ZZS',
        'text': 'Zhuzhou City,Hunan Province,China',
    },
    'CN-HN-XGT': {
        'level': '0',
        'classId': 'CN-HN-XGT',
        'text': 'Xiangtan City,Hunan Province,China',
    },
    'CN-HN-HNY': {
        'level': '0',
        'classId': 'CN-HN-HNY',
        'text': 'Hengyang City,Hunan Province,China',
    },
    'CN-HN-SYR': {
        'level': '0',
        'classId': 'CN-HN-SYR',
        'text': 'Shaoyang City,Hunan Province,China',
    },
    'CN-HN-YYG': {
        'level': '0',
        'classId': 'CN-HN-YYG',
        'text': 'Yueyang City,Hunan Province,China',
    },
    'CN-HN-CDE': {
        'level': '0',
        'classId': 'CN-HN-CDE',
        'text': 'Changde City,Hunan Province,China',
    },
    'CN-HN-ZJJ': {
        'level': '0',
        'classId': 'CN-HN-ZJJ',
        'text': 'Zhangjiajie City,Hunan Province,China',
    },
    'CN-HN-YYS': {
        'level': '0',
        'classId': 'CN-HN-YYS',
        'text': 'Yiyang City,Hunan Province,China',
    },
    'CN-HN-CNZ': {
        'level': '0',
        'classId': 'CN-HN-CNZ',
        'text': 'Chenzhou City,Hunan Province,China',
    },
    'CN-HN-YZS': {
        'level': '0',
        'classId': 'CN-HN-YZS',
        'text': 'Yongzhou City,Hunan Province,China',
    },
    'CN-HN-HHS': {
        'level': '0',
        'classId': 'CN-HN-HHS',
        'text': 'Huaihua City,Hunan Province,China',
    },
    'CN-HN-LDI': {
        'level': '0',
        'classId': 'CN-HN-LDI',
        'text': 'Loudi City,Hunan Province,China',
    },
    'CN-HN-XXZ': {
        'level': '0',
        'classId': 'CN-HN-XXZ',
        'text': '​Xiangxi Tujia&Miao Autonomous Prefecture​,Hunan Province,China',
    },
    'CN-GD': {
        'level': '0',
        'classId': 'CN-GD',
        'text': 'Guangdong Province,China',
    },
    'CN-GD-CAN': {
        'level': '0',
        'classId': 'CN-GD-CAN',
        'text': 'Guangzhou City,Guangdong Province,China',
    },
    'CN-GD-HSC': {
        'level': '0',
        'classId': 'CN-GD-HSC',
        'text': 'Shaoguan City,Guangdong Province,China',
    },
    'CN-GD-SZX': {
        'level': '0',
        'classId': 'CN-GD-SZX',
        'text': 'Shenzhen City,Guangdong Province,China',
    },
    'CN-GD-ZUH': {
        'level': '0',
        'classId': 'CN-GD-ZUH',
        'text': 'Zhuhai City,Guangdong Province,China',
    },
    'CN-GD-SWA': {
        'level': '0',
        'classId': 'CN-GD-SWA',
        'text': 'Shantou City,Guangdong Province,China',
    },
    'CN-GD-FOS': {
        'level': '0',
        'classId': 'CN-GD-FOS',
        'text': 'Foshan City,Guangdong Province,China',
    },
    'CN-GD-JMN': {
        'level': '0',
        'classId': 'CN-GD-JMN',
        'text': 'Jiangmen City,Guangdong Province,China',
    },
    'CN-GD-ZHA': {
        'level': '0',
        'classId': 'CN-GD-ZHA',
        'text': 'Zhanjiang City,Guangdong Province,China',
    },
    'CN-GD-MMI': {
        'level': '0',
        'classId': 'CN-GD-MMI',
        'text': 'Maoming City,Guangdong Province,China',
    },
    'CN-GD-ZQG': {
        'level': '0',
        'classId': 'CN-GD-ZQG',
        'text': 'Zhaoqing City,Guangdong Province,China',
    },
    'CN-GD-HUI': {
        'level': '0',
        'classId': 'CN-GD-HUI',
        'text': 'Huizhou City,Guangdong Province,China',
    },
    'CN-GD-MXZ': {
        'level': '0',
        'classId': 'CN-GD-MXZ',
        'text': 'Meizhou City,Guangdong Province,China',
    },
    'CN-GD-SWE': {
        'level': '0',
        'classId': 'CN-GD-SWE',
        'text': 'Shanwei City,Guangdong Province,China',
    },
    'CN-GD-HEY': {
        'level': '0',
        'classId': 'CN-GD-HEY',
        'text': 'Heyuan City,Guangdong Province,China',
    },
    'CN-GD-YJI': {
        'level': '0',
        'classId': 'CN-GD-YJI',
        'text': 'Yangjiang City,Guangdong Province,China',
    },
    'CN-GD-QYN': {
        'level': '0',
        'classId': 'CN-GD-QYN',
        'text': 'Qingyuan City,Guangdong Province,China',
    },
    'CN-GD-DGG': {
        'level': '0',
        'classId': 'CN-GD-DGG',
        'text': 'Dongguan City,Guangdong Province,China',
    },
    'CN-GD-ZSN': {
        'level': '0',
        'classId': 'CN-GD-ZSN',
        'text': 'Zhongshan City,Guangdong Province,China',
    },
    'CN-GD-CZY': {
        'level': '0',
        'classId': 'CN-GD-CZY',
        'text': 'Chaozhou City,Guangdong Province,China',
    },
    'CN-GD-JIY': {
        'level': '0',
        'classId': 'CN-GD-JIY',
        'text': 'Jieyang City,Guangdong Province,China',
    },
    'CN-GD-YFS': {
        'level': '0',
        'classId': 'CN-GD-YFS',
        'text': 'Yunfu City,Guangdong Province,China',
    },
    'CN-GX': {
        'level': '0',
        'classId': 'CN-GX',
        'text': 'Guangxi Zhuang Autonomous Region,China',
    },
    'CN-GX-NNG': {
        'level': '0',
        'classId': 'CN-GX-NNG',
        'text': 'Nanning City,Guangxi Zhuang Autonomous Region,China',
    },
    'CN-GX-LZH': {
        'level': '0',
        'classId': 'CN-GX-LZH',
        'text': 'Liuzhou City,Guangxi Zhuang Autonomous Region,China',
    },
    'CN-GX-KWL': {
        'level': '0',
        'classId': 'CN-GX-KWL',
        'text': 'Guilin City,Guangxi Zhuang Autonomous Region,China',
    },
    'CN-GX-WUZ': {
        'level': '0',
        'classId': 'CN-GX-WUZ',
        'text': 'Wuzhou City,Guangxi Zhuang Autonomous Region,China',
    },
    'CN-GX-BHY': {
        'level': '0',
        'classId': 'CN-GX-BHY',
        'text': 'Beihai City,Guangxi Zhuang Autonomous Region,China',
    },
    'CN-GX-FAN': {
        'level': '0',
        'classId': 'CN-GX-FAN',
        'text': 'Fangchenggang City,Guangxi Zhuang Autonomous Region,China',
    },
    'CN-GX-QZH': {
        'level': '0',
        'classId': 'CN-GX-QZH',
        'text': 'Qinzhou City,Guangxi Zhuang Autonomous Region,China',
    },
    'CN-GX-GUG': {
        'level': '0',
        'classId': 'CN-GX-GUG',
        'text': 'Guigang City,Guangxi Zhuang Autonomous Region,China',
    },
    'CN-GX-YUL': {
        'level': '0',
        'classId': 'CN-GX-YUL',
        'text': 'Yulin City,Guangxi Zhuang Autonomous Region,China',
    },
    'CN-GX-BSS': {
        'level': '0',
        'classId': 'CN-GX-BSS',
        'text': 'Bose City,Guangxi Zhuang Autonomous Region,China',
    },
    'CN-GX-HZO': {
        'level': '0',
        'classId': 'CN-GX-HZO',
        'text': 'Hezhou City,Guangxi Zhuang Autonomous Region,China',
    },
    'CN-GX-HCS': {
        'level': '0',
        'classId': 'CN-GX-HCS',
        'text': 'Hechi City,Guangxi Zhuang Autonomous Region,China',
    },
    'CN-GX-LIB': {
        'level': '0',
        'classId': 'CN-GX-LIB',
        'text': 'Laibin City,Guangxi Zhuang Autonomous Region,China',
    },
    'CN-GX-COZ': {
        'level': '0',
        'classId': 'CN-GX-COZ',
        'text': 'Chongzuo City,Guangxi Zhuang Autonomous Region,China',
    },
    'CN-HI': {
        'level': '0',
        'classId': 'CN-HI',
        'text': 'Hainan Province,China',
    },
    'CN-HI-HAK': {
        'level': '0',
        'classId': 'CN-HI-HAK',
        'text': 'Haikou City,Hainan Province,China',
    },
    'CN-HI-SYX': {
        'level': '0',
        'classId': 'CN-HI-SYX',
        'text': 'Sanva City,Hainan Province,China',
    },
    'CN-CQ': {
        'level': '0',
        'classId': 'CN-CQ',
        'text': 'Chongqing City,China',
    },
    'CN-SC': {
        'level': '0',
        'classId': 'CN-SC',
        'text': 'Sichuan Province,China',
    },
    'CN-SC-CTU': {
        'level': '0',
        'classId': 'CN-SC-CTU',
        'text': 'Chengdu City,Sichuan Province,China',
    },
    'CN-SC-ZGS': {
        'level': '0',
        'classId': 'CN-SC-ZGS',
        'text': 'Zigong City,Sichuan Province,China',
    },
    'CN-SC-PZH': {
        'level': '0',
        'classId': 'CN-SC-PZH',
        'text': 'Panzhihua City,Sichuan Province,China',
    },
    'CN-SC-LUZ': {
        'level': '0',
        'classId': 'CN-SC-LUZ',
        'text': 'Luzhou City,Sichuan Province,China',
    },
    'CN-SC-DEY': {
        'level': '0',
        'classId': 'CN-SC-DEY',
        'text': 'Deyang City,Sichuan Province,China',
    },
    'CN-SC-MYG': {
        'level': '0',
        'classId': 'CN-SC-MYG',
        'text': 'Mianyang City,Sichuan Province,China',
    },
    'CN-SC-GYC': {
        'level': '0',
        'classId': 'CN-SC-GYC',
        'text': 'Guangyuan City,Sichuan Province,China',
    },
    'CN-SC-SNS': {
        'level': '0',
        'classId': 'CN-SC-SNS',
        'text': 'Suining City,Sichuan Province,China',
    },
    'CN-SC-NJS': {
        'level': '0',
        'classId': 'CN-SC-NJS',
        'text': 'Neijiang City,Sichuan Province,China',
    },
    'CN-SC-LES': {
        'level': '0',
        'classId': 'CN-SC-LES',
        'text': 'Leshan City,Sichuan Province,China',
    },
    'CN-SC-NCO': {
        'level': '0',
        'classId': 'CN-SC-NCO',
        'text': 'Nanchong City,Sichuan Province,China',
    },
    'CN-SC-MSS': {
        'level': '0',
        'classId': 'CN-SC-MSS',
        'text': 'Meishan City,Sichuan Province,China',
    },
    'CN-SC-YBS': {
        'level': '0',
        'classId': 'CN-SC-YBS',
        'text': 'Yibin City,Sichuan Province,China',
    },
    'CN-SC-GAC': {
        'level': '0',
        'classId': 'CN-SC-GAC',
        'text': 'Guang\'an City,Sichuan Province,China',
    },
    'CN-SC-DAZ': {
        'level': '0',
        'classId': 'CN-SC-DAZ',
        'text': 'Dazhou City,Sichuan Province,China',
    },
    'CN-SC-YAS': {
        'level': '0',
        'classId': 'CN-SC-YAS',
        'text': 'Ya\'an City,Sichuan Province,China',
    },
    'CN-SC-BZS': {
        'level': '0',
        'classId': 'CN-SC-BZS',
        'text': 'Bazhong City,Sichuan Province,China',
    },
    'CN-SC-ZYS': {
        'level': '0',
        'classId': 'CN-SC-ZYS',
        'text': 'Ziyang City,Sichuan Province,China',
    },
    'CN-SC-ABA': {
        'level': '0',
        'classId': 'CN-SC-ABA',
        'text': 'Aba Tibetan&Qiang Autonomous Prefecture,Sichuan Province,China',
    },
    'CN-SC-GAZ': {
        'level': '0',
        'classId': 'CN-SC-GAZ',
        'text': 'Garzê Tibetan Autonomous Prefecture,Sichuan Province,China',
    },
    'CN-SC-LSY': {
        'level': '0',
        'classId': 'CN-SC-LSY',
        'text': 'Liangshan Yi Autonomous Prefecture​,Sichuan Province,China',
    },
    'CN-GZ': {
        'level': '0',
        'classId': 'CN-GZ',
        'text': 'Guizhou Province,China',
    },
    'CN-GZ-KWE': {
        'level': '0',
        'classId': 'CN-GZ-KWE',
        'text': 'Guiyang City,Guizhou Province,China',
    },
    'CN-GZ-LPS': {
        'level': '0',
        'classId': 'CN-GZ-LPS',
        'text': 'Lupanshui City,Guizhou Province,China',
    },
    'CN-GZ-ZNY': {
        'level': '0',
        'classId': 'CN-GZ-ZNY',
        'text': 'Zunyi City,Guizhou Province,China',
    },
    'CN-GZ-ASS': {
        'level': '0',
        'classId': 'CN-GZ-ASS',
        'text': 'Anshun City,Guizhou Province,China',
    },
    'CN-GZ-TRD': {
        'level': '0',
        'classId': 'CN-GZ-TRD',
        'text': 'Tongren Diqu,Guizhou Province,China',
    },
    'CN-GZ-QXZ': {
        'level': '0',
        'classId': 'CN-GZ-QXZ',
        'text': 'Qianxinan Buyei&Miao Autonomous Prefecture,Guizhou Province,China',
    },
    'CN-GZ-BJD': {
        'level': '0',
        'classId': 'CN-GZ-BJD',
        'text': 'Bijie Diqu,Guizhou Province,China',
    },
    'CN-GZ-QND': {
        'level': '0',
        'classId': 'CN-GZ-QND',
        'text': 'Qiandongnan Miao&Dong Autonomous Prefecture,Guizhou Province,China',
    },
    'CN-GZ-QNZ': {
        'level': '0',
        'classId': 'CN-GZ-QNZ',
        'text': '​Qiannan Buyei&Miao Autonomous Prefecture,Guizhou Province,China',
    },
    'CN-YN': {
        'level': '0',
        'classId': 'CN-YN',
        'text': 'Yunnan Province,China',
    },
    'CN-YN-KMG': {
        'level': '0',
        'classId': 'CN-YN-KMG',
        'text': 'Kunming City,Yunnan Province,China',
    },
    'CN-YN-QJS': {
        'level': '0',
        'classId': 'CN-YN-QJS',
        'text': 'Qujing City,Yunnan Province,China',
    },
    'CN-YN-YXS': {
        'level': '0',
        'classId': 'CN-YN-YXS',
        'text': 'Yuxi City,Yunnan Province,China',
    },
    'CN-YN-BOS': {
        'level': '0',
        'classId': 'CN-YN-BOS',
        'text': 'Baoshan City,Yunnan Province,China',
    },
    'CN-YN-ZTS': {
        'level': '0',
        'classId': 'CN-YN-ZTS',
        'text': 'Zhaotong City,Yunnan Province,China',
    },
    'CN-YN-LJH': {
        'level': '0',
        'classId': 'CN-YN-LJH',
        'text': 'Lijiang City,Yunnan Province,China',
    },
    'CN-YN-PRS': {
        'level': '0',
        'classId': 'CN-YN-PRS',
        'text': 'Pu\'er City,Yunnan Province,China',
    },
    'CN-YN-LIH': {
        'level': '0',
        'classId': 'CN-YN-LIH',
        'text': 'Lincang City,Yunnan Province,China',
    },
    'CN-YN-CXD': {
        'level': '0',
        'classId': 'CN-YN-CXD',
        'text': '​Chuxiong Yi Autonomous Prefecture,Yunnan Province,China',
    },
    'CN-YN-HHZ': {
        'level': '0',
        'classId': 'CN-YN-HHZ',
        'text': '​Honghe Hani&Yi Autonomous Prefecture,Yunnan Province,China',
    },
    'CN-YN-WSZ': {
        'level': '0',
        'classId': 'CN-YN-WSZ',
        'text': '​Wenshan Zhuang&Miao Autonomous Prefecture,Yunnan Province,China',
    },
    'CN-YN-XSB': {
        'level': '0',
        'classId': 'CN-YN-XSB',
        'text': 'Xishuangbanna Dai Autonomous Prefecture,Yunnan Province,China',
    },
    'CN-YN-DLZ': {
        'level': '0',
        'classId': 'CN-YN-DLZ',
        'text': '​Dali Bai Autonomous Prefecture,Yunnan Province,China',
    },
    'CN-YN-DHG': {
        'level': '0',
        'classId': 'CN-YN-DHG',
        'text': 'Dehong Dai&Jingpo Autonomous Prefecture,Yunnan Province,China',
    },
    'CN-YN-NUJ': {
        'level': '0',
        'classId': 'CN-YN-NUJ',
        'text': 'Nujiang Lisu Autonomous Prefecture,Yunnan Province,China',
    },
    'CN-YN-DEZ': {
        'level': '0',
        'classId': 'CN-YN-DEZ',
        'text': 'Deqên Tibetan Autonomous Prefecture,Yunnan Province,China',
    },
    'CN-XZ': {
        'level': '0',
        'classId': 'CN-XZ',
        'text': 'Tibet Autonomous Region,China',
    },
    'CN-XZ-LXA': {
        'level': '0',
        'classId': 'CN-XZ-LXA',
        'text': 'Lhasa City,Tibet Autonomous Region,China',
    },
    'CN-XZ-QAD': {
        'level': '0',
        'classId': 'CN-XZ-QAD',
        'text': 'Qamdo Diqu,Tibet Autonomous Region,China',
    },
    'CN-XZ-SND': {
        'level': '0',
        'classId': 'CN-XZ-SND',
        'text': 'Shannan Diqu,Tibet Autonomous Region,China',
    },
    'CN-XZ-XID': {
        'level': '0',
        'classId': 'CN-XZ-XID',
        'text': 'Xigaze Diqu,Tibet Autonomous Region,China',
    },
    'CN-XZ-NAD': {
        'level': '0',
        'classId': 'CN-XZ-NAD',
        'text': 'Nagqu Diqu,Tibet Autonomous Region,China',
    },
    'CN-XZ-NGD': {
        'level': '0',
        'classId': 'CN-XZ-NGD',
        'text': 'Ngari Diqu,Tibet Autonomous Region,China',
    },
    'CN-XZ-NYD': {
        'level': '0',
        'classId': 'CN-XZ-NYD',
        'text': 'Nyingchi Diqu,Tibet Autonomous Region,China',
    },
    'CN-SN': {
        'level': '0',
        'classId': 'CN-SN',
        'text': 'Shaanxi Province,China',
    },
    'CN-SN-SIA': {
        'level': '0',
        'classId': 'CN-SN-SIA',
        'text': 'Xi\'an City,Shaanxi Province,China',
    },
    'CN-SN-TCN': {
        'level': '0',
        'classId': 'CN-SN-TCN',
        'text': 'Tongchuan City,Shaanxi Province,China',
    },
    'CN-SN-BJI': {
        'level': '0',
        'classId': 'CN-SN-BJI',
        'text': 'Baoji City,Shaanxi Province,China',
    },
    'CN-SN-XYS': {
        'level': '0',
        'classId': 'CN-SN-XYS',
        'text': 'Xianyang City,Shaanxi Province,China',
    },
    'CN-SN-WNA': {
        'level': '0',
        'classId': 'CN-SN-WNA',
        'text': 'Weinan City,Shaanxi Province,China',
    },
    'CN-SN-YNA': {
        'level': '0',
        'classId': 'CN-SN-YNA',
        'text': 'Yan\'an City,Shaanxi Province,China',
    },
    'CN-SN-HZJ': {
        'level': '0',
        'classId': 'CN-SN-HZJ',
        'text': 'Hanzhong City,Shaanxi Province,China',
    },
    'CN-SN-YLN': {
        'level': '0',
        'classId': 'CN-SN-YLN',
        'text': 'Yulin City,Shaanxi Province,China',
    },
    'CN-SN-ANK': {
        'level': '0',
        'classId': 'CN-SN-ANK',
        'text': 'Ankang City,Shaanxi Province,China',
    },
    'CN-SN-SLH': {
        'level': '0',
        'classId': 'CN-SN-SLH',
        'text': 'Shangluo City,Shaanxi Province,China',
    },
    'CN-GS': {
        'level': '0',
        'classId': 'CN-GS',
        'text': 'Gansu Province,China',
    },
    'CN-GS-LHW': {
        'level': '0',
        'classId': 'CN-GS-LHW',
        'text': 'Lanzhou City,Gansu Province,China',
    },
    'CN-GS-JYG': {
        'level': '0',
        'classId': 'CN-GS-JYG',
        'text': 'Jiayuguan City,Gansu Province,China',
    },
    'CN-GS-JCS': {
        'level': '0',
        'classId': 'CN-GS-JCS',
        'text': 'Jinchang City,Gansu Province,China',
    },
    'CN-GS-BYS': {
        'level': '0',
        'classId': 'CN-GS-BYS',
        'text': 'Baiyin City,Gansu Province,China',
    },
    'CN-GS-TSU': {
        'level': '0',
        'classId': 'CN-GS-TSU',
        'text': 'Tianshui City,Gansu Province,China',
    },
    'CN-GS-WWS': {
        'level': '0',
        'classId': 'CN-GS-WWS',
        'text': 'Wuwei City,Gansu Province,China',
    },
    'CN-GS-ZYE': {
        'level': '0',
        'classId': 'CN-GS-ZYE',
        'text': 'Zhangye City,Gansu Province,China',
    },
    'CN-GS-PLS': {
        'level': '0',
        'classId': 'CN-GS-PLS',
        'text': 'Pingliang City,Gansu Province,China',
    },
    'CN-GS-JQG': {
        'level': '0',
        'classId': 'CN-GS-JQG',
        'text': 'Jiuquan City,Gansu Province,China',
    },
    'CN-GS-QYI': {
        'level': '0',
        'classId': 'CN-GS-QYI',
        'text': 'Qingyang City,Gansu Province,China',
    },
    'CN-GS-DNX': {
        'level': '0',
        'classId': 'CN-GS-DNX',
        'text': 'Dingxi City,Gansu Province,China',
    },
    'CN-GS-LGN': {
        'level': '0',
        'classId': 'CN-GS-LGN',
        'text': 'Longnan City,Gansu Province,China',
    },
    'CN-GS-LXH': {
        'level': '0',
        'classId': 'CN-GS-LXH',
        'text': '​Linxia Hui Autonomous Prefecture,Gansu Province,China',
    },
    'CN-GS-GNZ': {
        'level': '0',
        'classId': 'CN-GS-GNZ',
        'text': 'Gannan Tibetan Autonomous Prefecture,Gansu Province,China',
    },
    'CN-QH': {
        'level': '0',
        'classId': 'CN-QH',
        'text': 'Qinghai Province,China',
    },
    'CN-QH-XNN': {
        'level': '0',
        'classId': 'CN-QH-XNN',
        'text': 'Xining City,Qinghai Province,China',
    },
    'CN-QH-HDD': {
        'level': '0',
        'classId': 'CN-QH-HDD',
        'text': 'Haidong Diqu,Qinghai Province,China',
    },
    'CN-QH-HBZ': {
        'level': '0',
        'classId': 'CN-QH-HBZ',
        'text': 'Haibei Tibetan Autonomous Prefecture,Qinghai Province,China',
    },
    'CN-QH-HN7': {
        'level': '0',
        'classId': 'CN-QH-HN7',
        'text': 'Huangnan Tibetan Autonomous Prefecture,Qinghai Province,China',
    },
    'CN-QH-HNN': {
        'level': '0',
        'classId': 'CN-QH-HNN',
        'text': 'Hainan Tibetan Autonomous Prefecture,Qinghai Province,China',
    },
    'CN-QH-GOL': {
        'level': '0',
        'classId': 'CN-QH-GOL',
        'text': 'Golog Tibetan Autonomous Prefecture,Qinghai Province,China',
    },
    'CN-QH-YSZ': {
        'level': '0',
        'classId': 'CN-QH-YSZ',
        'text': 'Yushu Tibetan Autonomous Prefecture,Qinghai Province,China',
    },
    'CN-QH-HXZ': {
        'level': '0',
        'classId': 'CN-QH-HXZ',
        'text': 'Haixi Mongol&Tibetan Autonomous Prefecture,Qinghai Province,China',
    },
    'CN-NX': {
        'level': '0',
        'classId': 'CN-NX',
        'text': 'Ningxia Hui Autonomous Region,China',
    },
    'CN-NX-INC': {
        'level': '0',
        'classId': 'CN-NX-INC',
        'text': 'Yinchuan City,Ningxia Hui Autonomous Region,China',
    },
    'CN-NX-SZS': {
        'level': '0',
        'classId': 'CN-NX-SZS',
        'text': 'Shizuishan City,Ningxia Hui Autonomous Region,China',
    },
    'CN-NX-WZS': {
        'level': '0',
        'classId': 'CN-NX-WZS',
        'text': 'Wuzhong City,Ningxia Hui Autonomous Region,China',
    },
    'CN-NX-GYN': {
        'level': '0',
        'classId': 'CN-NX-GYN',
        'text': 'Guyuan City,Ningxia Hui Autonomous Region,China',
    },
    'CN-NX-ZWS': {
        'level': '0',
        'classId': 'CN-NX-ZWS',
        'text': 'Zhongwei City,Ningxia Hui Autonomous Region,China',
    },
    'CN-XJ': {
        'level': '0',
        'classId': 'CN-XJ',
        'text': 'Xinjiang Uygur Autonomous Region,China',
    },
    'CN-XJ-URC': {
        'level': '0',
        'classId': 'CN-XJ-URC',
        'text': 'Urümqi City,Xinjiang Uygur Autonomous Region,China',
    },
    'CN-XJ-KAR': {
        'level': '0',
        'classId': 'CN-XJ-KAR',
        'text': 'Karamay City,Xinjiang Uygur Autonomous Region,China',
    },
    'CN-XJ-TUD': {
        'level': '0',
        'classId': 'CN-XJ-TUD',
        'text': 'Turpan Diqu,Xinjiang Uygur Autonomous Region,China',
    },
    'CN-XJ-HMD': {
        'level': '0',
        'classId': 'CN-XJ-HMD',
        'text': 'Hami(Kumul)Diqu,Xinjiang Uygur Autonomous Region,China',
    },
    'CN-XJ-CJZ': {
        'level': '0',
        'classId': 'CN-XJ-CJZ',
        'text': 'Changji Hui Autonomous Prefecture,Xinjiang Uygur Autonomous Region,China',
    },
    'CN-XJ-BOR': {
        'level': '0',
        'classId': 'CN-XJ-BOR',
        'text': 'Bortala Mongol Autonomous Prefecture,Xinjiang Uygur Autonomous Region,China',
    },
    'CN-XJ-BAG': {
        'level': '0',
        'classId': 'CN-XJ-BAG',
        'text': 'Bayingolin Mongol Autonomous Prefecture,Xinjiang Uygur Autonomous Region,China',
    },
    'CN-XJ-AKD': {
        'level': '0',
        'classId': 'CN-XJ-AKD',
        'text': 'Aksu Diqu,Xinjiang Uygur Autonomous Region,China',
    },
    'CN-XJ-KIZ': {
        'level': '0',
        'classId': 'CN-XJ-KIZ',
        'text': '​Kizilsu Kirgiz Autonomous Prefecture,Xinjiang Uygur Autonomous Region,China',
    },
    'CN-XJ-KSI': {
        'level': '0',
        'classId': 'CN-XJ-KSI',
        'text': 'Kashi(Kaxgar)Diqu,Xinjiang Uygur Autonomous Region,China',
    },
    'CN-XJ-HOD': {
        'level': '0',
        'classId': 'CN-XJ-HOD',
        'text': 'Hotan Diqu,Xinjiang Uygur Autonomous Region,China',
    },
    'CN-XJ-ILD': {
        'level': '0',
        'classId': 'CN-XJ-ILD',
        'text': '​Ili Kazak Autonomous Prefecture,Xinjiang Uygur Autonomous Region,China',
    },
    'CN-XJ-TCD': {
        'level': '0',
        'classId': 'CN-XJ-TCD',
        'text': 'Tacheng(Qoqek)Diqu,Xinjiang Uygur Autonomous Region,China',
    },
    'CN-XJ-ALD': {
        'level': '0',
        'classId': 'CN-XJ-ALD',
        'text': 'Altay Diqu,Xinjiang Uygur Autonomous Region,China',
    },
    'CN-TW': {
        'level': '0',
        'classId': 'CN-TW',
        'text': 'Taiwan Province,China',
    },
    'CN-HK': {
        'level': '0',
        'classId': 'CN-HK',
        'text': 'Hong Kong Special Administrative Region of the People\'s Republic of China',
    },
    'CN-MO': {
        'level': '0',
        'classId': 'CN-MO',
        'text': 'Macao Special Administrative Region of the People\'s Republic of China',
    },
}


__all__ = ['Locations', 'TidasLocationsText', 'LocationsCategoryData', 'LOCATIONS_CATEGORIES']
