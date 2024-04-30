import pandas as pd
import typing
import math
from math import log as ln
from math import exp
from math import log10

def stem_vol_6(dbh_m, height_m)  :
    from math import log, pi
    a=0.560673
    b=0.15468
    c=-0.65583
    d=0.033210
    D=dbh_m*10
    H=height_m*10
    return ((pi/4)*(a*D**2*H+b*D**2*H*(log(D*D))+c*D**2+d*D*H))/1000

def stem_vol_18(dbh_m, height_m)  :
    a=0.05437
    b=1.94505
    c=0.92947
    D=dbh_m*100
    H=height_m
    return (a*D**b*H**c)/1000

def stem_vol_30(dbh_m, height_m)  :
    """
    not sure about units; constant in paper was different from source
    original paper gives the volume units as 1/10dm3;
    this is the reason division of 10000 in return line

    """
    a=-18.6827
    b=2.1461
    c=0.1283
    d=0.1380
    e=0.6311
    D=dbh_m*100
    H=height_m
    return (a+b*(D**2)+c*(D**2)*H+d*D*(H**2)+e*(H**2))/10000

def stem_vol_42(dbh_m, height_m) :
    a=0.00021491
    b=2.258957614
    c=-0.00956695
    d=0.60291075
    D=dbh_m*1000
    H=height_m
    return a*D**(b+c)*H**d/1000

def stem_vol_54(dbh_m, height_m) :
    a=-0.039836
    b=0.006262765
    c=-0.00015937
    d=-1.9902*10**-7
    e=-0.0009834
    f=3.7872*10**-5
    D=dbh_m*100
    H=height_m
    return a+b*D+c*D**2+d*D**3+e*H+f*D**2*H

def stem_vol_66(dbh_m, height_m) :
    a=-0.03088
    b=0.004676261
    c=-4.8614*10**-5
    d=-3.8178*10**-6
    e=-0.0011638
    f=4.0597*10**-5
    D=dbh_m*100
    H=height_m
    return a+b*D+c*D**2+d*D**3+e*H+f*D**2*H

def stem_vol_78(dbh_m, height_m) :
    a=0.00035217
    b=2.12841828
    c=0.003292718
    d=0.76283925
    D=dbh_m*1000
    H=height_m
    return (a*D**(b+c)*H**d)/1000

def stem_vol_90(dbh_m, height_m) :
    from math import log
    from math import exp
    a=-3.7544
    b=1.8960
    c=2.8979
    d=-1.6020
    e=-0.007827
    D=dbh_m*100
    H=height_m
    vol_ln_dm3=a+b*log(D)+c*log(H)+d*log(H-1.3)+e*D
    vol_dm3=exp(vol_ln_dm3)
    vol_m3 = vol_dm3/1000
    return vol_m3

def stem_vol_102(dbh_m, height_m) :
    a=0.6844
    b=3.0296
    c=2.0560
    d=-1.7377
    e=-0.9756
    D=dbh_m*100
    H=height_m
    return (a*H**b*D**c*(H-1.3)**d*(D+40)**e)/1000

def stem_vol_114(dbh_m, height_m) :
    from math import pi
    a=0.666151
    b=0.458507
    D=dbh_m*100
    H=height_m
    return (pi/40000)*H*D*(a+b*D)

def stem_vol_126(dbh_m, height_m) :
    a=0.1614
    b=3.7060
    c=1.9747
    d=-2.2905
    e=-0.6665
    D=dbh_m*100
    H=height_m
    return (a*H**b*D**c*(H-1.3)**d*(D+40)**e)/1000

def stem_vol_138(dbh_m, height_m) :
    from math import log10
    a=0.00010892
    b=1.9701
    c=0.0102
    d=0.0102
    e=0.1330
    D=dbh_m*100
    H=height_m
    return a*10**(b*(log10(D))+c*(log10(D*D))+d*(log10(H))+e*(log10(H*H)))

def stem_vol_150(dbh_m, height_m) :
    from math import log
    from math import exp
    a=-3.2890
    b=1.9995
    c=2.1395
    d=-1.1411
    e=-0.002847
    D=dbh_m*100
    H=height_m
    vol_ln_dm3=a+b*log(D)+c*log(H)+d*log(H-1.3)+e*D
    vol_dm3=exp(vol_ln_dm3)
    vol_m3 = vol_dm3/1000
    return vol_m3

def stem_vol_162(dbh_m, height_m) :
    a=0.1263
    b=2.4621
    c=1.9008
    d=-1.3716
    e=-0.2663
    D=dbh_m*100
    H=height_m
    return (a*H**b*D**c*(H-1.3)**d*(D+100)**e)/1000

def stem_vol_174(dbh_m, height_m) :
    a= -1.25246
    b=1.98244
    c= -0.13118
    d=1.03781
    e=-0.03482
    D=dbh_m*100
    H=height_m
    return (10**a*D**b*(D+20)**c*H**d*(H-1.3)**e)/1000

def stem_vol_186(dbh_m, height_m) :
    a= -0.21
    b=0.0398
    D=dbh_m*100
    H=height_m
    return (a+b*D**2*H)/1000

def stem_vol_198(dbh_m, height_m) :
    a=0.00095916
    b=2.092560524
    c=-0.0449007
    d=0.48824344
    D=dbh_m*1000
    H=height_m
    return (a*D**(b+c)*H**d)/1000

def stem_vol_210(dbh_m, height_m) :
    from math import pi
    a=0.115631
    b=65.9961
    c=1.20321
    d=-0.930406
    e=-215.758
    f=168.477
    D=dbh_m*10
    H=height_m*10
    return ((pi/4)*(a*D**2*H+b*D**2+c*D*H+d*H+d*H+e*D+f))/1000

def stem_vol_222(dbh_m, height_m) :
    a=-1.86827
    b=0.21461
    c=0.01283
    d=0.0138
    e=-0.06311
    D=dbh_m*100
    H=height_m
    return (a+b*D**2+c*D**2*H+d*H**2+D+e*H**2)/1000
    
#Jakub_Sobolewski
def stem_volume7(dbh_cm, height_m):
    from math import log10
    a=0.0000452
    b=2.1554
    c=-0.1067
    d=0.9380
    e=0.0228
    D=dbh_cm * 100
    H=height_m
    result = a*10**(b*log10(D)+c*log10(D)**2+d*log10(H)+e*log10(H)**2)
    return result
    
def stem_volume19(dbh_cm, height_m):
    from math import pi
    a=0.2264
    b=0.01347
    c=0.007665
    d=-0.06669
    e=0.000428
    D=dbh_cm * 100
    H=height_m
    return (a*D**2+b*D**2*H+c*D*H**2+d*D*H+e*D**2*H**2)/1000
    
def stem_volume31(dbh_cm, height_m):
    from math import pi
    a=0.99983
    b=0.006325
    c=0.02849
    d=0.00885
    e=-0.00799
    D=dbh_cm * 100
    H=height_m
    return (a+b*D**2+c*D**2*H+d*D*H**2+e*H**2)/1000
    
def stem_volume43(dbh_cm, height_m):
    from math import pi, log10, exp
    a=1.85298
    b=0.86717
    c=-2.33706
    D=dbh_cm * 100
    H=height_m
    return (D**a*H**b*exp(c))/1000
    
def stem_volume55(dbh_cm, height_m):
    from math import pi, log10, exp
    a=1.9577
    b=0.7706
    c=-2.48079
    D=dbh_cm * 100
    H=height_m
    return (D**a*H**b*exp(c))/1000
    
def stem_volume67(dbh_cm, height_m):
    from math import pi, log10, exp
    a=1.86670
    b=1.08118
    c=-3.0488
    D=dbh_cm * 100
    H=height_m
    return (D**a*H**b*exp(c))/1000
    
def stem_volume79(dbh_mm, height_m):
    from math import pi, log10, exp
    a=0.00035217
    b=2.12841828
    c=-0.1054168
    d=0.76283925
    D=dbh_mm * 1000
    H=height_m
    return (a*D**(b+c)*H**d)/1000
    
def stem_volume91(dbh_cm, height_m):
    from math import pi, log10, exp
    a=0.7877
    b=1.9302
    c=0.79465
    D=dbh_cm * 100
    H=height_m
    return (a*D**b*H**c)/10000
    
def stem_volume103(dbh_cm, height_m):
    from math import pi, log10
    a=0.7464
    b=2.496
    c=2.0714
    d=-1.4175
    e=-0.9601
    D=dbh_cm * 100
    H=height_m
    return (a*H**b*D**c*(H-1.3)**d*(D+40)**e)/1000
    
def stem_volume115(dbh_cm, height_m):
    from math import pi, log10
    a=0.53005
    b=1.229283
    D=dbh_cm * 100
    H=height_m
    return (pi/40000)*H*D*(a*D+b)
    
def stem_volume127(dbh_cm, height_m):
    from math import pi, log10
    a=0.1870
    b=3.7077
    c=1.9854
    d=-2.2816
    e=-0.7161
    D=dbh_cm * 100
    H=height_m
    return (a*H**b*D**c*(H-1.3)**d*(D+40)**e)/1000
    
def stem_volume139(dbh_cm, height_m):
    from math import pi, log10
    a=0.000074
    b=3.1
    D=dbh_cm * 100
    H=height_m
    return a*H**b
    
def stem_volume151(dbh_cm, height_m):
    from math import pi, log10
    a=0.0942
    b=1.9671
    c=0.7005
    D=dbh_cm * 100
    H=height_m
    return (a*D**b*H**c)/1000
    
def stem_volume163(dbh_cm, height_m):
    from math import pi, log10
    a=0.4434
    b=4.9667
    c=1.9912
    d=-3.6612
    e=-0.7502
    D=dbh_cm * 100
    H=height_m
    return (a*H**b*D**c*(H-1.3)**d*(D+100)**e)/1000
    
def stem_volume175(dbh_cm, height_m):
    from math import pi, log10
    a=-1.52761
    b=1.82928
    c=0.07454
    d=1.43792
    e=-0.35559
    D=dbh_cm * 100
    H=height_m
    return (10**a*D**b*(D+20)**c*H**d*(H-1.3)**e)/1000
    
def stem_volume187(dbh_cm, height_m):
    from math import pi, log10
    a=0.00007604
    b=1.7812
    c=0.0528
    d=0.8533
    e=0.0654
    D=dbh_cm * 100
    H=height_m
    return a*10**(b*log10(D)+c*log10(D)**2+d*log10(H)+e*log10(H)**2)
    
def stem_volume199(dbh_mm, height_m):
    from math import pi, log10
    a=0.00095916
    b=2.092560524
    c=0
    d=0.48824344
    D=dbh_mm * 1000
    H=height_m
    return (a*D**(b+c)*H**d)/1000
    
def stem_volume211(dbh_dm, height_dm):
    from math import pi, log
    a=0.417118
    b=0.21941
    c=13.32594
    D=dbh_dm * 10
    H=height_dm * 10
    return ((pi/4)*(a*D**2*H+b*D**2*H*log(D)**2+c*D**2))/1000
    
def stem_volume223(dbh_cm, height_m):
    from math import pi, exp
    a=1.67887
    b=1.11243
    c=-2.64821
    D=dbh_cm * 100
    H=height_m
    return (D**a*H**b*exp(c))/1000

# Jeremias
def stem_vol_4(dbh_m):
    D = dbh_m * 100
    
    a = 2.4613
    b = -0.4023

    V = a * math.log(D) + b

    return V

def stem_vol_16(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m

    a = 0.6716
    b = 0.75708
    c = 0.029679
    d = 0.004341

    V =  a + b * D**2 + c * D**2 * H + d * H * D
    
    return V / 1000

def stem_vol_28(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m

    a = 0.011197
    b = 2.10253
    c = 0.986
    d = 3.98519
    e =-2.65900

    V =  a * (D ** b) * (c ** D) * (H ** d) * (H - 1.3) ** e

    return V / 1000

def stem_vol_40(dbh_m, height_m):
    D = dbh_m * 1000
    H = height_m

    a = 0.00021491
    b = 2.258957614
    c = 0.001411006
    d = 0.60291075

    V =  a * D ** (b + c) * H ** d
    
    return V / 1000

def stem_vol_52(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m

    a = 1.55448
    b = 1.55880
    c = -3.57875

    V =  D ** a * H ** b * math.exp(c)
    
    return V / 1000

def stem_vol_64(dbh_m, height_m):
    D = dbh_m * 10
    H = height_m * 10

    a = 0.609443
    b = -0.0455748
    c = -18.6631
    d = -0.248736
    e = 0.126594
    f = 36.9783
    g = -14.204

    V =  result = (math.pi / 4) * (a * D**2 * H + b * D**2 * H * math.log(D)**2 + c * D**2 + d * D * H + e * H + f * D + g)
    
    return V / 1000

def stem_vol_76(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m

    a = 0.5
    b = 0.0753
    c = 0.03345
    d = -0.00243

    V =  a + b * D**2 + c * D**2 * H + d * H**2 * D
    
    return V / 1000

def stem_vol_88(dbh_m):
    D = dbh_m * 100

    a = -5.39934
    b = 3.46468
    c = 2
    d = 1.25
    e = -0.0273199

    V =  a + b * math.log(c + d * D) + e * D
    
    return math.exp(V) / 1000

def stem_vol_100(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m

    a = 1.75055
    b = 1.10897
    c = -2.75863

    V =  D ** a * H ** b * math.exp(c)
    
    return V / 1000

def stem_vol_112(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m

    a = 0.3
    b = 0.02593
    c = 0.01268
    d = -0.0977
    e = 0.14586

    V =  a + b * D**2 * H + c * D * H**2 + d * H**2 + e * D * H
    
    return V / 1000

def stem_vol_124(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m

    a = 0.4693
    b = 1.311
    c = 0.781

    V =  a * D**b * H**c
    
    return V / 1000

def stem_vol_136(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m

    a = 1.89192
    b = 0.95374
    c = -2.72505

    V =  D ** a * H ** b * math.exp(c)
    
    return V / 1000

def stem_vol_148(dbh_m):
    D = dbh_m * 100

    a = -5.39417
    b = 3.48060
    c = 2
    d = 1.25
    e = -0.039884

    V =  a + b * math.log(c + d * D) + e * D
    
    return math.exp(V) / 1000

def stem_vol_160(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m

    a = 1.82075
    b = 1.07427
    c = -2.8885

    V =  D ** a * H ** b * math.exp(c)
    
    return V / 1000

def stem_vol_172(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m

    a = -1.20914
    b = 1.94740
    c = -0.05947
    d = 1.40958
    e = -0.45810

    V =  10**a * D**b * (D + 20)**c * H**d * (H - 1.3)**e
    
    return V / 1000

def stem_vol_184(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m

    a = -0.004298
    b = 0.0000435
    c = 0.89

    V =  a + b * D**2 * H**c
    
    return V

def stem_vol_196(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m

    a = 4.477e-5
    b = 1.8688
    c = 0.0424
    d = 1.1411
    e = -0.1047

    V = a * 10**b * math.log(D) + c * math.log(D)**2 + d * math.log(H) + e * math.log(H)**2

    return V

def stem_vol_208(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m

    a = -0.02149
    b = 0.002986681
    c = -4.2506e-5
    d = -2.1806e-6
    e = -0.000743
    f = 3.7473e-5

    V =  a + b * D + c * D**2 + d * D**3 + e * H + f * D**2 * H
    
    return V

def stem_vol_220(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m

    a = 4.281e-5
    b = 2.0766
    c = -0.1296
    d = 0.6843
    e = 0.2745
    
    V =  a * 10**b * math.log(D) + c * math.log(D)**2 + d * math.log(H) + e * math.log(H)**2
    
    return V







##equation measurments dbh in cm & height in m
def stem_vol_229(dbh_m,height_m):
    from math import exp
    a=1.94295
    b=1.29229
    c=-4.20064
    dbh_m=dbh_m*100
    v= dbh_m**a*height_m**b*exp(c)
    return v/1000
#dbh in cm &height in meters
def stem_vol_217(dbh_m,height_m):
    a=-0.011585
    b=0.0000765
    c=0.75
    dbh_m=dbh_m*100
    v= a+b*dbh_m**2*height_m**c
    return v
#dbh in cm & height in m while the the results are in ln(m3)
def stem_vol_205(dbh_m, height_m):
    #from math import log as ln
    from math import log
    from math import exp
    a=-11.473
    b=2.548
    c=0.967
    dbh_m=dbh_m*100
    v= a+b*log(dbh_m)+c*height_m

    return v

#dbh in cm and the height in m
def stem_vol_193(dbh_m,height_m):
    a=-0.019911
    b=0.001871101
    c=0.000127328
    d=-5.7631*10**-6
    e=0.00071591
    f=3.9371*10**-5
    dbh_m=dbh_m*100
    v= a+b*dbh_m+c*dbh_m**2+d*dbh_m**3+e*height_m+f*dbh_m**2*height_m
    return v


#dbh in cm height in m  && the results in dm^3
def stem_vol_181(dbh_m,height_m):
    a=0.0009507
    b=1.895629295
    c=-0.00773694
    d=0.8392146
    dbh_m=dbh_m*1000

    v1=a*dbh_m**(b+c)*height_m**d
    v=v1/1000
    return v

#dbh in cm and height in m 
def stem_vol_169(dbh_m,height_m):
    from math import log10
    a=0.00014808
    b=1.8341
    c=-0.0448
    d=0.3115
    e=0.3525
    dbh_m=dbh_m*100
    v= a*10**(b*log10(dbh_m)+c*log10(dbh_m)**2+d*log10(height_m)+e*log10(height_m)**2)
    return v

# dbh in mm height in m &&& the results are in dm^3
def stem_vol_157(dbh_m,height_m):
    a=0.00207765
    b=1.952764402
    c=-8.6651*10**-5
    d=0.48560878
    dbh_m=dbh_m*1000

    v=a*dbh_m**(b+c)*height_m**d
    return v/1000

#dbh in cm and the height in m 
def stem_vol_145 (dbh_m, height_m):
    a=0.000244
    b=2.32716
    dbh_m=dbh_m*100
    v=a*dbh_m**b
    return v
#dbh in cm height in m and the results in dm^3
def stem_vol_133(dbh_m,height_m):
    a=0.1121
    b=0.0287
    c=-0.000061
    d=0.09176
    e=0.01249
    dbh_m=dbh_m*100
    v=a*dbh_m**2+b*dbh_m**2*height_m+c*dbh_m**2*height_m**2-d*dbh_m*height_m+e*dbh_m*height_m**2
    return v/1000

# dbh in cm ,  height in m and the results in dm^3
def stem_vol_121(dbh_m,height_m):
    a=-1.06019 
    b=2.04239
    c=-0.54292
    d=2.80843
    e=-1.5211
    dbh_m=dbh_m*100
    v=10**a*dbh_m**b*(dbh_m+20)**c*height_m**d*(height_m-1.3)**e
    return v/1000
    

#dbh  in cm , height in m && results in dm^3   
def stem_vol_109(dbh_m,height_m):
    a=0.46
    b=0.02427
    c=0.01521
    d=-0.18254
    e=0.20994
    dbh_m=dbh_m*100
    

    v= a+b*dbh_m**2*height_m+c*dbh_m*height_m**2+d*height_m**2+e*dbh_m*height_m
    return v/1000
    

# dbh in mm , height in m && the results in dm^3
def stem_vol_97(dbh_m,height_m):
    a=0.00053238
    b=2.164126647
    c=0.004108377
    d=0.54879808
    dbh_m=dbh_m*1000
    v= (a*dbh_m**(b+c)*height_m**d)
    return v/1000


#dbh in cm , height in m 
def stem_vol_85(dbh_m,height_m):
    a=0.00059707 
    b=2.1286
    dbh_m=dbh_m*100
    v= a*dbh_m**b
    return v

#dbh in cm , height in m  we assume that the results are in dm^3 not in m^3
def stem_vol_73(dbh_m,height_m):
    from math import exp
    a=-2.9946
    b=1.8105
    c= 0.9908
    dbh_cm=dbh_m*100
    v= exp(a) * dbh_cm ** b * height_m ** c
    return v/1000

#dbh in cm , height in m && the results in dm^3
def stem_vol_61(dbh_m,height_m):
    a=-1.86827
    b=0.21461
    c=0.01283
    d=0.0138
    e=-0.06311
    dbh_m=dbh_m*100
    v1=a+b*dbh_m**2+c*dbh_m**2*height_m+d*dbh_m*height_m**2+e*height_m**2
    v=v1/1000
    return v


##dbh in cm , height in m 
def stem_vol_49(dbh_m,height_m):
    a=-0.015572
    b=0.00290013
    c=-7.0476*10**-6
    d=2.393*10**-6
    e=-0.0013528 
    f=3.9837*10**-5
    dbh_m=dbh_m*100
    v=a+b*dbh_m+c*dbh_m**2+d*dbh_m**3+e*height_m+f*dbh_m**2*height_m
    return v


#dbh in cm , height in m && results in dm^3
def stem_vol_37(dbh_m,height_m):
    a=-0.35394 
    b= 2.52141
    c=-1.54257
    d=4.88165
    e=-3.47422
    dbh_m=dbh_m*100
    v1= (10**a)*(dbh_m**b)*((dbh_m+20)**c)*(height_m**d)*((height_m-1.3)**e)
    v=v1/1000
    return v


#dbh in cm , height in m 
def stem_vol_25(dbh_m,height_m):
    a=-0.011392 
    b=-0.00031447
    c=0.000279211
    d=-5.7966*10**-6
    e=-5.9573*10**-4
    f=3.0409*10**-5
    dbh_m=dbh_m*100
    v=a+b*dbh_m+c*dbh_m**2+d*dbh_m**3+e*height_m+f*dbh_m**2*height_m
    return v

#dbh in cm , height in m 
def stem_vol_13(dbh_m,height_m):
    from math import log10
    a=0.00065013
    b=1.675
    c=0.1001
    d=-0.4990
    e=0.5902
    dbh_m=dbh_m*100
    v= a*10**(b*log10(dbh_m)+c*log10(dbh_m)**2+d*log10(height_m)+e*log10(height_m)**2)
    return v

#dbh in cm , height in m && results in dm^3
def stem_vol_1(dbh_m,height_m):
    a=1.6662
    b=3.2394
    c=1.9334
    d=-1.8997
    e=-0.9739
    dbh_m=dbh_m*100
    v=a*height_m**b*dbh_m**c*(height_m-1.3)**d*(dbh_m+100)**e
    return v/1000

def calculator_dbh(df_trees: pd.DataFrame,
                   fnc: list[typing.Callable],
                   col_map: typing.Dict):
    """
    pass functions to calculate the volume of the trees on a batch of data
    :param col_map: dictionary mapping with the column names
    :param df_trees: pandas dataframe with the data
    :param fnc: list of functions to calculate the volume
    :return: pandas dataframe with the volume calculated
    """
    def wrapper_d(row: pd.Series, f: typing.Callable) -> pd.Series:
        """
        :param row: row of the dataframe which contains a diameter
        :param f: function to calculate the diameter with only the diameter
        :return: modified row
        """
        row[f.__name__] = f(row[col_map["diameter"]])
        return row

    for f in fnc:
        df_trees = df_trees.apply(wrapper_d, f=f, axis=1)

    return df_trees


def calculator_dbh_h(df_trees: pd.DataFrame,
                     fnc: list[typing.Callable],
                     col_map: typing.Dict):
    """
    pass functions to calculate the volume of the trees on a batch of data
    :param col_map: dictionary mapping with the column names
    :param df_trees: pandas dataframe with the data
    :param fnc: list of functions to calculate the volume
    :return: pandas dataframe with the volume calculated
    """
    def wrapper_d(row: pd.Series, f: typing.Callable) -> pd.Series:
        """
        :param row: row of the dataframe which contains a diameter and height
        :param f: function to calculate the volume
        :return: modified row
        """
        row[f.__name__] = f(row[col_map["diameter"]], row[col_map["height"]])
        return row

    for f in fnc:
        df_trees = df_trees.apply(wrapper_d, f=f, axis=1)

    return df_trees


def stem_vol_3(dbh_m, height_m, a=1.6662, b=3.2394, c=1.9334, d=-1.8997, e=-0.9739) -> float:
    D_cm = dbh_m * 100
    V = a * height_m ** b * D_cm ** c * (height_m - 1.3) ** d * (D_cm + 100) ** e

    return V / 1000


def stem_vol_15(dbh_m, height_m, a=8.6524, b=0.076844, c=0.031573) -> float:
    D = dbh_m * 100
    H = height_m
    V = a + b * D ** 2 + c * D ** 2 * H

    return V / 1000


def stem_vol_27(dbh_m, a=-5.41948, b=3.57630, c=2, d=1.25, e=-0.0395855) -> float:
    # TODO fix this, or its very far off. There is a chance this function actually return cubic meters
    """
    The original paper is: https://jukuri.luke.fi/handle/10024/522516
    the equation can be found in the page 42, eq 61.2, for birch it states
    The paper state the result is ln(v), Zianis et al. 2005, quoted that incorrectly on page 44, formula 27.

    :return:
    """
    D = dbh_m * 100

    V = a + b * math.log(c + d * D) + e * D
    # V = math.exp(V) # the paper suggests that the result is ln(v), but the result is even worse then
    return V / 1000


def stem_vol_39(dbh_m, height_m, a=-0.009184, b=0.0000673, c=0.75) -> float:
    D = dbh_m * 100
    H = height_m

    V = a + b * D ** 2 * H ** c

    return V


def stem_vol_51(dbh_m, height_m, a=16.641e-3, b=0.72179e-3, c=0.00252e-3) -> float:
    D = dbh_m * 100
    H = height_m * 10
    V = a + b * D * H ** 2 + c * D ** 3

    return V / 1000


def stem_vol_63(dbh_m, height_m, a=-0.012107, b=0.0000777, c=0.75) -> float:
    D = dbh_m * 100
    H = height_m

    V = a + b * D ** 2 * H ** c

    return V


def stem_vol_75(dbh_m, height_m, a=0.7761, b=3.6461, c=1.9166, d=-2.3179, e=-0.8236) -> float:
    D = dbh_m * 100
    H = height_m

    V = a * H ** b * D ** c * (H - 1.3) ** d * (D + 100) ** e

    return V / 1000


def stem_vol_87(dbh_m, a=-2.41218, b=2.62463) -> float:
    D = dbh_m * 100
    V = a + b * math.log(D)

    return math.exp(V) / 1000


def stem_vol_99(dbh_m, height_m, a=0.00053238, b=2.164126647, c=-0.0102582, d=0.54879808) -> float:
    D = dbh_m * 1000
    H = height_m

    V = a * D ** (b + c) * H ** d

    return V / 1000


def stem_vol_111(dbh_m, height_m, a=0.28, b=0.00815, c=0.03053, d=-0.50725, e=0.51643) -> float:
    D = dbh_m * 100
    H = height_m

    V = a + b * D ** 2 * H + c * D * H ** 2 + d * H ** 2 + e * D * H
    return V / 1000


def stem_vol_123(dbh_m, height_m, a=-1.0342, b=1.9683, c=-0.3850, d=2.4018, e=-1.2075) -> float:
    D = dbh_m * 100
    H = height_m

    V = 10 ** a * D ** b * (D + 20) ** c * H ** d * (H - 1.3) ** e
    return V / 1000


def stem_vol_135(dbh_m, height_m, a=0.0883, b=0.03202, c=-0.000114, d=-0.07892, e=-0.01049) -> float:
    D = dbh_m * 100
    H = height_m
    V = a * D ** 2 + b * D ** 2 * H + c * D ** 2 * H ** 2 - d * D * H + e * D * H ** 2
    return V / 1000


def stem_vol_147(dbh_m, a=-2.2945, b=2.57025) -> float:
    D = dbh_m * 100
    V = a + b * math.log(D)
    return math.exp(V) / 1000


def stem_vol_159(dbh_m, height_m, a=0.00207765, b=1.952764402, c=0.001095496, d=0.48560878) -> float:
    D = dbh_m * 1000
    H = height_m
    V = a * D ** (b + c) * H ** d
    return V / 1000


def stem_vol_171(dbh_m, height_m, a=-1.1226, b=2.0180, c=-0.2135, d=1.8271, e=-0.8297) -> float:
    D = dbh_m * 100
    H = height_m
    V = 10 ** a * D ** b * (D + 20) ** c * H ** d * (H - 1.3) ** e
    return V / 1000


def stem_vol_183(dbh_m, height_m, a=0.00041486, b=1.4466, c=0.1089, d=-0.1963, e=0.5681) -> float:
    D = dbh_m * 100
    H = height_m
    V = a * 10 ** (b * math.log(D, 10) + c * math.log(D, 10) ** 2 + d * math.log(H, 10) + e * math.log(H, 10) ** 2)
    return V


def stem_vol_195(dbh_m, height_m, a=1.8211, b=4.153, c=2.1342, d=-2.6902, e=-1.4265) -> float:
    D = dbh_m * 100
    H = height_m
    V = a * H ** b * D ** c * (H - 1.3) ** d * (D + 40) ** e
    return V / 1000


def stem_vol_207(dbh_m, height_m, a=2.00333, b=0.85925, c=-2.86353) -> float:
    D = dbh_m * 100
    H = height_m
    V = D ** a * H ** b * math.exp(c)
    return V / 1000


def stem_vol_219(dbh_m, height_m, a=0.00011585, b=1.6688, c=0.1090, d=0.7781, e=0.0269) -> float:
    D = dbh_m * 100
    H = height_m
    V = a * 10 ** (b * math.log(D, 10) + c * math.log(D, 10) ** 2 + d * math.log(H, 10) + e * math.log(H, 10) ** 2)
    return V


def stem_vol_230(dbh_m, height_m, a=0.00003992, b=2.1569, c=-0.0933, d=1.0728, e=-0.0708) -> float:
    D_cm = dbh_m * 100
    return a * 10 ** (b * math.log(D_cm, 10) + c * math.log(D_cm, 10) ** 2 + d * math.log(height_m, 10) + e * math.log(
        height_m, 10) ** 2)


def stem_vol_2( dbh_m, height_m ):    
    dbh_cm = dbh_m * 100 
    # constants
    a = 1.77220  
    b = 0.96736 
    c = -2.45224

    volum_dm3 = ( dbh_cm ** a ) * ( height_m ** b) * exp( c )
    volume_m3 = volum_dm3 / 1000
    return volume_m3

def stem_vol_14( dbh_m, height_m ):
    dbh_cm = dbh_m * 100 
    # constants
    a = 1.85749  
    b = 0.88675
    c = -2.5222

    volum_dm3 = ( dbh_cm ** a) * ( height_m **b ) * exp( c )
    volume_m3 = volum_dm3 / 1000
    return volume_m3

def stem_vol_26( dbh_m, height_m ):
    # constants
    a = -2.09787
    b = 2.55058

    dbh_cm = dbh_m * 100
    volume_ln_dm3 = a + ( b * ( ln ( dbh_cm ) ) )
    volume_dm3 = exp( volume_ln_dm3 )
    volume_m3 = volume_dm3 / 1000
    return volume_m3

def stem_vol_38( dbh_m, height_m ):
    a = 0.143 
    b = 0.008561
    c = 0.02180
    d = -0.06630
    dbh_cm = dbh_m * 100
    

    volume_dm3 = a *( dbh_cm*dbh_cm ) + b * ( dbh_cm * dbh_cm ) * height_m + c * dbh_cm * ( height_m * height_m) + d * ( height_m * height_m )
    volume_m3 = volume_dm3 / 1000
    return volume_m3

def stem_vol_50( dbh_m, height_m ):
    a = 15.589 * (10 ** -3)
    b = 0.01696 * (10 ** -3)
    c = 0.01883 * (10 ** -3)
    dbh_cm = dbh_m * 100
    height_dm = height_m * 10

    volume_dm3 = a + (b * dbh_cm * (height_dm**2)) + (c * (dbh_cm**3))
    volume_m3 = volume_dm3 / 1000
    return volume_m3

def stem_vol_62( dbh_m, height_m ):
    a = 0.00030648
    b = 1.2676
    c = 0.3102
    d = 0.4929
    e = 0.0962
    dbh_cm = dbh_m * 100

    volume_m3 = a * 10 ** (
        b * log10( dbh_cm ) + 
        c * (log10( dbh_cm)) ** 2 + 
        d * log10( height_m ) + 
        e * ( log10( height_m ))**2
        )
    return volume_m3

def stem_vol_74( dbh_m, height_m ):
    a = 0.0983 
    b = 1.551 
    c = 1.1483
    dbh_cm = dbh_m * 100

    # formula mentioned in Zianis et al. says the output volume is in m3, but it is in dm3 actually.
    # therefore converting the output from dm3 to m3
    volume_dm3 = a * (dbh_cm ** b) * (height_m ** c)
    volume_m3 = volume_dm3/1000
    return volume_m3

def stem_vol_86(dbh_m, height_m):
    """
    Calculate the stem volume of a tree using the 86 Czech Republic formula.

    Parameters:
    dbh_m (float): Diameter at breast height (in meters).
    height_m (float): Height of the tree (in meters).

    Returns:
    float: The calculated stem volume in cubic meters.
    """
    # 86 Czech Republic a·(H·D**2)**b
    a = 0.00011261
    b = 0.87852

    dbh_cm = dbh_m * 100

    volume_m3 = a * ((height_m * (dbh_m ** 2)) ** b)
    return volume_m3


def stem_vol_98( dbh_m, height_m ):
    """
    Calculate the volume of a tree stem.

    Parameters:
    dbh_m (float): The diameter at breast height (DBH) of the tree in meters.
    height_m (float): The height of the tree in meters.

    Returns:
    float: The volume of the tree stem in cubic meters.
    """
    a = 0.00053238
    b = 2.164126647
    c = -0.04670018
    d = 0.54879808
    dbh_mm = dbh_m * 1000

    volume_dm3 = a *( dbh_mm ** (b+c) )*(height_m**d)
    volume_m3 = volume_dm3 / 1000

    return volume_m3

def stem_vol_110( dbh_m, height_m ):
    # expects: cm, m
    # Outputs:dm3
    # 110 Norway a+b·D2·H+c·D·H2+d·D2
    a = 0.67
    b = 0.03023
    c = 0.00712
    d = 0.04175

    dbh_cm = dbh_m * 100
    volume_dm3 = a + b * (dbh_cm ** 2) * height_m + c * dbh_cm * (height_m ** 2) + d * (dbh_cm ** 2)
    volume_m3 = volume_dm3 / 1000

    return volume_m3

def stem_vol_122( dbh_m, height_m ):
    """
    Calculate the stem volume of a tree using the 122 formula.

    Parameters:
    dbh_m (float): Diameter at breast height (in meters).
    height_m (float): Height of the tree (in meters).

    Returns:
    float: The stem volume of the tree in cubic meters.
    """

    a = 0.1104
    b = 0.01925
    c = 0.01815
    d = -0.04936

    dbh_cm = dbh_m * 100
    volume_dm3 = a * (dbh_cm ** 2) + b * (dbh_cm ** 2) * height_m + c * dbh_cm * (height_m ** 2) + d * (height_m ** 2)
    volume_m3 = volume_dm3 / 1000
    return volume_m3

def stem_vol_134(dbh_m, height_m):
    """
    Calculate the stem volume using the 134 Sweden formula.

    Args:
        dbh_m (float): Diameter at breast height in meters.
        height_m (float): Tree height in meters.

    Returns:
        float: Stem volume in cubic meters.
    """
    a = 0.04514
    b = 1.9005
    c = 1.06964

    dbh_cm = dbh_m * 100
    volume_dm3 = a * dbh_cm ** b * height_m ** c
    volume_m3 = volume_dm3 / 1000

    return volume_m3

def stem_vol_146(dbh_m, height_m):
    """
    NOTE: The formula is not correct. The power of the constants b-f were multiplied 10*-1.
    Calculates the stem volume of a tree using the 146 Belgium formula.

    Args:
        dbh_m (float): Diameter at breast height (DBH) in meters.
        height_m (float): Height of the tree in meters.

    Returns:
        float: The stem volume of the tree in cubic meters.
    """
    a = -0.039836
    b = 4.8710 * 10 ** -3
    c = -6.1028 * 10 ** -5
    d = 1.4889 * 10 ** -5
    e = 7.3997 * 10 ** -5
    f = 2.9221 * 10 ** -5

    dbh_cm = dbh_m * 100
    volume_m3 = a+ b * dbh_cm +c * dbh_cm **2 + d * dbh_cm ** 3 + e * height_m + f * dbh_cm**2 * height_m
    return volume_m3

def stem_vol_158( dbh_m, height_m ):
    """
    Calculates the stem volume using the 158 Netherlands a·D(b+c)·Hd formula.

    Args:
        dbh_m (float): Diameter at breast height in meters.
        height_m (float): Tree height in meters.

    Returns:
        float: Stem volume in cubic meters.
    """
    a = 0.00207765
    b = 1.952764402
    c = -0.11110535
    d = 0.48560878

    dbh_mm = dbh_m * 1000

    volume_dm3 = a * (dbh_mm ** (b + c)) * (height_m ** d)
    volume_m3 = volume_dm3 / 1000
    return volume_m3

def stem_vol_170( dbh_m, height_m ):
    """
    Calculates the stem volume of a tree using the 170 Sweden formula.

    Args:
        dbh_m (float): Diameter at breast height (in meters).
        height_m (float): Height of the tree (in meters).

    Returns:
        float: Stem volume of the tree (in cubic meters).
    """
    a = 0.1028
    b = 0.02705
    c = 0.005215

    dbh_cm = dbh_m * 100
    volume_dm3 = a * (dbh_cm ** 2) + b * (dbh_cm ** 2) * height_m + c * dbh_cm * (height_m ** 2)
    volume_m3 = volume_dm3 / 1000

    return volume_m3


def stem_vol_182(dbh_m, height_m):
    """
    Calculates the stem volume of a tree using the 182 Romania formula.

    Args:
        dbh_m (float): Diameter at breast height in meters.
        height_m (float): Tree height in meters.

    Returns:
        float: The stem volume of the tree in cubic meters.
    """
    a = 0.00018059
    b = 1.9342
    c = 0.0013
    d = 0.0161
    e = 0.4099

    dbh_cm = dbh_m * 100
    volume_m3 = a * 10 ** (b * log10(dbh_cm) + c * log10(dbh_cm) ** 2 + d * log10(height_m) + e * log10(height_m) ** 2)

    return volume_m3


def stem_vol_194(dbh_m, height_m):
    """
    Calculates the stem volume using the 194 Netherlands Da·Hb·exp(c) formula.

    Args:
        dbh_m (float): Diameter at breast height in meters.
        height_m (float): Tree height in meters.

    Returns:
        float: Stem volume in cubic meters.
    """
    a = 1.90053
    b = 0.80726
    c = -2.43151
    dbh_cm = dbh_m * 100

    volume_dm3 = dbh_cm ** a * height_m ** b * exp(c)
    volume_m3 = volume_dm3 / 1000

    return volume_m3

def stem_vol_206(dbh_m, height_m):
    """
    Calculates the stem volume of a tree using the 206 Romania formula.

    Args:
        dbh_m (float): Diameter at breast height (in meters).
        height_m (float): Tree height (in meters).

    Returns:
        float: Stem volume of the tree in cubic meters.
    """
    a = 0.00035164
    b = 1.1119
    c = 0.3108
    d = 0.5356
    e = 0.2139
    dbh_cm = dbh_m * 100

    volume_m3 = a * 10 ** (b * log10(dbh_cm) + c * log10(dbh_cm) ** 2 + d * log10(height_m) + e * log10(height_m) ** 2)
    return volume_m3

def stem_vol_218( dbh_m, height_m ):
    """
    Calculate the stem volume of a tree using the 218 Norway formula.

    Args:
        dbh_m (float): Diameter at breast height (DBH) of the tree in meters.
        height_m (float): Height of the tree in meters.

    Returns:
        float: The stem volume of the tree in cubic meters.
    """
    a = -1.86827
    b = 0.21461
    c = 0.01283
    d = 0.0138
    e = -0.06311

    dbh_cm = dbh_m * 100
    volume_dm3 = a + b * dbh_cm ** 2 + c * dbh_cm ** 2 * height_m + d * dbh_cm * height_m ** 2 + e * height_m ** 2
    volume_m3 = volume_dm3 / 1000
    return volume_m3




def convert_to_cm(meters):
    """Convert meters to centimeters."""
    return meters * 100

def convert_to_mm(meters):
    """Convert meters to millimeters."""
    return meters * 1000

def convert_volume_to_m3(volume_dm3):
    """Convert volume from cubic decimeters to cubic meters."""
    return volume_dm3 / 1000

def calculate_logarithmic_volume(a, b, c, d, e, dbh_cm, height_m):
    """Calculate volume using logarithmic and polynomial components."""
    logD = math.log10(dbh_cm)
    logH = math.log10(height_m)
    exponent = (b * logD + c * logD**2 + d * logH + e * logH**2)
    return a * 10 ** exponent


def stem_vol_8(dbh_m, height_m):
    dbh_cm = convert_to_cm(dbh_m)
    return calculate_logarithmic_volume(0.00046903, 1.807, 0.0292, -0.4155, 0.5455, dbh_cm, height_m)

def stem_vol_20(dbh_m, height_m):
    dbh_cm = convert_to_cm(dbh_m)
    a = -1.86827
    b = 0.21461
    c = 0.01283
    d = 0.0138
    e = -0.06311
    volume_dm3 = a + b * dbh_cm**2 + c * dbh_cm**2 * height_m + d * dbh_cm * height_m**2 + e * height_m**2
    return convert_volume_to_m3(volume_dm3)


def stem_vol_32(dbh_m, height_m):
    dbh_cm = convert_to_cm(dbh_m)
    a = 8.141 * 10**-5
    b = 2.248
    c = -0.2062
    d = 0.1946
    e = 0.4147
    volume_m3 = calculate_logarithmic_volume(a, b, c, d, e, dbh_cm, height_m)
    return volume_m3  # Outputs directly in cubic meters

def stem_vol_44(dbh_m, height_m):
    dbh_cm = convert_to_cm(dbh_m)
    a = -1.86827
    b = 0.21461
    c = 0.01283
    d = 0.0138
    e = -0.06311
    volume_dm3 = a + b * dbh_cm**2 + c * dbh_cm**2 * height_m + d * dbh_cm * height_m**2 + e * height_m**2
    return convert_volume_to_m3(volume_dm3)  # Convert from dm3 to m3.

def stem_vol_56(dbh_m, height_m):
    dbh_cm = convert_to_cm(dbh_m)
    a = 0.03246
    b = 0.03310
    c = 0.04127
    volume_dm3 = a * dbh_cm**2 * height_m + b * dbh_cm**2 + c * dbh_cm * height_m
    return convert_volume_to_m3(volume_dm3)  # Convert from dm3 to m3.




def stem_vol_68(dbh_m, height_m):
    dbh_cm = convert_to_cm(dbh_m)
    a = 0.7761
    b = 3.6461
    c = 1.9166
    d = -2.3179
    e = -0.8236
    H_power_b = height_m ** b
    D_power_c = dbh_cm ** c
    H_minus_1_3_power_d = (height_m - 1.3) ** d
    D_plus_100_power_e = (dbh_cm + 100) ** e
    volume_dm3 = a * H_power_b * D_power_c * H_minus_1_3_power_d * D_plus_100_power_e
    return convert_volume_to_m3(volume_dm3)

def stem_vol_80(dbh_m, height_m):
    dbh_mm = convert_to_mm(dbh_m)  # Convert to millimeters as needed
    a = 0.00035217
    b = 2.12841828
    c = -0.0026067
    d = 0.76283925
    D_power = dbh_mm ** (b + c)
    H_power = height_m ** d
    volume_dm3 = a * D_power * H_power
    return convert_volume_to_m3(volume_dm3)

def stem_vol_92(dbh_m, height_m):
    dbh_cm = convert_to_cm(dbh_m)
    a = 0.10838
    b = 1.8202
    c = 0.77154
    volume_dm3 = a * (dbh_cm ** b) * (height_m ** c)
    return convert_volume_to_m3(volume_dm3)

def stem_vol_104(dbh_m, height_m):
    dbh_cm = convert_to_cm(dbh_m)
    a = 0.5824
    b = 1.1987
    c = 1.9339
    d = -0.0594
    e = -0.7442
    H_power_b = height_m ** b
    D_power_c = dbh_cm ** c
    H_minus_1_3_power_d = (height_m - 1.3) ** d
    D_plus_40_power_e = (dbh_cm + 40) ** e
    volume_dm3 = a * H_power_b * D_power_c * H_minus_1_3_power_d * D_plus_40_power_e
    return convert_volume_to_m3(volume_dm3)

def stem_vol_116(dbh_m, height_m):
    dbh_cm = convert_to_cm(dbh_m)
    a = 0.1150
    b = 0.01746
    c = 0.02022
    d = -0.05618
    D_squared = dbh_cm ** 2
    volume_dm3 = a * D_squared + b * D_squared * height_m + c * dbh_cm * height_m ** 2 + d * height_m ** 2
    return convert_volume_to_m3(volume_dm3)

def stem_vol_128(dbh_m, height_m):
    dbh_cm = convert_to_cm(dbh_m)
    a = 0.2101
    b = 1.8920
    c = 1.1095
    d = -0.3895
    D_power_b = dbh_cm ** b
    H_minus_1_3_power_c = (height_m - 1.3) ** c
    D_plus_40_power_d = (dbh_cm + 40) ** d
    volume_dm3 = a * D_power_b * H_minus_1_3_power_c * D_plus_40_power_d
    return convert_volume_to_m3(volume_dm3)

def stem_vol_140(dbh_m):
    dbh_cm = convert_to_cm(dbh_m)
    a = 0.0001078
    b = 2.56
    volume_m3 = a * (dbh_cm ** b)  # Directly in m^3, no dm^3 involved
    return volume_m3

def stem_vol_152(dbh_m, height_m):
    dbh_cm = convert_to_cm(dbh_m)
    a = 0.095
    b = 1.9185
    c = 0.7381
    volume_dm3 = a * (dbh_cm ** b) * (height_m ** c)
    return convert_volume_to_m3(volume_dm3)

def stem_vol_164(dbh_m, height_m):
    dbh_cm = convert_to_cm(dbh_m)
    a = 8.6524
    b = 0.076844
    c = 0.031573
    D_squared = dbh_cm ** 2
    volume_dm3 = a + b * D_squared + c * D_squared * height_m
    return convert_volume_to_m3(volume_dm3)

def stem_vol_176(dbh_m, height_m):
    dbh_cm = convert_to_cm(dbh_m)
    a = 0.1072
    b = 0.02427
    c = 0.007315
    D_squared = dbh_cm ** 2
    volume_dm3 = a * D_squared + b * D_squared * height_m + c * dbh_cm * height_m ** 2
    return convert_volume_to_m3(volume_dm3)

def stem_vol_188(dbh_m, height_m):
    dbh_cm = convert_to_cm(dbh_m)
    a = 0.01548
    b = 0.03255
    c = -0.000047
    d = -0.01333
    e = 0.004859
    D_squared = dbh_cm ** 2
    volume_dm3 = a * D_squared + b * D_squared * height_m + c * D_squared * (height_m ** 2) + d * dbh_cm * height_m + e * dbh_cm * (height_m ** 2)
    return convert_volume_to_m3(volume_dm3)

def stem_vol_200(dbh_m, height_m):
    dbh_cm = convert_to_cm(dbh_m)
    a = 7.188 * 10**-5
    b = 1.4486
    c = 0.0204
    d = 1.4084
    e = 0.0409
    volume_m3 = calculate_logarithmic_volume(a, b, c, d, e, dbh_cm, height_m)
    return volume_m3

def stem_vol_212(dbh_m, height_m):
    dbh_cm = convert_to_cm(dbh_m)
    a = -0.0022735
    b = 0.000389557
    c = 0.000124772
    d = -1.8434 * 10**-6
    e = -0.0016657
    f = 3.6985 * 10**-5
    volume_m3 = a + b * dbh_cm + c * dbh_cm**2 + d * dbh_cm**3 + e * height_m + f * dbh_cm**2 * height_m
    return volume_m3  # Directly in m3, no dm3 involved

def stem_vol_224(dbh_m, height_m):
    dbh_cm = convert_to_cm(dbh_m)
    a = 1.3057
    b = 3.9075
    c = 1.9832
    d = -2.3337
    e = -1.3024
    H_power_b = height_m ** b
    D_power_c = dbh_cm ** c
    H_minus_1_3_power_d = (height_m - 1.3) ** d
    D_plus_40_power_e = (dbh_cm + 40) ** e
    volume_dm3 = a * H_power_b * D_power_c * H_minus_1_3_power_d * D_plus_40_power_e
    return convert_volume_to_m3(volume_dm3)

def stem_vol_9(D,H) :
    a=0.010343
    b=-0.00450536
    c=3.4070*10**-4
    d=-4.0472*10**-6
    e=7.7115*10**-4
    f=2.9836*10**-5
    D=D*100 
    return a+b*D+c*D**2+d*D**3+e*H+f*D**2*H
    
def stem_vol_21(D,H) :
    from math import log10
    a=8.666*10**-5
    b=1.7148
    c=0.1014
    d=0.801
    e=0.0530
    D=D*100
    return a*10**(b*log10(D)+c*log10(D)**2+d*log10(H)+e*log10(H)**2)

def stem_vol_33(D,H) :
    a=0.1305
    b=0.01338
    c=0.01757
    d=-0.05606
    D=D*100
    return (a*D**2+b*D**2*H+c*D*H**2+d*H**2)/1000
    
def stem_vol_45(D,H) :
    import math
    from math import pi, log
    a=0.989253
    b=-0.0371508
    c=-31.0674
    d=-0.386321
    e=0.219462 
    f=49.6136
    g=-22.372
    D=D*10
    H=H*10
    return ((math.pi/4)*(a*D**2*H+b*D**2*H*log(D)**2+c*D**2+d*D*H+e*H+f*D+g))/1000
     
def stem_vol_57(D,H) :
    a=0.03593
    b=0.03310
    c=0.04127 
    D=D*100
    return (a*D**2*H+b*D**2+c*D*H)/1000
    
def stem_vol_69(D,H) :
    a=0.7761
    b=3.6461
    c=1.9166
    d=-2.3179
    e=-0.8236
    D=D*100
    return (a*H**b*D**c*(H-1.3)**d*(D+100)**e)/1000
    
def stem_vol_81(D,H) :
    from math import log10
    a=2.822*10**-5 
    b=2.2060
    c=-0.1136 
    d=1.115
    e=0.0129
    D=D*100
    return a*10**(b*log10(D)+c*log10(D)**2+d*log10(H)+e*log10(H)**2)
    
def stem_vol_93(D,H) :
    from math import e, log
    a=-2.59385  
    b=2.71757
    c=-0.000097 
    D=D*100
    return e**a+b*log(D)+c*D**2/1000
    
def stem_vol_105(D,H) :
    a=0.52   
    b=0.02403
    c=0.01463
    d=-0.10983
    e=0.15195
    D=D*100
    return (a+b*D**2*H+c*D*H**2+d*H**2+e*D*H)/1000
    
def stem_vol_117(D,H) :
    a=-0.9513  
    b=1.9781
    c=-0.5254 
    d=2.7604
    e=-1.4684
    D=D*100
    return (10**a*D**b*(D+20)**c*H**d*(H-1.3)**e)/1000
    
def stem_vol_129(D,H) :
    from math import log10
    a=0.00009464  
    b=1.9341
    c=-0.0722 
    d=0.6365
    e=0.172 
    D=D*100
    return a*10**(b*log10(D)+c*log10(D)**2+d*log10(H)+e*log10(H)**2)
    
def stem_vol_141(D,H) :
    a=0.00042613 
    b=2.066225947
    c=-0.001926657
    d=0.80636901 
    D=D*1000
    return (a*D**(b+c)*H**d)/1000
    
def stem_vol_153(D,H) :
    a=0.05782  
    b=0.11632 
    c=-0.01092 
    d=-0.01317
    D=D*100
    return (a*H*D**2+b*D*H+c*D**3+d*D*H**2)/1000
    
def stem_vol_165(D,H) :
    a=0.6716
    b=0.075708 
    c=0.029679 
    #there is no parameter d in the article
    D=D*100
    #return (a+b*D**2+c*D**2*H+d*D*H**2)/1000
    return (a+b*D**2+c*D**2*H)/1000
    
def stem_vol_177(D,H) :
    a=-1.2605
    b=1.9322  
    c=-0.0897
    d=2.1795
    e=-1.1676
    D=D*100
    return (10**a*D**b*(D+20)**c*H**d*(H-1.3)**e)/1000
    
def stem_vol_189(D,H) :
    a=0.03597
    b=1.84297  
    c=1.15988
    D=D*100
    return (a*D**b*H**c)/1000
    
def stem_vol_201(D,H) :
    a=1.1909
    b=0.038639  
    D=D*100
    return (a+b*D**2*H)/1000

def stem_vol_213(D,H) :
    a=0.00095853
    b=2.040672356
    c=0.001965013
    d=0.56366437    
    D=D*1000
    return (a*D**(b+c)*H**d)/1000
    
def stem_vol_225(D,H) :
    from math import log10
    a=0.004124
    b=1.9302
    c=0.0209
    d=0.129
    e=-0.1903    
    D=D*100
    return a*10**(b*log10(D)+c*log10(D)**2+d*log10(H)+e*log10(H)**2)


# Function for equation 12
def stem_vol_12(dbh_m, height_m):
    D = dbh_m * 100  
    H = height_m
    a = -0.012668
    b = 0.0000737
    c = 0.75
    V = a + b * D**2 * math.pow(H, c)  
    return V / 1000  

# Function for equation 24
def stem_vol_24(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m
    a = 1.8906
    b = 26595
    c = -1.07055
    V = (math.pi / 4) * (a * D**2 * H + b * D**2 + c * D)  
    return V / 1000 

# Function for equation 36
def stem_vol_36(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m
    a = -0.44224
    b = 2.4758
    c = -1.40854
    d = 5.16863
    e = -3.77147
    V = 10 * a * D**b * math.pow(D + 20, c) * math.pow(H, d) * math.pow(H - 1.3, e)
    return V / 1000  

# Function for equation 48
def stem_vol_48(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m
    a = -0.014306
    b = 0.0000748
    c = 0.75
    V = a + b * D**2 * math.pow(H, c)  
    return V / 1000  

# Function for equation 60
def stem_vol_60(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m
    a = 0.03453
    b = 0.02941
    c = 0.03892
    V = a * D**2 * H + b * D**2 + c * D * H  
    return V / 1000  

# Function for equation 72
def stem_vol_72(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m
    a = math.exp(-2.5079)
    b = 1.7574
    c = 0.9808
    V = a * D**b * math.pow(H, c)  
    return V / 1000  

# Function for equation 84
def stem_vol_84(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m
    a = -0.010929
    b = 0.004380951
    c = -9.4713e-5
    d = -7.8024e-6
    e = -0.00279222
    f = 4.8346e-5
    V = a + b * D + c * D**2 + d * D**3 + e * H + f * D**2 * H 
    return V / 1000  

# Function for equation 96
def stem_vol_96(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m
    a = 0.1299
    b = 1.6834
    c = 0.8598
    V = a * D**b * math.pow(H, c)  
    return V / 1000  

# Function for equation 108
def stem_vol_108(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m
    a = 6.69
    b = 0.01308
    c = -0.31956
    d = 0.28969
    V = a + b * D**2 * H + c * D * H**2 + d * H**2  # Cubic centimeters
    return V / 1000  # Convert to cubic meters

# Function for equation 120
def stem_vol_120(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m
    a = -0.82249
    b = 2.11094
    c = -0.89626
    d = 3.51812
    e = -2.05567
    V = 10 * a * D**b * math.pow(D + 20, c) * math.pow(H, d) * math.pow(H - 1.3, e)  # Cubic centimeters
    return V / 1000  # Convert to cubic meters

# Function for equation 132
def stem_vol_132(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m
    a = 1.89303
    b = 0.98667
    c = -2.88614
    V = D**a * H**b * math.exp(c)  # Cubic centimeters
    return V / 1000  # Convert to cubic meters

# Function for equation 144
def stem_vol_144(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m
    a = 0.435949
    b = -0.0149083
    c = 5.21091
    d = 0.028702
    V = (math.pi / 4) * (a * D**2 * H + b * D**2 * H * math.log(D)**2 + c * D**2 + d * H)
    return V / 1000  # Convert to cubic meters

# Function for equation 156
def stem_vol_156(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m
    a = 1.480589
    b = 1.982459514
    c = 0.742674501
    V = a * D**b * math.pow(H, c)  # Cubic centimeters
    return V / 1000  # Convert to cubic meters

# Function for equation 168
def stem_vol_168(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m
    a = 2.9361
    b = 0.038906
    V = a + b * D**2 * H  # Cubic centimeters
    return V / 1000  # Convert to cubic meters

# Function for equation 180
def stem_vol_180(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m
    a = 0.0009507
    b = 1.895629295
    c = -0.09208823
    d = 0.8392146
    V = a * D**(b + c) * math.pow(H, d)  # Cubic centimeters
    return V / 1000  # Convert to cubic meters

# Function for equation 192
def stem_vol_192(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m
    a = -0.002311
    b = -0.00117728
    c = 0.000149061
    d = -7.8058e-6
    e = 3.3282e-4
    f = 3.1526e-5
    V = a + b * D + c * D**2 + d * D**3 + e * H + f * D**2 * H  # Cubic centimeters
    return V / 1000  # Convert to cubic meters

# Function for equation 204
def stem_vol_204(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m
    a = -9.646
    b = 2.076
    c = 0.761
    V = a + b * math.log(D) + c * H  # Cubic centimeters
    return V / 1000  # Convert to cubic meters

# Function for equation 216
def stem_vol_216(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m
    a = 8.839e-5
    b = 1.8905
    c = 0.0469
    d = 0.8059
    e = -0.0045  # Possible source of negative results
    # Check for valid inputs for logarithmic operations
    if D <= 0 or H <= 0:
        raise ValueError("Diameter and height must be positive.")
    V = a * 10**(b * math.log(D) + c * math.log(D)**2 + d * math.log(H) + e * math.log(H)**2)
    return V / 1000  # Convert to cubic meters

# Function for equation 228
def stem_vol_228(dbh_m, height_m):
    D = dbh_m * 100
    H = height_m
    a = -0.034716
    b = 0.004268168
    c = -0.00013227
    d = -1.7667e-6
    e = 0.00016516
    f = 3.8311e-5
    V = a + b * D + c * D**2 + d * D**3 + e * H + f * D**2 * H  # Cubic centimeters
    return V / 1000  # Convert to cubic meters

def stem_vol_7(dbh_cm, height_m):
    from math import log10
    a=0.0000452
    b=2.1554
    c=-0.1067
    d=0.9380
    e=0.0228
    D=dbh_cm * 100
    H=height_m
    result = a*10**(b*log10(D)+c*log10(D)**2+d*log10(H)+e*log10(H)**2)
    return result
    
def stem_vol_19(dbh_cm, height_m):
    from math import pi
    a=0.2264
    b=0.01347
    c=0.007665
    d=-0.06669
    e=0.000428
    D=dbh_cm * 100
    H=height_m
    return (a*D**2+b*D**2*H+c*D*H**2+d*D*H+e*D**2*H**2)/1000
    
def stem_vol_31(dbh_cm, height_m):
    from math import pi
    a=0.99983
    b=0.006325
    c=0.02849
    d=0.00885
    e=-0.00799
    D=dbh_cm * 100
    H=height_m
    return a+b*D**2+c*D**2*H+d*D*H**2+e*H**2
    
def stem_vol_43(dbh_cm, height_m):
    from math import pi, log10, exp
    a=1.85298
    b=0.86717
    c=-2.33706
    D=dbh_cm * 100
    H=height_m
    return (D**a*H**b*exp(c))/1000
    
def stem_vol_55(dbh_cm, height_m):
    from math import pi, log10, exp
    a=1.9577
    b=0.7706
    c=-2.48079
    D=dbh_cm * 100
    H=height_m
    return (D**a*H**b*exp(c))/1000
    
def stem_vol_67(dbh_cm, height_m):
    from math import pi, log10, exp
    a=1.86670
    b=1.08118
    c=-3.0488
    D=dbh_cm * 100
    H=height_m
    return (D**a*H**b*exp(c))/1000
    
def stem_vol_79(dbh_mm, height_m):
    from math import pi, log10, exp
    a=0.00035217
    b=2.12841828
    c=-0.1054168
    d=0.76283925
    D=dbh_mm * 1000
    H=height_m
    return (a*D**(b+c)*H**d)/1000
    
def stem_vol_91(dbh_cm, height_m):
    from math import pi, log10, exp
    a=0.7877
    b=1.9302
    c=0.79465
    D=dbh_cm * 100
    H=height_m
    return (a*D**b*H**c)/1000
    
def stem_vol_103(dbh_cm, height_m):
    from math import pi, log10
    a=0.7464
    b=2.496
    c=2.0714
    d=-1.4175
    e=-0.9601
    D=dbh_cm * 100
    H=height_m
    return (a*H**b*D**c*(H-1.3)**d*(D+40)**e)/1000
    
def stem_vol_115(dbh_cm, height_m):
    from math import pi, log10
    a=0.53005
    b=1.229283
    D=dbh_cm * 100
    H=height_m
    return (pi/40000)*H*D*(a*D+b)
    
def stem_vol_127(dbh_cm, height_m):
    from math import pi, log10
    a=0.1870
    b=3.7077
    c=1.9854
    d=-2.2816
    e=-0.7161
    D=dbh_cm * 100
    H=height_m
    return (a*H**b*D**c*(H-1.3)**d*(D+40)**e)/1000
    
def stem_vol_139(dbh_cm, height_m):
    from math import pi, log10
    a=0.000074
    b=3.1
    D=dbh_cm * 100
    H=height_m
    return a*H**b
    
def stem_vol_151(dbh_cm, height_m):
    from math import pi, log10
    a=0.0942
    b=1.9671
    c=0.7005
    D=dbh_cm * 100
    H=height_m
    return (a*D**b*H**c)/1000
    
def stem_vol_163(dbh_cm, height_m):
    from math import pi, log10
    a=0.4434
    b=4.9667
    c=1.9912
    d=-3.6612
    e=-0.7502
    D=dbh_cm * 100
    H=height_m
    return (a*H**b*D**c*(H-1.3)**d*(D+100)**e)/1000
    
def stem_vol_175(dbh_cm, height_m):
    from math import pi, log10
    a=-1.52761
    b=1.82928
    c=0.07454
    d=1.43792
    e=-0.35559
    D=dbh_cm * 100
    H=height_m
    return (10**a*D**b*(D+20)**c*H**d*(H-1.3)**e)/1000
    
def stem_vol_187(dbh_cm, height_m):
    from math import pi, log10
    a=0.00007604
    b=1.7812
    c=0.0528
    d=0.8533
    e=0.0654
    D=dbh_cm * 100
    H=height_m
    return a*10**(b*log10(D)+c*log10(D)**2+d*log10(H)+e*log10(H)**2)
    
def stem_vol_199(dbh_mm, height_m):
    from math import pi, log10
    a=0.00095916
    b=2.092560524
    c=0
    d=0.48824344
    D=dbh_mm * 1000
    H=height_m
    return (a*D**(b+c)*H**d)/1000
    
def stem_vol_211(dbh_dm, height_dm):
    from math import pi, log
    a=0.417118
    b=0.21941
    c=13.32594
    D=dbh_dm * 10
    H=height_dm * 10
    return ((pi/4)*(a*D**2*H+b*D**2*H*log(D)**2+c*D**2))/1000
    
def stem_vol_223(dbh_cm, height_m):
    from math import pi, exp
    a=1.67887
    b=1.11243
    c=-2.64821
    D=dbh_cm * 100
    H=height_m
    return (D**a*H**b*exp(c))/1000
    

def stem_vol_10(D, H):
    a = 1.89756
    b = 0.97716
    c = -2.94253

    V = D ** a * H ** b * math.exp(c)
    
    return V / 1000

def stem_vol_22(D, H):
    a = 0.387399
    b = 7.17123
    c = 0.04407

    V = (math.pi / 4) * (a * D**2 * H + b * D**2 + c * D)
    
    return V / 1000

def stem_vol_34(D, H):
    a = -0.89359
    b = 2.27954
    c = -1.18672
    d = 7.07362
    e = -5.45175

    V = 10**a * D**b * (D + 20)**c * H**d * (H - 1.3)**e
    
    return V / 1000

def stem_vol_46(D, H):
    a = 0.5173
    b = -13.62144
    c = 9.9888

    V = (math.pi / 4) * (a * D**2 * H + b * D**2 + c * D)
    
    return V / 1000

def stem_vol_58(D, H):
    a = 0.06328
    b = 1.92428
    c = 0.8869

    V = a * D**b * H**c
    
    return V / 1000

def stem_vol_70(D, H):
    a = 1.87077
    b = 1.00616
    c = -2.8748

    V = D ** a * H ** b * math.exp(c)
    
    return V / 1000

def stem_vol_82(D, H):
    a = 0.46818
    b = -0.013919
    c = -28.213
    d = 0.37474
    e = -0.28875
    f = 28.279

    V = (math.pi / 4) * (a * D**2 * H + b * D**2 * H * math.log(D)**2 + c * D**2 + d * D * H + e * H + f * D)
    
    return V / 1000

def stem_vol_94(D, H):
    a = 0.502

    V = a * H * D**2
    
    return V

def stem_vol_106(D, H):
    a = -31.57
    b = 0.0016
    c = 0.0186
    d = 0.63
    e = -2.34
    f = 3.2

    V = a + b * D * H**2 + c * H**2 + d * D * H + e * H + f * D
    
    return V / 1000

def stem_vol_118(D, H):
    a = -0.79784
    b = 2.07157
    c = -0.73883
    d = 3.16332
    e = -1.82623

    V = 10**a * D**b * (D + 20)**c * H**d * (H - 1.3)**e
    
    return V / 1000

def stem_vol_130(D, H):
    a = 0.0739
    b = 1.7508
    c = 1.0228

    V = a * D**b * H**c
    
    return V / 1000

def stem_vol_142(D, H):
    a = 0.00042613
    b = 2.066225947
    c = -0.07956244
    d = 0.80636901

    V = a * D**(b + c) * H**d
    
    return V

def stem_vol_154(D, H):
    a = -2.37912
    b = 2.62903
    c = -0.000126

    V = a + b * math.log(D) + c * D**2
    
    return V

def stem_vol_166(D, H):
    a = 2.0044
    b = 0.029886
    c = 0.036972
    d = 0.004341

    V = a + b * D**2 + c * D**2 * H
    
    return V / 1000

def stem_vol_178(D, H):
    a = 0.366419
    b = 1.13323
    c = 0.1306

    V = (math.pi / 4) * (a * D**2 * H + b * D**2 + c * D)
    
    return V / 1000

def stem_vol_190(D, H):
    a = 0.03392
    b = -0.01491
    c = -0.000005
    d = 0.01704
    e = 0.002926

    V = a * D**2 * H + b * D**2 * H + c * D**2 * H**2 + d * D * H + e * D * H**2
    
    return V / 1000

def stem_vol_202(D, H):
    a = 0.000096
    b = 1.821
    c = 0.759

    V = a * D**b * H**c
    
    return V

def stem_vol_214(D, H):
    a = 0.00095853
    b = 2.040672356
    c = -0.02101921
    d = 0.56366437

    V = a * D**(b + c) * H**d
    
    return V

def stem_vol_226(D, H):
    a = 1.76755
    b = 1.37219
    c = -3.54922

    V = D ** a * H ** b * math.exp(c)
    
    return V / 1000

def stem_vol_5(dbh_m, height_m):
    from math import pi, log
    a=0.580223
    b=-0.0307373
    c=-17.1507
    d=0.089869
    e=-0.080557
    f=19.661
    g=-2.4584
    D=dbh_m*10
    H=height_m*10
    return ((pi/4)*(a*D**2*H+b*D**2*H*log(D)**2+c*D**2+d*D*H+e*H+f*D+g))/1000

def stem_vol_17(dbh_m, height_m):
    from math import pi, log
    a=0.1926
    b=0.01631
    c=0.003755
    d=-0.02756
    e=0.000499
    D=dbh_m*100
    H=height_m
    return (a*D**2+b*D**2*H+c*D*H**2+d*D*H+e*D**2*H**2)/1000

def stem_vol_29(dbh_m, height_m):
    from math import pi, log
    a=-4.4759
    b=2.0851
    c=4.0691
    d=-2.7375
    e=-0.013311
    D=dbh_m*100
    H=height_m
    return (a+b*log(D)+c*log(H)+d*log(H-1.3)+e*D)/1000

def stem_vol_41(dbh_m, height_m):
    from math import pi, log
    a=0.00021491
    b=2.258957614
    c=-0.01120638
    d=0.60291075
    D=dbh_m*1000
    H=height_m
    return (a*D**(b+c)*H**d)/1000

def stem_vol_53(dbh_m, height_m):
    from math import pi, log
    a=0.049
    b=1.78189
    c=1.08345
    D=dbh_m*100
    H=height_m
    return (a*D**b*H**c)/1000

def stem_vol_65(dbh_m, height_m):
    from math import pi, log
    a=0.487270
    b=-2.04291
    c=5.<<9995
    D=dbh_m*10
    H=height_m*10
    return ((pi/4)*(a*D**2*H+b*D**2+c*D))/1000
    
