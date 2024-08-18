import bisect

import arrow

# timestamps for fullmoons between year 2000 and 2099
# data source http://home.hiwaay.net/~krcool/Astro/moon/fullmoon.htm

fullmoons = [
    948429720,
    950977680,
    953527560,
    956079780,
    958635300,
    961194480,
    963755820,
    966316440,
    968873880,
    971427240,
    973977360,
    976525500,
    979071960,
    981616380,
    984158640,
    986700240,
    989243700,
    991791660,
    994345560,
    996904620,
    999467040,
    1002030600,
    1004593320,
    1007153400,
    1009708920,
    1012258320,
    1014801480,
    1017340020,
    1019876580,
    1022414040,
    1024955100,
    1027501680,
    1030055400,
    1032616800,
    1035184860,
    1037756100,
    1040325060,
    1042886940,
    1045439520,
    1047983760,
    1050521880,
    1053056280,
    1055589480,
    1058124180,
    1060663740,
    1063211820,
    1065770940,
    1068340500,
    1070915880,
    1073490060,
    1076057280,
    1078614960,
    1081163040,
    1083702900,
    1086236460,
    1088766600,
    1091297160,
    1093832580,
    1096377000,
    1098932940,
    1101499740,
    1104073680,
    1106649180,
    1109220900,
    1111784400,
    1114337280,
    1116879600,
    1119413700,
    1121943660,
    1124474040,
    1127008860,
    1129551300,
    1132102740,
    1134663420,
    1137232140,
    1139805900,
    1142379420,
    1144946520,
    1147503180,
    1150049040,
    1152586980,
    1155120840,
    1157654520,
    1160190780,
    1162731540,
    1165278360,
    1167832740,
    1170395220,
    1172963880,
    1175534160,
    1178100660,
    1180659900,
    1183211400,
    1185756480,
    1188297300,
    1190835960,
    1193374380,
    1195914660,
    1198459020,
    1201008960,
    1203564720,
    1206124860,
    1208687220,
    1211249580,
    1213810320,
    1216368000,
    1218921480,
    1221470100,
    1224014640,
    1226557140,
    1229099940,
    1231644480,
    1234191060,
    1236739200,
    1239289080,
    1241841780,
    1244398380,
    1246958580,
    1249520220,
    1252080300,
    1254636660,
    1257189300,
    1259739180,
    1262286900,
    1264832340,
    1267375200,
    1269916080,
    1272457260,
    1275001740,
    1277551920,
    1280108280,
    1282669560,
    1285233540,
    1287797880,
    1290360480,
    1292919300,
    1295472180,
    1298018280,
    1300558320,
    1303094760,
    1305630600,
    1308168900,
    1310712060,
    1313261940,
    1315819680,
    1318385280,
    1320956280,
    1323527820,
    1326094260,
    1328651760,
    1331199720,
    1333740060,
    1336275420,
    1338808380,
    1341341640,
    1343878140,
    1346421600,
    1348975260,
    1351540320,
    1354114080,
    1356690120,
    1359261600,
    1361824080,
    1364376540,
    1366919940,
    1369456020,
    1371987240,
    1374517080,
    1377049620,
    1379589300,
    1382139600,
    1384701480,
    1387272600,
    1389848040,
    1392422100,
    1394989800,
    1397547840,
    1400095020,
    1402632780,
    1405164360,
    1407694260,
    1410226800,
    1412765520,
    1415312640,
    1417868940,
    1420433700,
    1423005060,
    1425578820,
    1428149220,
    1430710980,
    1433262000,
    1435803660,
    1438339440,
    1440873420,
    1443408720,
    1445947560,
    1448491500,
    1451041980,
    1453600080,
    1456165320,
    1458734520,
    1461302700,
    1463865360,
    1466420640,
    1468969140,
    1471512540,
    1474052820,
    1476591900,
    1479131580,
    1481674020,
    1484220960,
    1486773240,
    1489330500,
    1491890940,
    1494452640,
    1497013860,
    1499573340,
    1502129580,
    1504681440,
    1507228860,
    1509773040,
    1512316140,
    1514859960,
    1517405280,
    1519951920,
    1522499880,
    1525050000,
    1527603660,
    1530161700,
    1532722920,
    1535284680,
    1537844040,
    1540399560,
    1542951660,
    1545501000,
    1548047820,
    1550591640,
    1553132640,
    1555672440,
    1558213980,
    1560760320,
    1563313200,
    1565872260,
    1568435640,
    1571000940,
    1573565760,
    1576127640,
    1578684180,
    1581233700,
    1583776140,
    1586313420,
    1588848420,
    1591384500,
    1593924360,
    1596470400,
    1599024180,
    1601586360,
    1604155860,
    1606728660,
    1609298940,
    1611861420,
    1614413940,
    1616957400,
    1619494440,
    1622027760,
    1624560120,
    1627094340,
    1629633780,
    1632182160,
    1634741880,
    1637312340,
    1639888620,
    1642463400,
    1645030680,
    1647587940,
    1650135420,
    1652674560,
    1655207580,
    1657737540,
    1660268160,
    1662803940,
    1665348960,
    1667905440,
    1670472600,
    1673046600,
    1675621800,
    1678192920,
    1680755760,
    1683308160,
    1685850180,
    1688384340,
    1690914720,
    1693445760,
    1695981480,
    1698524700,
    1701076680,
    1703637300,
    1706205360,
    1708777920,
    1711350120,
    1713916260,
    1716472500,
    1719018540,
    1721557080,
    1724091960,
    1726626900,
    1729164480,
    1731706200,
    1734253380,
    1736807340,
    1739368500,
    1741935360,
    1744503840,
    1747069080,
    1749627960,
    1752179880,
    1754726160,
    1757268540,
    1759808880,
    1762348860,
    1764890160,
    1767434640,
    1769983860,
    1772538000,
    1775096040,
    1777656300,
    1780217220,
    1782777480,
    1785335820,
    1787890800,
    1790441400,
    1792987980,
    1795532100,
    1798075800,
    1800620340,
    1803165960,
    1805712420,
    1808260200,
    1810810860,
    1813365960,
    1815925620,
    1818487860,
    1821049560,
    1823608140,
    1826162880,
    1828714260,
    1831262700,
    1833807960,
    1836349740,
    1838889000,
    1841428260,
    1843971060,
    1846519980,
    1849075920,
    1851637800,
    1854203220,
    1856769540,
    1859334120,
    1861894200,
    1864447500,
    1866993180,
    1869532140,
    1872067140,
    1874601600,
    1877138700,
    1879681080,
    1882230780,
    1884789060,
    1887355800,
    1889928240,
    1892501220,
    1895068500,
    1897626120,
    1900173540,
    1902712920,
    1905247260,
    1907779380,
    1910312040,
    1912848360,
    1915392000,
    1917946140,
    1920511980,
    1923086520,
    1925663220,
    1928234880,
    1930797060,
    1933348980,
    1935891660,
    1938427200,
    1940958180,
    1943488020,
    1946020920,
    1948561200,
    1951112100,
    1953674460,
    1956245700,
    1958820840,
    1961394300,
    1963961280,
    1966518660,
    1969065480,
    1971603240,
    1974135180,
    1976665740,
    1979199120,
    1981738800,
    1984286640,
    1986843060,
    1989407340,
    1991977560,
    1994549940,
    1997119140,
    1999680240,
    2002231260,
    2004773400,
    2007310140,
    2009845320,
    2012382000,
    2014922040,
    2017466640,
    2020016940,
    2022574020,
    2025137520,
    2027704800,
    2030271420,
    2032833300,
    2035388760,
    2037938160,
    2040483060,
    2043025080,
    2045565840,
    2048106780,
    2050649760,
    2053196280,
    2055747300,
    2058302640,
    2060860920,
    2063420820,
    2065981140,
    2068540740,
    2071098120,
    2073651900,
    2076201420,
    2078747400,
    2081291700,
    2083835880,
    2086380600,
    2088925860,
    2091471840,
    2094019860,
    2096571780,
    2099128860,
    2101690260,
    2104253220,
    2106814560,
    2109372300,
    2111926200,
    2114476680,
    2117023560,
    2119566600,
    2122106100,
    2124644160,
    2127184020,
    2129728920,
    2132281020,
    2134840260,
    2137404780,
    2139971880,
    2142538620,
    2145102000,
    2147659320,
    2150208660,
    2152750260,
    2155286280,
    2157819960,
    2160354780,
    2162893800,
    2165439480,
    2167993500,
    2170556580,
    2173127340,
    2175701520,
    2178272820,
    2180835660,
    2183387820,
    2185930500,
    2188466520,
    2190999000,
    2193530700,
    2196064680,
    2198604240,
    2201153040,
    2203713480,
    2206284720,
    2208861540,
    2211436560,
    2214003660,
    2216560380,
    2219107200,
    2221645740,
    2224178460,
    2226708420,
    2229239460,
    2231775840,
    2234321460,
    2236878480,
    2239445880,
    2242019580,
    2244594120,
    2247164460,
    2249726580,
    2252278440,
    2254820400,
    2257354920,
    2259885900,
    2262417840,
    2264954580,
    2267498700,
    2270051040,
    2272611300,
    2275178340,
    2277749460,
    2280320280,
    2282885460,
    2285441400,
    2287987860,
    2290527240,
    2293063320,
    2295599640,
    2298138540,
    2300681220,
    2303228640,
    2305781880,
    2308341540,
    2310906420,
    2313473040,
    2316037140,
    2318595720,
    2321148360,
    2323695900,
    2326240080,
    2328782220,
    2331323640,
    2333865840,
    2336410380,
    2338958580,
    2341510980,
    2344066860,
    2346625080,
    2349184680,
    2351744640,
    2354303760,
    2356860360,
    2359413120,
    2361961740,
    2364507360,
    2367051720,
    2369596020,
    2372140500,
    2374685160,
    2377230900,
    2379779700,
    2382333480,
    2384892780,
    2387455800,
    2390019240,
    2392579980,
    2395136700,
    2397689460,
    2400238380,
    2402783220,
    2405323800,
    2407861440,
    2410399080,
    2412940320,
    2415488220,
    2418043920,
    2420606520,
    2423173440,
    2425741560,
    2428307820,
    2430868980,
    2433422520,
    2435967600,
    2438505480,
    2441039220,
    2443572420,
    2446108560,
    2448650400,
    2451200160,
    2453759040,
    2456326800,
    2458900620,
    2461474680,
    2464042560,
    2466600000,
    2469146820,
    2471685300,
    2474218740,
    2476750200,
    2479282560,
    2481818940,
    2484362940,
    2486917680,
    2489484120,
    2492059260,
    2494636200,
    2497207740,
    2499769500,
    2502320820,
    2504862960,
    2507398080,
    2509929060,
    2512459260,
    2514992760,
    2517533700,
    2520085200,
    2522647800,
    2525218860,
    2527793340,
    2530365900,
    2532932040,
    2535488880,
    2538035580,
    2540573520,
    2543106120,
    2545637520,
    2548171980,
    2550712620,
    2553261060,
    2555817420,
    2558380920,
    2560949700,
    2563520520,
    2566088460,
    2568648960,
    2571200160,
    2573743080,
    2576281020,
    2578817580,
    2581355700,
    2583896880,
    2586442020,
    2588991960,
    2591547780,
    2594109420,
    2596674660,
    2599239660,
    2601800940,
    2604356700,
    2606907300,
    2609453820,
    2611997820,
    2614540260,
    2617082340,
    2619625680,
    2622171540,
    2624721060,
    2627274240,
    2629830420,
    2632388640,
    2634948180,
    2637508140,
    2640066900,
    2642622720,
    2645174400,
    2647722180,
    2650267500,
    2652811800,
    2655355680,
    2657899380,
    2660443440,
    2662989480,
    2665539840,
    2668096140,
    2670657840,
    2673222180,
    2675785560,
    2678345400,
    2680900980,
    2683452240,
    2685999000,
    2688541080,
    2691079200,
    2693615640,
    2696153880,
    2698697640,
    2701249140,
    2703808680,
    2706374400,
    2708943180,
    2711511720,
    2714076420,
    2716634220,
    2719183320,
    2721724020,
    2724258780,
    2726791260,
    2729325000,
    2731863420,
    2734408920,
    2736963360,
    2739527280,
    2742099240,
    2744674500,
    2747246520,
    2749809480,
    2752361220,
    2754903060,
    2757438300,
    2759970060,
    2762501400,
    2765035380,
    2767575240,
    2770124580,
    2772685560,
    2775257340,
    2777834400,
    2780409360,
    2782976100,
    2785532280,
    2788078500,
    2790616620,
    2793149280,
    2795679540,
    2798211120,
    2800748220,
    2803294560,
    2805851940,
    2808419280,
    2810992380,
    2813566080,
    2816135400,
    2818696740,
    2821248360,
    2823790440,
    2826325500,
    2828857320,
    2831390340,
    2833928160,
    2836473060,
    2839025640,
    2841585360,
    2844151080,
    2846720580,
    2849289840,
    2851854120,
    2854409940,
    2856957000,
    2859497520,
    2862035040,
    2864572920,
    2867113140,
    2869656600,
    2872203960,
    2874756300,
    2877314220,
    2879876940,
    2882441700,
    2885004720,
    2887563300,
    2890116780,
    2892665940,
    2895212040,
    2897756040,
    2900298900,
    2902841700,
    2905385940,
    2907933000,
    2910483480,
    2913037200,
    2915593500,
    2918151960,
    2920711740,
    2923271880,
    2925830340,
    2928385200,
    2930935800,
    2933482800,
    2936027640,
    2938571460,
    2941114680,
    2943657480,
    2946201240,
    2948748300,
    2951301000,
    2953860120,
    2956424160,
    2958989400,
    2961552240,
    2964110880,
    2966664840,
    2969213940,
    2971758120,
    2974297440,
    2976833520,
    2979369540,
    2981909520,
    2984456580,
    2987012280,
    2989575660,
    2992144080,
    2994714000,
    2997281760,
    2999843700,
    3002397240,
    3004941540,
    3007478340,
    3010010880,
    3012543060,
    3015078480,
    3017620080,
    3020170020,
    3022729620,
    3025298400,
    3027873240,
    3030448140,
    3033016260,
    3035573460,
    3038119560,
    3040657260,
    3043189980,
    3045721020,
    3048253260,
    3050789940,
    3053334420,
    3055889700,
    3058456740,
    3061032180,
    3063609060,
    3066180240,
    3068741460,
    3071292120,
    3073833840,
    3076368840,
    3078900000,
    3081430740,
    3083964960,
    3086506680,
    3089058780,
    3091621440,
    3094192020,
    3096765600,
    3099337080,
    3101902260,
    3104458560,
    3107005260,
    3109543740,
    3112077180,
    3114609660,
    3117145320,
    3119686980,
    3122235840,
    3124791960,
    3127354320,
    3129921480,
    3132490500,
    3135057180,
    3137617260,
    3140168880,
    3142712820,
    3145252140,
    3147790320,
    3150329880,
    3152872080,
    3155417520,
    3157966920,
    3160521240,
    3163080780,
    3165643980,
    3168207540,
    3170768340,
    3173324700,
    3175876560,
    3178425000,
    3180970860,
    3183514980,
    3186058080,
    3188601480,
    3191146560,
    3193694400,
    3196245480,
    3198799560,
    3201356280,
    3203915280,
    3206475720,
    3209036040,
    3211593960,
    3214147740,
    3216697200,
    3219243360,
    3221787480,
    3224330340,
    3226872420,
    3229414560,
    3231958860,
    3234507840,
    3237063540,
    3239625720,
    3242191560,
    3244756980,
    3247318860,
    3249875880,
    3252427680,
    3254974140,
    3257515140,
    3260051880,
    3262586760,
    3265123680,
    3267666480,
    3270217680,
    3272777640,
    3275344560,
    3277915020,
    3280485060,
    3283050780,
    3285608820,
    3288157440,
    3290697180,
    3293230860,
    3295762260,
    3298295280,
    3300833280,
    3303378900,
    3305933820,
    3308498580,
    3311071500,
    3313647660,
    3316220040,
    3318782880,
    3321334020,
    3323875200,
    3326409660,
    3328940940,
    3331472220,
    3334006380,
    3336546780,
    3339096660,
    3341658180,
    3344230200,
    3346807320,
    3349381860,
    3351947940,
    3354503520,
    3357049260,
    3359587200,
    3362120040,
    3364650840,
    3367183200,
    3369721140,
    3372268200,
    3374825880,
    3377392800,
    3379965000,
    3382537500,
    3385105680,
    3387666360,
    3390217740,
    3392760240,
    3395296080,
    3397829040,
    3400363320,
    3402902280,
    3405447900,
    3408000420,
    3410559360,
    3413123520,
    3415691160,
    3418258860,
    3420822300,
    3423378240,
    3425926140,
    3428467980,
    3431007120,
    3433546620,
    3436088100,
    3438632220,
    3441179340,
    3443730480,
    3446286480,
    3448847100,
    3451410060,
    3453972060,
    3456530760,
    3459085320,
    3461636280,
    3464184360,
    3466730220,
    3469274340,
    3471817620,
    3474361440,
    3476907120,
    3479455620,
    3482007180,
    3484561680,
    3487119060,
    3489678960,
    3492240240,
    3494800620,
    3497357700,
    3499910220,
    3502458420,
    3505003440,
    3507546600,
    3510088380,
    3512629440,
    3515171340,
    3517716900,
    3520268700,
    3522827880,
    3525392940,
    3527959980,
    3530524920,
    3533085240,
    3535640040,
    3538189200,
    3540732540,
    3543270600,
    3545805180,
    3548339880,
    3550878780,
    3553425300,
    3555981120,
    3558545400,
    3561115260,
    3563686740,
    3566255700,
    3568818180,
    3571371480,
    3573915060,
    3576450780,
    3578982300,
    3581513640,
    3584048580,
    3586590120,
    3589140480,
    3591700740,
    3594270360,
    3596846040,
    3599421420,
    3601989540,
    3604546320,
    3607091760,
    3609628800,
    3612160980,
    3614691840,
    3617224320,
    3619761480,
    3622306500,
    3624862380,
    3627429720,
    3630005100,
    3632581620,
    3635152140,
    3637712640,
    3640262820,
    3642804300,
    3645339420,
    3647871120,
    3650402580,
    3652937760,
    3655480260,
    3658032780,
    3660595320,
    3663165060,
    3665737440,
    3668307660,
    3670871880,
    3673427820,
    3675974760,
    3678513960,
    3681048420,
    3683582220,
    3686119140,
    3688661700,
    3691210920,
    3693766440,
    3696327480,
    3698892720,
    3701460000,
    3704025480,
    3706585260,
    3709137420,
    3711682560,
    3714223500,
    3716763420,
    3719304480,
    3721847640,
    3724393200,
    3726941760,
    3729494400,
    3732051780,
    3734612880,
    3737175060,
    3739735500,
    3742292580,
    3744846060,
    3747396480,
    3749944380,
    3752490060,
    3755034000,
    3757577280,
    3760121280,
    3762667380,
    3765216300,
    3767768400,
    3770323800,
    3772882380,
    3775443540,
    3778005480,
    3780565560,
    3783121500,
    3785672400,
    3788219160,
    3790762920,
    3793304640,
    3795845100,
    3798385440,
    3800928060,
    3803475960,
    3806031240,
    3808594020,
    3811161360,
    3813728820,
    3816292560,
    3818850780,
    3821402940,
    3823948860,
    3826488840,
    3829024140,
    3831557640,
    3834093420,
    3836635500,
    3839186520,
    3841747140,
    3844315200,
    3846887160,
    3849458520,
    3852025020,
    3854583120,
    3857131080,
    3859669920,
    3862202580,
    3864733140,
    3867265620,
    3869803500,
    3872349360,
    3874904880,
    3877470420,
    3880044120,
    3882620760,
    3885193260,
    3887755740,
    3890306340,
    3892846800,
    3895380780,
    3897911820,
    3900443220,
    3902977800,
    3905518800,
    3908069280,
    3910631220,
    3913203240,
    3915779940,
    3918353820,
    3920919240,
    3923474220,
    3926019660,
    3928557660,
    3931090920,
    3933622440,
    3936155700,
    3938694600,
    3941242260,
    3943799940,
    3946366260,
    3948937320,
    3951508380,
    3954075420,
    3956635440,
    3959186880,
    3961729980,
    3964266900,
    3966801120,
    3969336720,
    3971876880,
    3974423040,
    3976975380,
    3979533180,
    3982095600,
    3984661260,
    3987227400,
    3989790120,
    3992346300,
    3994895280,
    3997438680,
    3999979560,
    4002520740,
    4005063420,
    4007607960,
    4010154600,
    4012704300,
    4015258320,
    4017816720,
    4020377940,
    4022939220,
    4025498220,
    4028054100,
    4030606920,
    4033157100,
    4035704760,
    4038250020,
    4040793540,
    4043336640,
    4045880820,
    4048427280,
    4050976800,
    4053529680,
    4056086220,
    4058646360,
    4061208960,
    4063771380,
    4066330620,
    4068884940,
    4071434040,
    4073979120,
    4076521380,
    4079061660,
    4081600980,
    4084141260,
    4086685440,
    4089236520,
    4091795880,
    4094362140,
    4096931040,
    4099497900,
    4102059660,
]


def get_last_full_moon(d):
    """Return the last full moon for d.

    Raise ValueError if the d value is not between 2000 - 2099.
    """
    now = d.int_timestamp
    idx = bisect.bisect_right(fullmoons, now)
    if idx in [0, len(fullmoons)]:
        raise ValueError(
            "watson has only full moon dates from year 2000 to 2099, not {}".format(
                d.year
            )
        )

    last = fullmoons[idx - 1]
    return arrow.get(last)
