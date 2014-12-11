import sys
import string
import numpy as np

class MOM_out(object):
    """Parser and container for MOM timings scraped from mom.out
    """

    def __init__(self,filename=None):
        """Return a MOM_out object
        """
        if filename is not None:

            self.read(filename)

    def read(self,filename):

        print("Parsing %s\n") % filename

        with open(filename, 'r') as momout:
            times = []
            timekeys = []
            tparse = False
            for line in momout:

                if tparse or line.startswith('Total runtime'):

                    tparse = True

                    # Grab the text up to column 32, strip out leading and trailing
                    # whitespace and parentheses and save in keys array 
                    timekeys.append(line[:32].strip(string.whitespace).strip('()'))

                    # Builds a matrix of times
                    times.append(line[33:].split())

                # Terminate on last timing statistic
                if line.startswith('final flux_check_stocks'):
                    break

        # Post-processing
        # x = np.zeros(3, dtype=[('tmin','f8'),('tmax','f8'),('tavg','f8'),('tstd','f8'),('tfac','f8'),('grain','i4'),('pemin','i4'),('pemax','i4')])
        self.times = np.array(times,dtype=('f8,f8,f8,f8,f8,i4,i4,i4'))
        self.times.dtype.names = ('tmin','tmax','tavg','tstd','tfac','grain','pemin','pemax')

if __name__ == "__main__":

    t = MOM_out(sys.argv[1])

## Tabulating mpp_clock statistics across   2500 PEs...

##                                           tmin          tmax          tavg          tstd  tfrac grain pemin pemax
## Total runtime                      2088.452062   2088.672771   2088.534617      0.041640  1.000     0     0  2499
## Initialization                      345.137030    345.283794    345.193797      0.027224  0.165     0     0  2499
## Main loop                          1702.277038   1702.321808   1702.285551      0.003578  0.815     0     0  2499
## Termination                          29.999656     30.111275     30.013179      0.007841  0.014     0     0  2499
## Ice                                  29.872240     43.965854     34.461424      2.345482  0.017     1     0  2499
## Ice: bot to top                       0.877553      2.888470      1.430089      0.211257  0.001    41     0  2499
## Ice: update slow (dn)                27.917928     42.184189     32.116852      2.390277  0.015    41     0  2499
##   Ice: slow: conservation check       0.061693      0.199227      0.110127      0.028676  0.000    51     0  2499
##   Ice: slow: dynamics                22.131905     34.813968     25.310656      1.724635  0.012    51     0  2499
##        slow: ice_dynamics            21.672201     34.464556     24.833619      1.712067  0.012    51     0  2499
##        slow: comm/cut check           0.090624      0.682396      0.304643      0.107838  0.000    51     0  2499
##        slow: diags                    0.067996      0.458620      0.140199      0.050524  0.000    51     0  2499
##   Ice: slow: thermodynamics           0.061381      0.758684      0.164059      0.113730  0.000    51     0  2499
##   Ice: slow: restore/limit            0.000031      0.022493      0.004003      0.004318  0.000    51     0  2499
##   Ice: slow: salt to ocean            2.322937      5.418255      4.110797      0.888263  0.002    51     0  2499
##   Ice: slow: thermodyn diags          0.271975      0.861540      0.506269      0.055121  0.000    51     0  2499
## Ice: update fast                      0.587849      1.537081      0.914117      0.163478  0.000    41     0  2499
## Ocean                              1603.304101   1604.191210   1603.603253      0.109293  0.768     1     0  2499
## (Ocean initialization)              275.991922    276.711453    276.465338      0.160400  0.132    11     0  2499
## (Ocean ODA)                           0.003652      0.073226      0.017864      0.013602  0.000    11     0  2499
## (Ocean advection velocity)           16.898165     26.162367     25.263036      0.409359  0.012    31     0  2499
## (Ocean density diag)                 13.590659     26.946370     24.348951      0.636033  0.012    31     0  2499
## (Ocean update density)               63.160308     64.796063     64.069593      0.234250  0.031    31     0  2499
## (Ocean vertical mixing coeff)       153.408395    219.747481    188.126432     10.844364  0.090    31     0  2499
## (Ocean neutral physics)               0.002701      0.036594      0.010422      0.005007  0.000    31     0  2499
## (Ocean submesoscale restrat)        140.962444    167.421697    154.969307      5.750988  0.074    31     0  2499
## (Ocean shortwave)                     8.865169     37.866899     25.712769      7.690553  0.012    31     0  2499
## (Ocean sponges_eta)                   0.000609      0.053672      0.014192      0.013242  0.000    31     0  2499
## (Ocean sponges_tracer)                0.000399      0.012121      0.003021      0.002259  0.000    31     0  2499
## (Ocean sponges_velocity)              0.000317      0.008798      0.002687      0.002099  0.000    31     0  2499
## (Ocean xlandinsert)                   0.000640      0.015477      0.003424      0.001578  0.000    31     0  2499
## (Ocean xlandmix)                      0.000615      0.010722      0.003999      0.002363  0.000    31     0  2499
## (Ocean rivermix)                      0.842624      3.463367      1.664957      0.518399  0.001    31     0  2499
## (Ocean overexchange)                  0.000854      0.006178      0.003004      0.001050  0.000    31     0  2499
## (Ocean mixdownslope)                  0.001180      0.011576      0.004695      0.002150  0.000    31     0  2499
## (Ocean blob update)                   0.000535      0.016984      0.002635      0.001335  0.000    31     0  2499
## (Ocean blob cell update)              0.000000      0.000000      0.000000      0.000000  0.000    31     0  2499
## (Ocean blob diagnose depth)           0.000407      0.050105      0.015599      0.013476  0.000    31     0  2499
## (Ocean overflow)                      0.006248      0.208861      0.018318      0.007265  0.000    31     0  2499
## (Ocean overflow_OFP)                  0.000950      0.018340      0.004015      0.001653  0.000    31     0  2499
## (Ocean sigma transport)               0.011018      0.054070      0.031049      0.005738  0.000    31     0  2499
## (Ocean tracer update)               249.231937    291.153350    280.129431      5.354484  0.134    31     0  2499
## (Ocean surface flux)                 38.466060     67.728495     45.404727      4.077232  0.022    31     0  2499
## (Ocean bottom flux)                   0.130411      0.811807      0.444086      0.109344  0.000    31     0  2499
## (Ocean restoring flux)                0.096384      0.654277      0.281763      0.153243  0.000    31     0  2499
## (Ocean TPM source)                    0.332767      1.711517      0.904892      0.317115  0.000    31     0  2499
## (Ocean TPM bbc)                       0.000189      0.004980      0.001326      0.000735  0.000    31     0  2499
## (Ocean TPM tracer)                    0.022340      0.186501      0.070703      0.038747  0.000    31     0  2499
## (Ocean explicit accel_a)            201.900556    297.610951    229.183421     19.010727  0.110    31     0  2499
## (Ocean explicit accel_b)              7.368190     31.127607     15.965042      2.207114  0.008    31     0  2499
## (Ocean implicit accel)               23.135425     53.679910     42.418243      2.357276  0.020    31     0  2499
## (Ocean eta and pbot tendency)         0.045025      0.163677      0.095873      0.026291  0.000    31     0  2499
## (Ocean eta and pbot update)           0.388158     11.559359      1.489497      0.533740  0.001    31     0  2499
## (Ocean eta and pbot diagnose)        32.368335     81.798343     45.989182      6.764744  0.022    31     0  2499
## (Ocean rho_dzt tendency)              2.014444      3.183712      2.889200      0.059456  0.001    31     0  2499
## (Ocean dzt_dst update)                0.000000      0.000000      0.000000      0.000000  0.000    31     0  2499
## (Ocean surface height smooth)        19.821963     90.050118     44.600519     15.918357  0.021    31     0  2499
## (Ocean bottom pressure smooth)        0.000000      0.000000      0.000000      0.000000  0.000    31     0  2499
## (Ocean mass forcing)                  0.665575      1.115347      0.996316      0.032487  0.000    31     0  2499
## (Ocean barotropic forcing)            2.742845     42.525621      8.146715      4.784731  0.004    31     0  2499
## (Ocean barotropic dynamics)          35.677838    135.152663    104.732937     20.540714  0.050    31     0  2499
## (Ocean velocity update)              13.452836     36.507615     25.328269      1.160742  0.012    31     0  2499
## (Ocean diagnostics)                 164.375697    221.575169    187.457605      5.140638  0.090    31     0  2499
## (Ocean update T-cell thickness)      11.068326     22.355473     20.347151      0.764349  0.010    31     0  2499
## (Ocean update Total thickness)        0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean update L sys. thickness)       0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean update E sys. thickness)       0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean update U-cell thickness)      24.423514     55.977192     31.499436      5.036704  0.015    31     0  2499
## (Ocean tracer halo updates)           1.621021      2.953306      2.295550      0.174884  0.001    31     0  2499
## (Ocean velocity halo update)          0.857859      5.357504      1.827216      0.552119  0.001    31     0  2499
## (Ocean sum ocean surface)             0.824361      2.544282      1.345937      0.116589  0.001    31     0  2499
## (Ocean average state)                 0.013687      0.119562      0.051971      0.020722  0.000    31     0  2499
## (Ocean tracer tmask limit)            4.406404     17.410420     10.819375      4.127833  0.005    31     0  2499
## (Ocean gotm: advection)               0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean increment eta)                 0.000430      0.060458      0.016110      0.015614  0.000    31     0  2499
## (Ocean increment tracer)              0.000448      0.019292      0.002340      0.001365  0.000    31     0  2499
## (Ocean increment velocity)            0.000340      0.015597      0.005181      0.004358  0.000    31     0  2499
## (Ocean update rho_salinity)           0.490048      1.228813      0.841186      0.102433  0.000    31     0  2499
## (Ocean idealized surface waves)       0.000408      0.379086      0.004299      0.009902  0.000    31     0  2499
## (Ocean open boundaries)               0.000000      0.000000      0.000000      0.000000  0.000    31     0  2499
## (Ocean tracer: bih tracer)            0.001217      0.023938      0.004404      0.001745  0.000    31     0  2499
## (Ocean tracer: lap tracer)            0.001585      0.034499      0.007854      0.003471  0.000    31     0  2499
## (Ocean tracer: vert diffuse)          1.677519      7.319305      4.753185      1.428041  0.002    31     0  2499
## (Ocean tracer: vert diffuse impl     16.812868     30.137272     26.752889      1.202790  0.013    31     0  2499
## (Ocean tracer: advection)           178.220814    214.967493    200.819811      6.911816  0.096    31     0  2499
## (Ocean tracer: frazil)                0.664008      1.652434      1.145481      0.094386  0.001    31     0  2499
## (Ocean tracer: convection)            0.000514      0.003973      0.001998      0.001002  0.000    31     0  2499
## (Ocean tracer: Lagrangian blobs)      0.002607      0.028178      0.007765      0.003453  0.000    31     0  2499
## (Ocean tracer: implicit blobs)        0.000687      0.020376      0.002551      0.001789  0.000    41     0  2499
## (Ocean tracer: adjust the L thic      0.000232      0.004141      0.001475      0.001000  0.000    41     0  2499
## (Ocean tracer: adjust the E thic      0.000463      0.003613      0.001868      0.001002  0.000    41     0  2499
## (Ocean CT2PT: 1)                      0.000000      0.000000      0.000000      0.000000  0.000    31     0  2499
## (Ocean CT2PT: 2)                      0.000000      0.000000      0.000000      0.000000  0.000    31     0  2499
## (Ocean CT2PT: 3)                      0.000000      0.000000      0.000000      0.000000  0.000    31     0  2499
## (Ocean vmix: constant)                0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean vmix: PPvmix)                  0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean vmix: KPP_test)                0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean vmix: KPP_mom4p0)              0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean vmix: KPP_mom4p1)             91.840544    142.998865    110.904872      6.802817  0.053    41     0  2499
## (Ocean vmix: chenvmix)                0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean vmix: gotmvmix)                0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean vmix: tidal)                  47.440135     88.407090     70.286693      7.737030  0.034    41     0  2499
## (Ocean vmix: watermass_diag)          0.000948      0.014725      0.006044      0.003751  0.000    41     0  2499
## (Ocean const   lap frict)             0.000000      0.000000      0.000000      0.000000  0.000    31     0  2499
## (Ocean general lap frict)             0.006967      0.127780      0.026122      0.009525  0.000    31     0  2499
## (Ocean C-grid lap frict)              0.000000      0.000000      0.000000      0.000000  0.000    31     0  2499
## (Ocean const   bih frict)             0.000000      0.000000      0.000000      0.000000  0.000    31     0  2499
## (Ocean general bih frict)           123.689861    222.145766    149.061241     16.021981  0.071    31     0  2499
## (Ocean c-grid  bih frict)             0.000000      0.000000      0.000000      0.000000  0.000    31     0  2499
## (Ocean advect: horz 4th)              0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: vert 4th)              0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: horz 6th)              0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: vert 6th)              0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: horz quk)              0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: vert quk)              0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: horz qukmom3)          0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: vert qukmom3)          0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: MDFL-sup-b)            0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: MDFL-sweby)            0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: MDFL-sweby-all)        0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: MDFL-sweby-test)       0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: DST-linear)            0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: DST-linear-test)       0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: MDFL-sweby-mpi)        0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: MDFL-sweby-cuk)        0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: MDFL-sweby-cui)        0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: MDFL-sweby-cuj)        0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: MDFL-sweby-diag)       0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: MDPPM)               150.570608    192.803064    169.835942      4.922965  0.081    41     0  2499
## (Ocean advect: MDPPM-TEST)            0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: psom total)            0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean psom advect: psom_x)           0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean psom advect: psom_y)           0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean psom advect: psom_z)           0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: MDMDT-TEST)            0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: horz up)               0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: vert up)               0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: horz 2nd)              0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: vert 2nd)              0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: gyre_overturn)         0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean advect: advect diss)           0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean shortwave morel pen)           0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean shortwave morel pen-mom4p      0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Ocean_OFP_init)                      0.000000      0.000000      0.000000      0.000000  0.000    31     0  2499
## (Ocean_OFP_main)                      0.000000      0.000000      0.000000      0.000000  0.000    31     0  2499
## (ocean_OFP_update_1)                  0.000000      0.000000      0.000000      0.000000  0.000    31     0  2499
## (ocean_OFP_update_2)                  0.000000      0.000000      0.000000      0.000000  0.000    31     0  2499
## (ocean_OFP_update_3)                  0.000000      0.000000      0.000000      0.000000  0.000    31     0  2499
## (Ocean diagnostics: adv_vel)         40.957902     83.039464     63.812224      7.102383  0.031    31     0  2499
## (Ocean diagnostics: tracer)          73.904595    157.783341     99.465941      8.435857  0.048    31     0  2499
## (Ocean diagnostics: velocity)        22.782964     27.608795     24.172821      0.517465  0.012    31     0  2499
## (Ocean adv_vel_diag: numerics)        0.000383      0.000967      0.000655      0.000066  0.000    41     0  2499
## (Ocean adv_vel_diag: s-trans)         7.392026     19.209469     15.187877      1.581702  0.007    41     0  2499
## (Ocean adv_vel_diag: rho-trans)      33.425021     66.300586     48.601653      7.648361  0.023    41     0  2499
## (Ocean adv_vel_diag: nrho-trans)      0.002096      0.020979      0.010635      0.003784  0.000    41     0  2499
## (Ocean adv_vel_diag: theta-trans      0.000791      0.008036      0.003577      0.001975  0.000    41     0  2499
## (Ocean tracer_diag: mld_dtheta)       0.000173      0.000825      0.000422      0.000105  0.000    41     0  2499
## (Ocean tracer_diag: mld)              6.269397     15.541707     11.767925      2.077625  0.006    41     0  2499
## (Ocean tracer_diag: rho_mld)          0.004053      0.007443      0.005324      0.000476  0.000    41     0  2499
## (Ocean tracer_diag: potrho depth      0.000055      0.000244      0.000091      0.000013  0.000    41     0  2499
## (Ocean tracer_diag: theta depth)      0.000052      0.000153      0.000095      0.000012  0.000    41     0  2499
## (Ocean tracer_diag: tracer on rh      0.000518      0.038099      0.003229      0.002335  0.000    41     0  2499
## (Ocean tracer_diag: tracer_zrho       0.000232      0.017147      0.000577      0.000386  0.000    41     0  2499
## (Ocean tracer_diag: numerical)        4.086535      5.981163      4.680882      0.192539  0.002    41     0  2499
## (Ocean tracer_diag: diag mixing       0.000212      0.003751      0.001579      0.001067  0.000    41     0  2499
## (Ocean tracer_diag: conserve)         5.791432     16.117229      9.809084      1.426695  0.005    41     0  2499
## (Ocean tracer_diag: total water       0.000233      0.001004      0.000435      0.000097  0.000    41     0  2499
## (Ocean tracer_diag: total water      30.667003    118.542057     55.650821      8.528063  0.027    41     0  2499
## (Ocean tracer_diag: total tracer     17.169625     17.712256     17.532996      0.101084  0.008    41     0  2499
## (Ocean tracer_diag: integrals)        0.918986      1.117448      0.973878      0.025492  0.000    41     0  2499
## (Ocean tracer_diag: change)           1.519657      1.524626      1.520800      0.000364  0.001    41     0  2499
## (Ocean tracer_diag: land check)       0.129482      0.134612      0.133531      0.000530  0.000    41     0  2499
## (Velocity diag: energy analysis)      0.000000      0.000000      0.000000      0.000000  0.000    31     0  2499
## (Velocity diag: press convert)        0.000000      0.000000      0.000000      0.000000  0.000    31     0  2499
## (Velocity diag: press energy)         0.000000      0.000000      0.000000      0.000000  0.000    31     0  2499
## (Velocity diag: friction energy)      0.000000      0.000000      0.000000      0.000000  0.000    31     0  2499
## (Velocity diag: vert dissipation      0.002262      0.011554      0.006968      0.001440  0.000    31     0  2499
## (Wave model initialization)           0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## (Wave diagnostics)                    0.000000      0.000000      0.000000      0.000000  0.000    41     0  2499
## Land-ice-atm coupler                 23.775657     38.150575     33.396623      2.557425  0.016     1     0  2499
## SFC boundary layer                   20.987529     29.208919     25.636527      1.530432  0.012    11     0  2499
## Flux DN from atm                      2.305239      8.943363      4.401835      1.046943  0.002    41     0  2499
## Flux land to ice                      0.019453      7.288575      1.297308      1.240507  0.001    41     0  2499
## XGrid generation                      0.011848      0.498013      0.110220      0.067791  0.000    41     0  2499
## Flux UP to atm                        0.040992      7.001835      1.950162      1.527152  0.001    41     0  2499
## Ice-ocean coupler                    15.828352     16.670092     16.370715      0.112038  0.008     1     0  2499
## Flux ice to ocean                     5.842649      6.321193      6.106554      0.081713  0.003    41     0  2499
## Flux ocean to ice                     9.643072     10.598808     10.263995      0.144430  0.005    41     0  2499
## generate_sfc_xgrid                    0.012259      0.513585      0.124231      0.072751  0.000     0     0  2499
## flux_ocean_to_ice                     9.947136     10.612120     10.284033      0.136941  0.005     0     0  2499
## flux_ice_to_ocean                     5.872766      6.345189      6.124371      0.082054  0.003     0     0  2499
## flux_check_stocks                     0.000000      0.000000      0.000000      0.000000  0.000     0     0  2499
## ATM                                  66.645623     68.494236     67.850730      0.368354  0.032     0     0  2499
##   ATM: update_ice_model_slow_up       0.899634      2.932277      1.455881      0.214237  0.001     0     0  2499
##   ATM: atmos loop                    24.428292     36.419882     32.923751      2.032078  0.016     0     0  2499
##      A-L: atmos_tracer_driver_ga      0.000000      0.000000      0.000000      0.000000  0.000     0     0  2499
##      A-L: sfc_boundary_layer         20.988609     29.214264     25.643331      1.530226  0.012     0     0  2499
##      A-L: update_atmos_model_dow      0.000000      0.000000      0.000000      0.000000  0.000     0     0  2499
##      A-L: flux_down_from_atmos        2.305630      8.944302      4.403853      1.046677  0.002     0     0  2499
##      A-L: update_land_model_fast      0.000011      0.000125      0.000047      0.000014  0.000     0     0  2499
##      A-L: update_ice_model_fast       0.598588      1.543473      0.924953      0.164082  0.000     0     0  2499
##      A-L: flux_up_to_atmos            0.041241      7.002198      1.950683      1.527143  0.001     0     0  2499
##      A-L: update_atmos_model_up       0.000015      0.000091      0.000044      0.000009  0.000     0     0  2499
##   ATM: update_land_model_slow         0.000003      0.000042      0.000017      0.000005  0.000     0     0  2499
##   ATM: flux_land_to_ice               0.019641      7.289088      1.298922      1.240737  0.001     0     0  2499
##   ATM: update_ice_model_slow_dn      27.943475     42.203694     32.150585      2.390483  0.015     0     0  2499
##   ATM: flux_ice_to_ocean_stocks       0.007487      0.039480      0.015003      0.005473  0.000     0     0  2499
## OCN                                1603.356567   1605.120763   1603.767019      0.201124  0.768     0     0  2499
## intermediate restart                  0.000000      0.000000      0.000000      0.000000  0.000     0     0  2499
## final flux_check_stocks               0.110284      0.110646      0.110370      0.000034  0.000     0     0  2499
##  MPP_STACK high water mark=           0
