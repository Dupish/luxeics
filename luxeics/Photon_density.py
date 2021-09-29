
    
def Photon_density(xoffset,yoffset, X1, X2, spotsize,sigmaT):
    print(f"Sigma Transverse :{sigmaT}")
    figure(figsize=(14,6))

    ax1=subplot(121,aspect=1)
    scatter(xoffset, yoffset, color='r',marker='.',lw=0,s=W);
    xlim(-2*spotsize,2*spotsize)
    ylim(-2*spotsize,2*spotsize)

    xlabel(r'$x$ (micron)')
    ylabel(r'$y$ (micron)');
    title('zero source size')


    ax2=subplot(122,aspect=1)

    # plot(X1+xoffset, X2+yoffset, color='m', marker=',',lw=0);





    scatter(X1+xoffset, X2+yoffset, color='m', marker='.',lw=0,s=W);

    xlim(-2*spotsize,2*spotsize)
    ylim(-2*spotsize,2*spotsize)

    xlabel(r'$x$ (micron)')
    ylabel(r'$y$ (micron)');
    title('finite source size')

    ax1.add_patch(Circle((0,0),spotsize,color='C0',fill=False))
    ax2.add_patch(Circle((0,0),spotsize,color='C0',fill=False))


    suptitle(f'{sampling} sampling')

    

    print(r'Goal: To get as many photons within the spot size')


    Area=np.pi*spotsize**2

    selector1 = sqrt(xoffset**2+yoffset**2) < spotsize
    selector2 = sqrt((xoffset+X1)**2+(yoffset+X2)**2) < spotsize


    print ( f'IP-laser spot size: {spotsize:.2f} micron')
    print ( f'baseline          : {baseline/1e6:.2f} metres')
    print ('-'*42)

    print (f'photons in spot, {sampling} sampling:')
    print (f'macrophoton weight               : {amax(W):.4g}')
    print ( 'macrophotons, zero   source size :',sum( selector1 ) )
    print ( 'macrophotons, finite source size :',sum( selector2 ) )
    print ( 'photon weight, zero   source size:',sum(W[selector1 ] ) )
    print ( 'photon weight, finite source size:',sum(W[selector2 ] ) )
    
    
    print ( f'Photon density, zero   source size:',sum(W[selector1 ] )/Area)
    print ( f'Photon density, finite source size:',sum(W[selector2 ] )/Area)
    
    print (' ######################################### '  )
    print ('                                           '  )
    
def run():
    
    # import matplotlib.pyplot as plt


    input_filename = 'New.yml'

    with open( input_filename, 'r' ) as stream:
        input_dict = yaml.load(stream, Loader=yaml.SafeLoader)
    luxeics.main_program( input_filename )
    %pylab inline

    import h5py
    import yaml
    from scipy.interpolate import interp2d,RectBivariateSpline
    import numpy as np
    from matplotlib.backends.backend_pdf import PdfPages
    input_filename = 'New'

    with h5py.File(input_filename + '.h5' ,'r') as ff:
    #     omega      = ff['final-state/spectrum/omega'][:]/1e9
    #     theta      = ff['final-state/spectrum/theta'][:]*1e6
    #     spectrum   = ff['final-state/spectrum/spectrum'][:]

        K0,K1,K2,K3  = ff['final-state/photon/momentum'][:].T
        X0,X1,X2,X3  = ff['final-state/photon/position'][:].T
        W            = ff['final-state/photon/weight'  ][:]

        P0,P1,P2,P3  = ff['final-state/electron/momentum'][:].T
    #     X0,X1,X2,X3  = ff['final-state/photon/position'][:].T
    #     We            = ff['final-state/photon/weight'  ][:]

    with open( input_filename + '.yml', 'r' ) as stream:
        input_dict = yaml.load(stream, Loader=yaml.SafeLoader)

        mode             = input_dict['control']['mode']


        beam_charge      = float( input_dict['beam']['beam_charge'])
        number_electrons = int( beam_charge / 1.60217653e-19)

    #     sampling         = input_dict['control']['sampling']
        sampling = mode

        w0               = float(input_dict['laser']['w0'])
        omega0           = float(input_dict['laser']['omega0'])
        gamma            = float(input_dict['beam']['gamma'])
        Xr               = 4*gamma*omega0/511*10**(-3)
        energyspread     = float(input_dict['beam']['energyspread'])
        sigmaT           = float(input_dict['beam']['sigmaT'])
    thetax=K1/K3
    thetay=K2/K3

    baseline = 7.5e6 

    xoffset = thetax * baseline
    yoffset = thetay * baseline
    spotsize = 3 # micron


    Photon_density( xoffset , yoffset, X1, X2, spotsize,sigmaT)
    Photon_density( xoffset , yoffset , X1 , X2 , 10 ,sigmaT)

    print (input_dict)


