# -*- coding: utf-8 -*-
"""
Created on Wed May 12 15:04:18 2021

@author: ferre
"""

#import random


def main():
 #   f0 = open("declara_w.txt", "w+")
 #   for i in range(48):
 #       f0.write("print(\"x_" + str(i) + " = \", x_"+ str(i) + ")"'\n')
 #   f0.close()
    
    mat = open("H1calc.txt", "w+")
    mat.write("i = 0;" '\n')
    mat.write("while(i<=96){" '\n')
    for a in range(97):
        mat.write("    H_" + str(a) + "[i] = H_" + str(a) + "[i] + J[i]*J[" + str(a) + "]/N;" '\n' )
    mat.write("i = i+1;")
    mat.close()
    
    
    
    mat = open("H1calc.txt", "w+")
    mat.write("i = 0;" '\n')
    mat.write("while(i<=96){" '\n')
    for a in range(97):
        mat.write("    H_" + str(a) + "[i] = 0;" '\n' )
    mat.write("    i++;" '\n')
    mat.write("}")
    mat.close()
    
    
    
    
    mat = open("iddecla.txt", "w+")
    mat.write("while i<=96:")
    for a in range(97):       
        mat.write("    id" + str(a) + "=  np.array(np.zeros(97)).astype(np.float);" '\n' )
    mat.write("i+=1;")
    mat.close()
    
    
    
    
    py = open("iden.txt", "w+")
    for i in range(97):
        py.write("float iden_" + str(i) + "[97];"  '\n')
    py.close()
    
    py = open("inter0e1.txt", "w+")
    for i in range(97):
        py.write("inter0" + str(i) + "[97];"  '\n')
    py.close()
    
    py = open("iden.txt", "w+")
    for i in range(97):
        py.write("iden_" + str(i) + "["+str(i)+"]=1;"  '\n')
    py.close()
    
    
    py = open("soma.txt", "w+")
    for i in range(97):
        py.write("float soma_" + str(i) +"[97];"  '\n')
    py.close()
    
    
    py = open("somaop.txt", "w+")
    py.write("while(i<=96){" '\n')
    for i in range(97):
        py.write("    soma_" + str(i) + "[i] = H_" + str(i) + "[i]+ M_" + str(i) + "[i];"  '\n')
    py.write("    i++;" '\n')
    py.write("}")
    py.close()
    
    py = open("inv.txt", "w+")
    for i in range(97):
        py.write("inve_" + str(i) + "=inv(soma_" + str(i) + ");" '\n')
    py.close()
    
    py = open("Mmult.txt", "w+")
    for i in range(97):
        py.write("M_" + str(i) + "[" + str(i) + "] = iden_" + str(i) + "[" + str(i) + "]*mi;"  '\n')
    py.close()
    
    
    
    py = open("varaux.txt", "w+")
    py.write("while i<=96:")
    for i in range(97):
        py.write("    variavelauxiliar_" + str(i) + "[i] = id" + str(i) + "[i];"  '\n')
    py.close()
    
    
    
    py = open("gxinv.txt", "w+")
    py.write("while i<=96:" '\n')
    for a in range (97):
        py.write("    auxiliar["+str(a)+"] = ")
        for i in range(97):
            py.write("g["+str(i)+"]*id" + str(i) + "[" + str(a) + "] "  )
            if i <96:
                py.write("+")
            else:
                py.write(";")
        py.write('\n' '\n' '\n')
        
    py.write("i+=1;")
    py.close()
    
    
    
    
    #teste
    dab = open("W_1.txt", "w+")
    arquivo = open("W1.txt", "r")
    cont = 0
    for i in arquivo:
            dab.write("W1_0"  + "[" + str(cont) + "] = " + str(i.split()) + ";" '\n' )
            cont=1+cont
    arquivo.close()
    dab.close()

    dab = open("W_2.txt", "w+")
    arquivo = open("W2.txt", "r")
    cont = 0
    for i in arquivo:
            dab.write("W1_1"  + "[" + str(cont) + "] = " + str(i.split()) + ";" '\n' )
            cont=1+cont
    arquivo.close()
    dab.close()

    dab = open("W_3.txt", "w+")
    arquivo = open("W3.txt", "r")
    cont = 0
    for i in arquivo:
            dab.write("W1_2" + "[" + str(cont) + "] = " + str(i.split()) + ";" '\n' )
            cont=1+cont
    arquivo.close()
    dab.close()

    dab = open("W_4.txt", "w+")
    arquivo = open("W4.txt", "r")
    cont = 0
    for i in arquivo:
            dab.write("W1_4"  + "[" + str(cont) + "] = " + str(i.split()) + ";" '\n' )
            cont=1+cont
    arquivo.close()
    dab.close()
    
    dab = open("W_5.txt", "w+")
    arquivo = open("W5.txt", "r")
    cont = 0
    for i in arquivo:
            dab.write("W1_5"  + "[" + str(cont) + "] = " + str(i.split()) + ";" '\n' )
            cont=1+cont
    arquivo.close()
    dab.close()

    dab = open("W_6.txt", "w+")
    arquivo = open("W6.txt", "r")
    cont = 0
    for i in arquivo:
            dab.write("W1_6"  + "[" + str(cont) + "] = " + str(i.split()) + ";" '\n' )
            cont=1+cont
    arquivo.close()
    dab.close()

    dab = open("W_7.txt", "w+")
    arquivo = open("W7.txt", "r")
    cont = 0
    for i in arquivo:
            dab.write("W1_7"  + "[" + str(cont) + "] = " + str(i.split()) + ";" '\n' )
            cont=1+cont
    arquivo.close()
    dab.close()

    dab = open("W_8.txt", "w+")
    arquivo = open("W8.txt", "r")
    cont = 0
    for i in arquivo:
            dab.write("W1_8"  + "[" + str(cont) + "] = " + str(i.split()) + ";" '\n' )
            cont=1+cont
    arquivo.close()
    dab.close()
    
    
    #fim do teste
    dab = open("X.txt", "w+")
    arquivo = open("x.txt", "r")
    cont = 0;
    for i in arquivo:
        dab.write("x[" + str(cont) + "] = " + str(i) + ";" '\n')
        cont = cont + 1
    arquivo.close()
    dab.close()
    
    #teste
    dab = open("W_1a.txt", "w+")
    
    for i in range(97):
        dab.write("W1_0"  + "[]"'\n' )
    dab.close()

    dab = open("W_2a.txt", "w+")
    arquivo = open("W2.txt", "r")
    cont = 0
    for i in arquivo:
            dab.write("W1_1"  + "[" + str(cont) + "] = " + str(i.split()) + ";" '\n' )
            cont=1+cont
    arquivo.close()
    dab.close()

    dab = open("W_3a.txt", "w+")
    arquivo = open("W3.txt", "r")
    cont = 0
    for i in arquivo:
            dab.write("W1_2" + "[" + str(cont) + "] = " + str(i.split()) + ";" '\n' )
            cont=1+cont
    arquivo.close()
    dab.close()

    dab = open("W_4a.txt", "w+")
    arquivo = open("W4.txt", "r")
    cont = 0
    for i in arquivo:
            dab.write("W1_4"  + "[" + str(cont) + "] = " + str(i.split()) + ";" '\n' )
            cont=1+cont
    arquivo.close()
    dab.close()
    
    dab = open("W_5a.txt", "w+")
    arquivo = open("W5.txt", "r")
    cont = 0
    for i in arquivo:
            dab.write("W1_5"  + "[" + str(cont) + "] = " + str(i.split()) + ";" '\n' )
            cont=1+cont
    arquivo.close()
    dab.close()

    dab = open("W_6a.txt", "w+")
    arquivo = open("W6.txt", "r")
    cont = 0
    for i in arquivo:
            dab.write("W1_6"  + "[" + str(cont) + "] = " + str(i.split()) + ";" '\n' )
            cont=1+cont
    arquivo.close()
    dab.close()

    dab = open("W_7a.txt", "w+")
    arquivo = open("W7.txt", "r")
    cont = 0
    for i in arquivo:
            dab.write("W1_7"  + "[" + str(cont) + "] = " + str(i.split()) + ";" '\n' )
            cont=1+cont
    arquivo.close()
    dab.close()

    dab = open("W_8a.txt", "w+")
    arquivo = open("W8.txt", "r")
    cont = 0
    for i in arquivo:
            dab.write("W1_8"  + "[" + str(cont) + "] = " + str(i.split()) + ";" '\n' )
            cont=1+cont
    arquivo.close()
    dab.close()
    
    
    dab = open("somamatriz.txt", "w+")
    dab.write("while(i<=96):" '\n')
    for i in range(97):           
        dab.write("soma[" + str(i) + "][i]=soma_" + str(i) + "[i]" '\n')
    dab.write("i= i +1")
    dab.close()
    
    let = open("xentr.txt", "w+")
    dab = open("sinEntradax.txt", "r")
    let.write("w = [np.zeros(10000)];")
    cont = 0;
    for i in dab:
        let.write("x["+str(cont)+"] = " + str(i.split()) + ";" '\n')
        cont+=1;
    dab.close()
    let.close()
    
    let = open("tentr.txt", "w+")
    dab = open("sinalt.txt", "r")
    let.write("t = [np.zeros(10000)];")
    cont = 0;
    for i in dab:
        let.write("t["+str(cont)+"] = " + str(i.split()) + ";" '\n')
        cont+=1;
    dab.close()
    let.close()
    

   # f1 = open("vetor_x.txt", "w+")
   # for i in range(48):
   #     f1.write("x[" + str(i) + "] = " + str(random.randint(0, 100)) + ";" '\n')
   # f1.close()

   # f2 = open("matriz_w.txt", "w+")
   # for i in range(48):
    #    for j in range(48):
   #         f2.write("h" + str(i) + "[" + str(j) + "] = " + str(random.randint(0, 100)) + ";" '\n')
   # f2.close()

#    f3 = open("declara_y.txt", "w+")
#    for i in range(48):
#        f3.write("mi" + str(i) + "[i] = mi*w" + str(i) + "[i];"'\n')
#    f3.close()

#    f4 = open("gera_loop.txt", "w+")
#    for i in range(48):
#        f4.write("miwd[" + str(i) + "] = miwd[" + str(i) + "] + miw" + str(i) + "[i]*d[i];" '\n')
#    f4.close()

 #   f5 = open("vetor_d.txt", "w+")
  #  for i in range(48):
  #      f5.write("d[" + str(i) + "] = " + str(random.randint(0, 100)) + ";" '\n')
  #  f5.close()

#    f6 = open("vetor_x_novo.txt", "w+")
#    for i in range(48):
#        f6.write("aux[" + str(i) + "] = aux[" + str(i) + "] + x[i]*h" + str(i) + "[i];" '\n')
#    f6.close()#

#    f7 = open("matriz_miw.txt", "w+")
#    for i in range(48):
#        f7.write("LOAD mainaux_" + str(i) + "'\n'")
#        f7.write("PSET mainx_" + str(i))
#    f7.close()

#    f8 = open("que.txt", "w+")
#    for i in range(48):
#        f8.write("LOAD mainaux_" + str(i) + '\n' + "PSET mainx_" + str(i) + '\n')
#    f8.close()

#    f9 = open("multicore.txt", "w+")
#    for i in range(146):
#        f9.write(str(i) + ": begin rst"+ str(i) +" <= 0; if (cnt <= 32'd210) cnt=cnt+32'd1; else begin q <= q+32'd1; cnt=0; end	end"+ '\n')
#    f9.close()
  
arquivo = open("saida2.txt", "a", newline="")
persons = ['-0.522819','-0.576786','-0.578795','-0.579203','-0.579601','-0.579926','-0.580317','-0.580696','-0.581093','-0.581463','-0.581839','-0.582218','-0.582588','-0.582965','-0.583331','-0.583711','-0.584081','-0.584451','-0.584823','-0.585204','-0.585577','-0.585947','-0.586318','-0.586690','-0.587059','-0.587431','-0.587808','-0.588175','-0.588551','-0.588926','-0.589296','-0.589646','-0.590014','-0.590387','-0.590743','-0.591177','-0.591539','-0.591900','-0.592266','-0.592655','-0.593023','-0.593377','-0.593750','-0.594125','-0.594487','-0.594867','-0.595222','-0.595588','-0.595964','-0.596356','-0.596718','-0.597096','-0.597458','-0.597824','-0.598184','-0.598537','-0.598913','-0.599289','-0.599682','-0.600062','-0.600427','-0.600777','-0.601152','-0.601511','-0.601869','-0.602221','-0.602603','-0.603000','-0.603374','-0.603742','-0.604104','-0.604458','-0.604815','-0.605188','-0.605554','-0.605935','-0.606312','-0.606669','-0.607029','-0.607383','-0.607753','-0.608130','-0.608496','-0.608874','-0.609244','-0.609600','-0.609963','-0.610325','-0.610682','-0.611046','-0.611423','-0.611802','-0.612173','-0.612536','-0.612887','-0.613252','-0.613615','-0.613974','-0.614341','-0.614721','-0.615083','-0.615440','-0.615800','-0.616164','-0.616528','-0.616896','-0.617267','-0.617633','-0.618005','-0.618353','-0.618719','-0.619077','-0.619436','-0.619811','-0.620180','-0.620552','-0.620912','-0.621273','-0.621629','-0.621987','-0.622343','-0.622715','-0.623077','-0.623447','-0.623816','-0.624170','-0.624531','-0.624889','-0.625253','-0.625621','-0.625982','-0.626351','-0.626714','-0.627069','-0.627427','-0.627785','-0.628148','-0.628502','-0.628863','-0.629232','-0.629597','-0.629958','-0.630325','-0.630683','-0.631033','-0.631389','-0.631752','-0.632111','-0.632464','-0.632824','-0.633192','-0.633547','-0.633909','-0.634273','-0.634633','-0.634998','-0.635352','-0.635703','-0.636061','-0.636419','-0.636777','-0.637135','-0.637495','-0.637860','-0.638221','-0.638575','-0.638933','-0.639293','-0.639647','-0.640006','-0.640359','-0.640718','-0.641076','-0.641428','-0.641787','-0.642150','-0.642513','-0.642871','-0.643236','-0.643596','-0.643956','-0.644314','-0.644676','-0.645029','-0.645393','-0.645746','-0.646107','-0.646469','-0.646826','-0.647184','-0.647534','-0.647899','-0.648256','-0.648613','-0.648970','-0.649324','-0.649687','-0.650042','-0.650396','-0.650746','-0.651101','-0.651456','-0.651812','-0.652168','-0.652517','-0.652864','-0.653220','-0.653571','-0.653930','-0.654280','-0.654631','-0.654983','-0.655334','-0.655691','-0.656038','-0.656393','-0.656737','-0.657096','-0.657442','-0.657799','-0.658151','-0.658502','-0.658853','-0.659204','-0.659560','-0.659916','-0.660261','-0.660611','-0.660966','-0.661318','-0.661670','-0.662021','-0.662368','-0.662727','-0.663075','-0.663423','-0.663773','-0.664123','-0.664477','-0.664831','-0.665180','-0.665528','-0.665881','-0.666224','-0.666571','-0.666923','-0.667266','-0.667624','-0.667964','-0.668315','-0.668662','-0.669014','-0.669355','-0.669704','-0.670049','-0.670391','-0.670747','-0.671087','-0.671437','-0.671774','-0.672124','-0.672465','-0.672818','-0.673159','-0.673508','-0.673853','-0.674205','-0.674542','-0.674891','-0.675235','-0.675582','-0.675920','-0.676274','-0.676606','-0.676959','-0.677293','-0.677645','-0.677987','-0.678326','-0.678668','-0.679021','-0.679360','-0.679704','-0.680044','-0.680381','-0.680713','-0.681061','-0.681403','-0.681748','-0.682088','-0.682433','-0.682773','-0.683116','-0.683460','-0.683810','-0.684160','-0.684501','-0.684846','-0.685187','-0.685530','-0.685874','-0.686209','-0.686547','-0.686886','-0.687227','-0.687568','-0.687916','-0.688258','-0.688595','-0.688939','-0.689288','-0.689632','-0.689959','-0.690323','-0.690660','-0.690997','-0.691334','-0.691664','-0.691992','-0.692324','-0.692668','-0.693007','-0.693352','-0.693696','-0.694030','-0.694375','-0.694703','-0.695061','-0.695398','-0.695733','-0.696059','-0.696394','-0.696725','-0.697063','-0.697405','-0.697742','-0.698078','-0.698418','-0.698754','-0.699096','-0.699447','-0.699777','-0.700116','-0.700460','-0.700794','-0.701122','-0.701455','-0.701792','-0.702133','-0.702469','-0.702810','-0.703145','-0.703484','-0.703820','-0.704160','-0.704490','-0.704821','-0.705141','-0.705479','-0.705800','-0.706138','-0.706473','-0.706812','-0.707146','-0.707484','-0.707816','-0.708151','-0.708491','-0.708833','-0.709165','-0.709491','-0.709808','-0.710142','-0.710484','-0.710812','-0.711145','-0.711483','-0.711820','-0.712160','-0.712492','-0.712814','-0.713156','-0.713491','-0.713814','-0.714133','-0.714470','-0.714802','-0.715130','-0.715465','-0.715793','-0.716120','-0.716448','-0.716785','-0.717122','-0.717446','-0.717770','-0.718093','-0.718414','-0.718741','-0.719073','-0.719401','-0.719725','-0.720059','-0.720400','-0.720733','-0.721057','-0.721387','-0.721717','-0.722051','-0.722381','-0.722695','-0.723013','-0.723346','-0.723672','-0.723997','-0.724332','-0.724663','-0.724991','-0.725328','-0.725649','-0.725971','-0.726304','-0.726627','-0.726954','-0.727267','-0.727586','-0.727910','-0.728242','-0.728570','-0.728904','-0.729226','-0.729546','-0.729867','-0.730185','-0.730513','-0.730837','-0.731156','-0.731478','-0.731802','-0.732117','-0.732427','-0.732755','-0.733076','-0.733397','-0.733724','-0.734043','-0.734368','-0.734690','-0.735009','-0.735330','-0.735651','-0.735972','-0.736295','-0.736621','-0.736943','-0.737251','-0.737551','-0.737872','-0.738198','-0.738515','-0.738840','-0.739151','-0.739476','-0.739800','-0.740117','-0.740439','-0.740769','-0.741084','-0.741406','-0.741725','-0.742040','-0.742357','-0.742675','-0.742996','-0.743297','-0.743608','-0.743928','-0.744247','-0.744568','-0.744902','-0.745226','-0.745540','-0.745856','-0.746171','-0.746479','-0.746802','-0.747118','-0.747441','-0.747752','-0.748074','-0.748386','-0.748696','-0.749023','-0.749345','-0.749658','-0.749978','-0.750277','-0.750576','-0.750888','-0.751198','-0.751521','-0.751832','-0.752155','-0.752466','-0.752779','-0.753089','-0.753404','-0.753721','-0.754037','-0.754346','-0.754666','-0.754983','-0.755296','-0.755610','-0.755924','-0.756240','-0.756555','-0.756866','-0.757174','-0.757490','-0.757802','-0.758106','-0.758416','-0.758731','-0.759040','-0.759349','-0.759663','-0.759971','-0.760280','-0.760577','-0.760872','-0.761183','-0.761499','-0.761808','-0.762114','-0.762416','-0.762728','-0.763030','-0.763354','-0.763667','-0.763976','-0.764285','-0.764595','-0.764902','-0.765213','-0.765515','-0.765821','-0.766132','-0.766434','-0.766744','-0.767047','-0.767359','-0.767661','-0.767966','-0.768276','-0.768584','-0.768889','-0.769194','-0.769499','-0.769805','-0.770112','-0.770414','-0.770719','-0.771023','-0.771326','-0.771631','-0.771928','-0.772233','-0.772537','-0.772836','-0.773142','-0.773444','-0.773742','-0.774050','-0.774348','-0.774652','-0.774951','-0.775257','-0.775560','-0.775860','-0.776164','-0.776468','-0.776776','-0.777075','-0.777376','-0.777679','-0.777971','-0.778279','-0.778581','-0.778877','-0.779183','-0.779482','-0.779779','-0.780086','-0.780376','-0.780683','-0.780982','-0.781280','-0.781583','-0.781878','-0.782174','-0.782471','-0.782769','-0.783066','-0.783365','-0.783662','-0.783957','-0.784255','-0.784555','-0.784848','-0.785147','-0.785436','-0.785735','-0.786033','-0.786330','-0.786623','-0.786912','-0.787203','-0.787503','-0.787796','-0.788092','-0.788392','-0.788683','-0.788977','-0.789280','-0.789589','-0.789882','-0.790175','-0.790472','-0.790765','-0.791062','-0.791356','-0.791648','-0.791946','-0.792243','-0.792531','-0.792828','-0.793119','-0.793406','-0.793696','-0.793992','-0.794278','-0.794572','-0.794861','-0.795150','-0.795440','-0.795733','-0.796021','-0.796308','-0.796590','-0.796877','-0.797169','-0.797462','-0.797749','-0.798045','-0.798327','-0.798620','-0.798910','-0.799204','-0.799489','-0.799777','-0.800062','-0.800351','-0.800639','-0.800940','-0.801235','-0.801528','-0.801815','-0.802100','-0.802383','-0.802674','-0.802953','-0.803242','-0.803533','-0.803809','-0.804088','-0.804376','-0.804655','-0.804940','-0.805230','-0.805511','-0.805800','-0.806084','-0.806368','-0.806654','-0.806942','-0.807231','-0.807524','-0.807805','-0.808089','-0.808370','-0.808644','-0.808930','-0.809214','-0.809505','-0.809794','-0.810070','-0.810350','-0.810626','-0.810917','-0.811190','-0.811476','-0.811754','-0.812035','-0.812316','-0.812597','-0.812879','-0.813159','-0.813440','-0.813723','-0.814005','-0.814285','-0.814563','-0.814841','-0.815118','-0.815391','-0.815660','-0.815925','-0.816208','-0.816485','-0.816770','-0.817056','-0.817345','-0.817622','-0.817903','-0.818172','-0.818454','-0.818729','-0.819007','-0.819287','-0.819565','-0.819840','-0.820111','-0.820393','-0.820677','-0.820955','-0.821232','-0.821508','-0.821782','-0.822050','-0.822321','-0.822593','-0.822867','-0.823145','-0.823419','-0.823693','-0.823962','-0.824246','-0.824510','-0.824790','-0.825057','-0.825334','-0.825609','-0.825880','-0.826152','-0.826425','-0.826691','-0.826959','-0.827221','-0.827491','-0.827767','-0.828039','-0.828306','-0.828578','-0.828842','-0.829118','-0.829385','-0.829660','-0.829926','-0.830200','-0.830467','-0.830740','-0.831009','-0.831290','-0.831553','-0.831835','-0.832100','-0.832370','-0.832640','-0.832907','-0.833174','-0.833440','-0.833702','-0.833966','-0.834229','-0.834495','-0.834765','-0.835026','-0.835294','-0.835562','-0.835830','-0.836093','-0.836362','-0.836628','-0.836889','-0.837156','-0.837421','-0.837682','-0.837947','-0.838215','-0.838475','-0.838742','-0.839006','-0.839269','-0.839535','-0.839801','-0.840062','-0.840325','-0.840580','-0.840846','-0.841106','-0.841369','-0.841628','-0.841889','-0.842147','-0.842409','-0.842671','-0.842928','-0.843193','-0.843448','-0.843713','-0.843969','-0.844233','-0.844499','-0.844763','-0.845022','-0.845284','-0.845537','-0.845800','-0.846056','-0.846315','-0.846577','-0.846834','-0.847094','-0.847345','-0.847604','-0.847862','-0.848113','-0.848367','-0.848623','-0.848882','-0.849130','-0.849396','-0.849644','-0.849908','-0.850161','-0.850411','-0.850673','-0.850927','-0.851186','-0.851435','-0.851696','-0.851951','-0.852208','-0.852462','-0.852715','-0.852975','-0.853223','-0.853487','-0.853727','-0.853986','-0.854237','-0.854491','-0.854743','-0.854998','-0.855245','-0.855494','-0.855753','-0.855995','-0.856256','-0.856497','-0.856753','-0.857004','-0.857256','-0.857505','-0.857759','-0.858006','-0.858255','-0.858497','-0.858746','-0.858990','-0.859237','-0.859477','-0.859721','-0.859963','-0.860208','-0.860459','-0.860710','-0.860959','-0.861202','-0.861454','-0.861707','-0.861957','-0.862200','-0.862456','-0.862704','-0.862951','-0.863195','-0.863439','-0.863682','-0.863931','-0.864176','-0.864422','-0.864668','-0.864914','-0.865162','-0.865405','-0.865647','-0.865894','-0.866136','-0.866382','-0.866624','-0.866864','-0.867107','-0.867350','-0.867594','-0.867837','-0.868081','-0.868322','-0.868572','-0.868822','-0.869060','-0.869303','-0.869543','-0.869783','-0.870025','-0.870259','-0.870497','-0.870738','-0.870981','-0.871213','-0.871450','-0.871685','-0.871924','-0.872159','-0.872400','-0.872637','-0.872870','-0.873111','-0.873347','-0.873585','-0.873823','-0.874056','-0.874291','-0.874529','-0.874765','-0.875003','-0.875235','-0.875475','-0.875701','-0.875942','-0.876179','-0.876414','-0.876643','-0.876878','-0.877114','-0.877350','-0.877588','-0.877818','-0.878055','-0.878287','-0.878521','-0.878754','-0.878989','-0.879223','-0.879465','-0.879690','-0.879923','-0.880154','-0.880385','-0.880614','-0.880850','-0.881075','-0.881310','-0.881539','-0.881770','-0.882000','-0.882232','-0.882462','-0.882696','-0.882937','-0.883166','-0.883393','-0.883624','-0.883853','-0.884080','-0.884313','-0.884533','-0.884761','-0.884985']

for p in persons:
    arquivo.write(p+'\n')
arquivo.close()
  
  
  
  
  
dab = open("micro.txt", "w+")
cont = 0
for i in range(16):
            a=2**cont
            dab.write("if(k=="+str(a)+"){\n")
            dab.write("    printf(\"\\r\\nTecla " + str(cont+1) +"\\r\\n\");\n}\n")
            cont=1+cont
dab.close()

if __name__ == "__main__":
    main()