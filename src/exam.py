import stem_volume
#from stem_volume import stem_vol_6
from stem_volume import *
import pandas as pd
import numpy as np

input_df = pd.read_csv('./data/tree_sampled_data.csv')
from mapping import species_mapping
metadata = pd.read_csv('./data/form_metadata.csv',sep= ';')


def expand_dataframe(input_df):
    # Create a new DataFrame with additional columns starting from column 5
        # Define the dimensions of the DataFrame

    rows = 102

    cols = 234


    

    output_df = pd.DataFrame(np.nan, index=range(rows), columns=[f"F{i}" for i in range(1, cols+1)])


    output_df = input_df.copy()  # Copy input DataFrame to retain original columns and rows
    
    
    
    
    for formula_number in range(1, 231):
        form_meta =metadata[ metadata[ 'FormNum' ] == formula_number ]
        volumes = []
        
        
        for _, row in output_df.iterrows():
            dbh = row['diameter at breast height [mm]'] / 1000
            height = row['height [dm]'] / 10 
            species= row['species']
            sp = species_mapping[ species ]
           
            
   
        
        
        #print (formula_number, form_meta['Species'].iloc[0],sp)
            if form_meta['Species'].iloc[0] == sp:

                
                    if formula_number ==1:
                            volume = stem_vol_1(dbh,height)
                    elif formula_number ==2:
                            volume = stem_vol_2(dbh,height)
                    elif formula_number ==3:
                            volume = stem_vol_3(dbh,height)
                    elif formula_number ==4:
                            volume = stem_vol_4(dbh,height)
                    elif formula_number ==5:
                            volume = stem_vol_5(dbh,height)
                    elif formula_number ==6:
                            volume = stem_vol_6(dbh,height)
                    elif formula_number ==7:
                            volume = stem_vol_7(dbh,height)
                    elif formula_number ==8:
                            volume = stem_vol_8(dbh,height)
                    elif formula_number ==9:
                            volume = stem_vol_9(dbh,height)
                    elif formula_number ==10:
                            volume = stem_vol_10(dbh,height)
                    elif formula_number ==11:
                            volume = np.nan
                    elif formula_number ==12:
                            volume = stem_vol_12(dbh,height)
                    elif formula_number ==13:
                            volume = stem_vol_13(dbh,height)
                    elif formula_number ==14:
                            volume = stem_vol_14(dbh,height)
                    elif formula_number ==15:
                            volume = stem_vol_15(dbh,height)
                    elif formula_number ==16:
                            volume = stem_vol_16(dbh,height)
                    elif formula_number ==17:
                            volume = stem_vol_17(dbh,height)
                    elif formula_number ==18:
                            volume = stem_vol_18(dbh,height)
                    elif formula_number ==19:
                            volume = stem_vol_19(dbh,height)
                    elif formula_number ==20:
                            volume = stem_vol_20(dbh,height)
                    elif formula_number ==21:
                            volume = stem_vol_21(dbh,height)
                    elif formula_number ==22:
                            volume = stem_vol_22(dbh,height)
                    elif formula_number ==23:
                            volume = np.nan
                    elif formula_number ==24:
                            volume = stem_vol_24(dbh,height)
                    elif formula_number ==25:
                            volume = stem_vol_25(dbh,height)
                    elif formula_number ==26:
                            volume = stem_vol_26(dbh,height)
                    elif formula_number ==27:
                            volume = stem_vol_27(dbh,height)
                    elif formula_number ==28:
                            volume = stem_vol_28(dbh,height)
                    elif formula_number ==29:
                            volume = stem_vol_29(dbh,height)
                    elif formula_number ==30:
                            volume = stem_vol_30(dbh,height)
                    elif formula_number ==31:
                            volume = stem_vol_31(dbh,height)
                    elif formula_number ==32:
                            volume = stem_vol_32(dbh,height)
                    elif formula_number ==33:
                            volume = stem_vol_33(dbh,height)
                    elif formula_number ==34:
                            volume = stem_vol_34(dbh,height)
                    elif formula_number ==35:
                            volume = np.nan
                    elif formula_number ==36:
                            volume = stem_vol_36(dbh,height)
                    elif formula_number ==37:
                            volume = stem_vol_37(dbh,height)
                    elif formula_number ==38:
                            volume = stem_vol_38(dbh,height)
                    elif formula_number ==39:
                            volume = stem_vol_39(dbh,height)
                    elif formula_number ==40:
                            volume = stem_vol_40(dbh,height)
                    elif formula_number ==41:
                            volume = stem_vol_41(dbh,height)
                    elif formula_number ==42:
                            volume = stem_vol_42(dbh,height)
                    elif formula_number ==43:
                            volume = stem_vol_43(dbh,height)
                    elif formula_number ==44:
                            volume = stem_vol_44(dbh,height)
                    elif formula_number ==45:
                            volume = stem_vol_45(dbh,height)
                    elif formula_number ==46:
                            volume = stem_vol_46(dbh,height)
                    elif formula_number ==47:
                            volume = np.nan
                    elif formula_number ==48:
                            volume = stem_vol_48(dbh,height)
                    elif formula_number ==49:
                            volume = stem_vol_49(dbh,height)
                    elif formula_number ==50:
                            volume = stem_vol_50(dbh,height)
                    elif formula_number ==51:
                            volume = stem_vol_51(dbh,height)
                    elif formula_number ==52:
                            volume = stem_vol_52(dbh,height)
                    elif formula_number ==53:
                            volume = stem_vol_53(dbh,height)
                    elif formula_number ==54:
                            volume = stem_vol_54(dbh,height)
                    elif formula_number ==55:
                            volume = stem_vol_55(dbh,height)
                    elif formula_number ==56:
                            volume = stem_vol_56(dbh,height)
                    elif formula_number ==57:
                            volume = stem_vol_57(dbh,height)
                    elif formula_number ==58:
                            volume = stem_vol_58(dbh,height)
                    elif formula_number ==59:
                            volume = np.nan
                    elif formula_number ==60:
                            volume = stem_vol_60(dbh,height)
                    elif formula_number ==61:
                            volume = stem_vol_61(dbh,height)
                    elif formula_number ==62:
                            volume = stem_vol_62(dbh,height)
                    elif formula_number ==63:
                            volume = stem_vol_63(dbh,height)
                    elif formula_number ==64:
                            volume = stem_vol_64(dbh,height)
                    elif formula_number ==65:
                            volume = np.nan
                    elif formula_number ==66:
                            volume = stem_vol_66(dbh,height)
                    elif formula_number ==67:
                            volume = stem_vol_67(dbh,height)
                    elif formula_number ==68:
                            volume = stem_vol_68(dbh,height)
                    elif formula_number ==69:
                            volume = stem_vol_69(dbh,height)
                    elif formula_number ==70:
                            volume = stem_vol_70(dbh,height)
                    elif formula_number ==71:
                            volume = np.nan
                    elif formula_number ==72:
                            volume = stem_vol_72(dbh,height)
                    elif formula_number ==73:
                            volume = stem_vol_73(dbh,height)
                    elif formula_number ==74:
                            volume = stem_vol_74(dbh,height)
                    elif formula_number ==75:
                            volume = stem_vol_75(dbh,height)
                    elif formula_number ==76:
                            volume = stem_vol_76(dbh,height)
                    elif formula_number ==77:
                            volume = np.nan
                    elif formula_number ==78:
                            volume = stem_vol_78(dbh,height)
                    elif formula_number ==79:
                            volume = stem_vol_79(dbh,height)
                    elif formula_number ==80:
                            volume = stem_vol_80(dbh,height)
                    elif formula_number ==81:
                            volume = stem_vol_81(dbh,height)
                    elif formula_number ==82:
                            volume = stem_vol_82(dbh,height)
                    elif formula_number ==83:
                            volume = np.nan
                    elif formula_number ==84:
                            volume = stem_vol_84(dbh,height)
                    elif formula_number ==85:
                            volume = stem_vol_85(dbh,height)
                    elif formula_number ==86:
                            volume = stem_vol_86(dbh,height)
                    elif formula_number ==87:
                            volume = stem_vol_87(dbh,height)
                    elif formula_number ==88:
                            volume = stem_vol_88(dbh)
                    elif formula_number ==89:
                            volume = np.nan
                    elif formula_number ==90:
                            volume = stem_vol_90(dbh,height)
                    elif formula_number ==91:
                            volume = stem_vol_91(dbh,height)
                    elif formula_number ==92:
                            volume = stem_vol_92(dbh,height)
                    elif formula_number ==93:
                            volume = stem_vol_93(dbh,height)
                    elif formula_number ==94:
                            volume = stem_vol_94(dbh,height)
                    elif formula_number ==95:
                            volume = np.nan
                    elif formula_number ==96:
                            volume = stem_vol_96(dbh,height)
                    elif formula_number ==97:
                            volume = stem_vol_97(dbh,height)
                    elif formula_number ==98:
                            volume = stem_vol_98(dbh,height)
                    elif formula_number ==99:
                            volume = stem_vol_99(dbh,height)
                    elif formula_number ==100:
                            volume = stem_vol_100(dbh,height)
                    elif formula_number ==101:
                            volume = np.nan
                    elif formula_number ==102:
                            volume = stem_vol_102(dbh,height)
                    elif formula_number ==103:
                            volume = stem_vol_103(dbh,height)
                    elif formula_number ==104:
                            volume = stem_vol_104(dbh,height)
                    elif formula_number ==105:
                            volume = stem_vol_105(dbh,height)
                    elif formula_number ==106:
                            volume = stem_vol_106(dbh,height)
                    elif formula_number ==107:
                            volume = np.nan
                    elif formula_number ==108:
                            volume = stem_vol_108(dbh,height)
                    elif formula_number ==109:
                            volume = stem_vol_109(dbh,height)
                    elif formula_number ==110:
                            volume = stem_vol_110(dbh,height)
                    elif formula_number ==111:
                            volume = stem_vol_111(dbh,height)
                    elif formula_number ==112:
                            volume = stem_vol_112(dbh,height)
                    elif formula_number ==113:
                            volume = np.nan
                    elif formula_number ==114:
                            volume = stem_vol_114(dbh,height)
                    elif formula_number ==115:
                            volume = stem_vol_115(dbh,height)
                    elif formula_number ==116:
                            volume = stem_vol_116(dbh,height)
                    elif formula_number ==117:
                            volume = stem_vol_117(dbh,height)
                    elif formula_number ==118:
                            volume = stem_vol_118(dbh,height)
                    elif formula_number ==119:
                            volume = np.nan
                    elif formula_number ==120:
                            volume = stem_vol_120(dbh,height)
                    elif formula_number ==121:
                            volume = stem_vol_121(dbh,height)
                    elif formula_number ==122:
                            volume = stem_vol_122(dbh,height)
                    elif formula_number ==123:
                            volume = stem_vol_123(dbh,height)
                    elif formula_number ==124:
                            volume = stem_vol_124(dbh,height)
                    elif formula_number ==125:
                            volume = np.nan
                    elif formula_number ==126:
                            volume = stem_vol_126(dbh,height)
                    elif formula_number ==127:
                            volume = stem_vol_127(dbh,height)
                    elif formula_number ==128:
                            volume = stem_vol_128(dbh,height)
                    elif formula_number ==129:
                            volume = stem_vol_129(dbh,height)
                    elif formula_number ==130:
                            volume = stem_vol_130(dbh,height)
                    elif formula_number ==131:
                            volume = np.nan
                    elif formula_number ==132:
                            volume = stem_vol_132(dbh,height)
                    elif formula_number ==133:
                            volume = stem_vol_133(dbh,height)
                    elif formula_number ==134:
                            volume = stem_vol_134(dbh,height)
                    elif formula_number ==135:
                            volume = stem_vol_135(dbh,height)
                    elif formula_number ==136:
                            volume = stem_vol_136(dbh,height)
                    elif formula_number ==137:
                            volume = np.nan
                    elif formula_number ==138:
                            volume = stem_vol_138(dbh,height)
                    elif formula_number ==139:
                            volume = stem_vol_139(dbh,height)
                    elif formula_number ==140:
                            volume = stem_vol_140(dbh)
                    elif formula_number ==141:
                            volume = stem_vol_141(dbh,height)
                    elif formula_number ==142:
                            volume = stem_vol_142(dbh,height)
                    elif formula_number ==143:
                            volume = np.nan
                    elif formula_number ==144:
                            volume = stem_vol_144(dbh,height)
                    elif formula_number ==145:
                            volume = stem_vol_145(dbh,height)
                    elif formula_number ==146:
                            volume = stem_vol_146(dbh,height)
                    elif formula_number ==147:
                            volume = stem_vol_147(dbh,height)
                    elif formula_number ==148:
                            volume = stem_vol_148(dbh)
                    elif formula_number ==149:
                            volume = np.nan
                    elif formula_number ==150:
                            volume = stem_vol_150(dbh,height)
                    elif formula_number ==151:
                            volume = stem_vol_151(dbh,height)
                    elif formula_number ==152:
                            volume = stem_vol_152(dbh,height)
                    elif formula_number ==153:
                            volume = stem_vol_153(dbh,height)
                    elif formula_number ==154:
                            volume = stem_vol_154(dbh,height)
                    elif formula_number ==155:
                            volume = np.nan
                    elif formula_number ==156:
                            volume = stem_vol_156(dbh,height)
                    elif formula_number ==157:
                            volume = stem_vol_157(dbh,height)
                    elif formula_number ==158:
                            volume = stem_vol_158(dbh,height)
                    elif formula_number ==159:
                            volume = stem_vol_159(dbh,height)
                    elif formula_number ==160:
                            volume = stem_vol_160(dbh,height)
                    elif formula_number ==161:
                            volume = np.nan
                    elif formula_number ==162:
                            volume = stem_vol_162(dbh,height)
                    elif formula_number ==163:
                            volume = stem_vol_163(dbh,height)
                    elif formula_number ==164:
                            volume = stem_vol_164(dbh,height)
                    elif formula_number ==165:
                            volume = stem_vol_165(dbh,height)
                    elif formula_number ==166:
                            volume = stem_vol_166(dbh,height)
                    elif formula_number ==167:
                            volume = np.nan
                    elif formula_number ==168:
                            volume = stem_vol_168(dbh,height)
                    elif formula_number ==169:
                            volume = stem_vol_169(dbh,height)
                    elif formula_number ==170:
                            volume = stem_vol_170(dbh,height)
                    elif formula_number ==171:
                            volume = stem_vol_171(dbh,height)
                    elif formula_number ==172:
                            volume = stem_vol_172(dbh,height)
                    elif formula_number ==173:
                            volume = np.nan
                    elif formula_number ==174:
                            volume = stem_vol_174(dbh,height)
                    elif formula_number ==175:
                            volume = stem_vol_175(dbh,height)
                    elif formula_number ==176:
                            volume = stem_vol_176(dbh,height)
                    elif formula_number ==177:
                            volume = stem_vol_177(dbh,height)
                    elif formula_number ==178:
                            volume = stem_vol_178(dbh,height)
                    elif formula_number ==179:
                            volume = np.nan
                    elif formula_number ==180:
                            volume = stem_vol_180(dbh,height)
                    elif formula_number ==181:
                            volume = stem_vol_181(dbh,height)
                    elif formula_number ==182:
                            volume = stem_vol_182(dbh,height)
                    elif formula_number ==183:
                            volume = stem_vol_183(dbh,height)
                    elif formula_number ==184:
                            volume = stem_vol_184(dbh,height)
                    elif formula_number ==185:
                            volume = np.nan
                    elif formula_number ==186:
                            volume = stem_vol_186(dbh,height)
                    elif formula_number ==187:
                            volume = stem_vol_187(dbh,height)
                    elif formula_number ==188:
                            volume = stem_vol_188(dbh,height)
                    elif formula_number ==189:
                            volume = stem_vol_189(dbh,height)
                    elif formula_number ==190:
                            volume = stem_vol_190(dbh,height)
                    elif formula_number ==191:
                            volume = np.nan
                    elif formula_number ==192:
                            volume = stem_vol_192(dbh,height)
                    elif formula_number ==193:
                            volume = stem_vol_193(dbh,height)
                    elif formula_number ==194:
                            volume = stem_vol_194(dbh,height)
                    elif formula_number ==195:
                            volume = stem_vol_195(dbh,height)
                    elif formula_number ==196:
                            volume = stem_vol_196(dbh,height)
                    elif formula_number ==197:
                            volume = np.nan
                    elif formula_number ==198:
                            volume = stem_vol_198(dbh,height)
                    elif formula_number ==199:
                            volume = stem_vol_199(dbh,height)
                    elif formula_number ==200:
                            volume = stem_vol_200(dbh,height)
                    elif formula_number ==201:
                            volume = stem_vol_201(dbh,height)
                    elif formula_number ==202:
                            volume = stem_vol_202(dbh,height)
                    elif formula_number ==203:
                            volume = np.nan
                    elif formula_number ==204:
                            volume = stem_vol_204(dbh,height)
                    elif formula_number ==205:
                            volume = stem_vol_205(dbh,height)
                    elif formula_number ==206:
                            volume = stem_vol_206(dbh,height)
                    elif formula_number ==207:
                            volume = stem_vol_207(dbh,height)
                    elif formula_number ==208:
                            volume = stem_vol_208(dbh,height)
                    elif formula_number ==209:
                            volume = np.nan
                    elif formula_number ==210:
                            volume = stem_vol_210(dbh,height)
                    elif formula_number ==211:
                            volume = stem_vol_211(dbh,height)
                    elif formula_number ==212:
                            volume = stem_vol_212(dbh,height)
                    elif formula_number ==213:
                            volume = stem_vol_213(dbh,height)
                    elif formula_number ==214:
                            volume = stem_vol_214(dbh,height)
                    elif formula_number ==215:
                            volume = np.nan
                    elif formula_number ==216:
                            volume = stem_vol_216(dbh,height)
                    elif formula_number ==217:
                            volume = stem_vol_217(dbh,height)
                    elif formula_number ==218:
                            volume = stem_vol_218(dbh,height)
                    elif formula_number ==219:
                            volume = stem_vol_219(dbh,height)
                    elif formula_number ==220:
                            volume = stem_vol_220(dbh,height)
                    elif formula_number ==221:
                            volume = np.nan
                    elif formula_number ==222:
                            volume = stem_vol_222(dbh,height)
                    elif formula_number ==223:
                            volume = stem_vol_223(dbh,height)
                    elif formula_number ==224:
                            volume = stem_vol_224(dbh,height)
                    elif formula_number ==225:
                            volume = stem_vol_225(dbh,height)
                    elif formula_number ==226:
                            volume = stem_vol_226(dbh,height)
                    elif formula_number ==227:
                            volume = np.nan
                    elif formula_number ==228:
                            volume = stem_vol_228(dbh,height)
                    elif formula_number ==229:
                            volume = stem_vol_229(dbh,height)
                    elif formula_number ==230:
                            volume = stem_vol_230(dbh,height)

                        
            else:
                volume= np.nan
                
            
            #volume = stem_vol_6(dbh, height) if hasattr(stem_volume, f"stem_vol_{formula_number}") else float('nan')
            #print(f"Species {sp} with DBH {row['diameter at breast height [mm]']} has volume {volume} using formula {formula_number}")
            
            volumes.append(volume)
        print(volumes, len(volumes))
        #volumes_row = pd.DataFrame([volumes], columns=[f'F{i}' for i in range(1, 231)])
        #print(volumes_row)
        #output_df = pd.concat([output_df, volumes_row], axis=1)
        #output_df.loc[ "F"+str(formula_number) ] = volumes
        #print(output_df)
    #volumes_row = pd.DataFrame([volumes], columns=[f'F{formula_number}']).T
    #print(volumes_row)
        output_df[f'F{formula_number}'] = volumes
    
    return output_df

expanded_df = expand_dataframe(input_df)

#%%timeit
result = expand_dataframe(input_df)
