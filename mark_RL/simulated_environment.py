import numpy
from point import Point
lidar_points = numpy.empty([2,37], dtype = object)

'''
OBS
'''
point0 = Point(-198.0,2.4248006623117594e-14,198,-90)
point1 = Point(-197.2465502221656,17.256837064036322,198,-85)
point2 = Point(-196.9615506024416,34.72963553338605,200,-80)
'''
WALL
'''
point3 = Point(-585.3510507311753,156.84434133212773,606,-75)
point4 = Point(-383.3945892806506,139.5442184768729,408,-70)
point5 = Point(-392.43127178686944,182.99370733372288,433,-65)
point6 = Point(-611.4139350718137,352.99999999999994,706,-60)
point7 = Point(-610.268272995299,427.31444508152924,745,-55)
point8 = Point(-510.95164356035826,428.7393356609218,667,-50)
point9 = Point(-422.1427483683688,422.1427483683689,597,-45)
point10 = Point(-379.2446897150582,451.96622144019705,590,-40)
point11 = Point(-314.3198871203733,448.89532027036745,548,-35)
point12 = Point(-261.4999999999999,452.93128617926146,523,-30)
'''
OBS
'''
point13 = Point(-225.67815176953343,483.9683582775711,534,-25)
point14 = Point(-16.07494673630643,44.1655531769377,47,-20)
point15 = Point(-11.646857029613438,43.466662183008076,45,-15)
point16 = Point(-7.466871639678003,42.34673337952494,43,-10)
point17 = Point(-3.747696938149304,42.83637201794506,43,-5)
point18 = Point(2.87791997799628e-15,47.0,47,0)
point19 = Point(3.660541195401642,41.84017731985331,42,5)
point20 = Point(7.293223462011078,41.361925626512736,42,10)
point21 = Point(10.870399894305871,40.56888470414087,42,15)
point22 = Point(14.36484601967809,39.46709007300815,42,20)
point23 = Point(150.02948291794831,321.73926439801073,355,25)
point24 = Point(147.50000000000003,255.4774941164094,295,30)
'''
WALL
'''
point25 = Point(318.33492217483064,454.6293845803904,555,35)
point26 = Point(372.81681361819284,444.3057770090073,580,40)
point27 = Point(378.30212793480297,378.3021279348029,535,45)
point28 = Point(378.42595490077514,317.5370791851504,494,50)
point29 = Point(381.7248526386702,267.28661933958745,466,55)
point30 = Point(381.05117766515303,219.99999999999997,440,60)
point31 = Point(384.27450170353956,179.19014297805657,424,65)
point32 = Point(386.21366714300837,140.57027890684984,411,70)
point33 = Point(386.3703305156273,103.5276180410083,400,75)
'''
WALL
'''
point34 = Point(388.01425468681,68.41738200077054,394,80)
point35 = Point(389.5121269538725,34.07789541433434,391,85)
point36 = Point(391.0,0.0,391,90)


point37 = Point(391.0,0.0,391,90)
point38 = Point(389.5121269538725,34.07789541433434,391,85)
point39 = Point(387.0294469337978,68.24373382310363,393,80)
point40 = Point(384.43847886304917,103.00997995080326,398,75)
point41 = Point(382.45489665986474,139.20219833354716,407,70)
point42 = Point(378.83665498131967,176.65443340761237,418,65)
point43 = Point(376.7210506462308,217.49999999999997,435,60)
point44 = Point(369.4375719743353,258.68297279432176,451,55)
point45 = Point(368.46737714022845,309.18084025922536,481,50)
point46 = Point(364.86709909225857,364.8670990922585,516,45)
point47 = Point(366.3889375213274,436.64533257781744,570,40)
point48 = Point(333.8214859563089,476.74648977619324,582,35)
point49 = Point(146.00000000000003,252.87941790505607,292,30)
point50 = Point(127.63071504569123,273.7049516850683,302,25)
point51 = Point(15.390906449655096,42.286167935365874,45,20)
point52 = Point(11.129218939408393,41.53481053042994,43,15)
point53 = Point(6.7722789290102865,38.40750236747611,39,10)
point54 = Point(3.4862297099063255,39.84778792366982,40,5)
point55 = Point(2.5717582782094417e-15,42.0,42,0)
point56 = Point(-3.311918224411013,37.85539852748633,38,-5)
point57 = Point(-6.945927106677212,39.39231012048832,40,-10)
point58 = Point(-10.870399894305876,40.56888470414087,42,-15)
point59 = Point(-13.680805733026748,37.58770483143634,40,-20)
point60 = Point(-231.59480743390324,496.6566672960842,548,-25)
point61 = Point(-262.4999999999999,454.6633369868303,525,-30)
point62 = Point(-309.1576991932139,441.5229518717665,539,-35)
point63 = Point(-395.3143799572217,471.11733251817145,615,-40)
point64 = Point(-410.8290398693841,410.82903986938413,581,-45)
point65 = Point(-619.7299544832531,520.0151762364104,809,-50)
point66 = Point(-633.2045302353907,443.3745852993585,773,-55)
point67 = Point(-626.1363669361492,361.49999999999994,723,-60)
point68 = Point(-406.93219637945583,189.75559952157408,449,-65)
point69 = Point(-443.53491701094873,161.43350764971572,472,-70)
point70 = Point(-614.3288255198473,164.60891268520336,636,-75)
point71 = Point(-192.03751183738058,33.861394645051405,195,-80)
point72 = Point(-193.26177142979864,16.90821409304569,194,-85)
point73 = Point(-195.0,2.388061258337339e-14,195,-90)

lidar_points[0][0] = point0
lidar_points[0][1] = point1
lidar_points[0][2] = point2
lidar_points[0][3] = point3
lidar_points[0][4] = point4
lidar_points[0][5] = point5
lidar_points[0][6] = point6
lidar_points[0][7] = point7
lidar_points[0][8] = point8
lidar_points[0][9] = point9
lidar_points[0][10] = point10
lidar_points[0][11] = point11
lidar_points[0][12] = point12
lidar_points[0][13] = point13
lidar_points[0][14] = point14
lidar_points[0][15] = point15
lidar_points[0][16] = point16
lidar_points[0][17] = point17
lidar_points[0][18] = point18
lidar_points[0][19] = point19
lidar_points[0][20] = point20
lidar_points[0][21] = point21
lidar_points[0][22] = point22
lidar_points[0][23] = point23
lidar_points[0][24] = point24
lidar_points[0][25] = point25
lidar_points[0][26] = point26
lidar_points[0][27] = point27
lidar_points[0][28] = point28
lidar_points[0][29] = point29
lidar_points[0][30] = point30
lidar_points[0][31] = point31
lidar_points[0][32] = point32
lidar_points[0][33] = point33
lidar_points[0][34] = point34
lidar_points[0][35] = point35
lidar_points[0][36] = point36

lidar_points[1][0] =  point73
lidar_points[1][1] =  point72
lidar_points[1][2] =  point71
lidar_points[1][3] =  point70
lidar_points[1][4] =  point69
lidar_points[1][5] =  point68
lidar_points[1][6] =  point67
lidar_points[1][7] =  point66
lidar_points[1][8] =  point65
lidar_points[1][9] =  point64
lidar_points[1][10] =  point63
lidar_points[1][11] =  point62
lidar_points[1][12] =  point61
lidar_points[1][13] =  point60
lidar_points[1][14] =  point59
lidar_points[1][15] =  point58
lidar_points[1][16] =  point57
lidar_points[1][17] =  point56
lidar_points[1][18] =  point55
lidar_points[1][19] =  point54
lidar_points[1][20] =  point53
lidar_points[1][21] =  point52
lidar_points[1][22] =  point51
lidar_points[1][23] =  point50
lidar_points[1][24] =  point49
lidar_points[1][25] =  point48
lidar_points[1][26] =  point47
lidar_points[1][27] =  point46
lidar_points[1][28] =  point45
lidar_points[1][29] =  point44
lidar_points[1][30] =  point43
lidar_points[1][31] =  point42
lidar_points[1][32] =  point41
lidar_points[1][33] =  point40
lidar_points[1][34] =  point39
lidar_points[1][35] =  point38
lidar_points[1][36] =  point37