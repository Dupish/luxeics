{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'beam': {'beam_charge': '100e-12', 'emittance': 1.5, 'energyspread': '1e-3', 'gamma': 32289.62818003914, 'sigmaL': 20.0, 'sigmaT': 10.0, 'theta': 0.0}, 'control': {'beam': {'Nemit': 30, 'Nenergy': 7}, 'energyaverage': False, 'laser': {'sigma_crit': 500.0, 'sigma_rescale': False}, 'mode': 'full', 'name': 'New', 'radiation': 'KN', 'sample_electrons': '1e8', 'sampling': 'rejection'}, 'detector': {'omega': ['5.0e9', '9.2e9', 300], 'pdim': 2, 'phi': 0.0, 'theta': [0, '15e-6', 110]}, 'laser': {'Tpulse': 100.0, 'a0': 0.1, 'omega0': 4.1, 'pol': 0.7853981633974483, 'pulse': 'cos2', 'w0': 25.0}}\n",
      ">>> mode == full\n",
      "[10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000] 100000000 100000000\n",
      " >> number_electrons   = 624150947\n",
      " >> sample_electrons   = 100000000\n",
      " >> electron weight    = 6.242\n",
      " >> MC sampling\n",
      "  > batch 0 : 10000000 macroelectrons\n",
      "   base photon weight : 6.987178588540231\n",
      "   number photons     : 13196\n",
      "   total photon number: 13196\n",
      "  > batch 1 : 10000000 macroelectrons\n",
      "   base photon weight : 6.711356019092371\n",
      "   number photons     : 13344\n",
      "   total photon number: 26540\n",
      "  > batch 2 : 10000000 macroelectrons\n",
      "   base photon weight : 6.829997247822177\n",
      "   number photons     : 12929\n",
      "   total photon number: 39469\n",
      "  > batch 3 : 10000000 macroelectrons\n",
      "   base photon weight : 6.9426760059578605\n",
      "   number photons     : 12923\n",
      "   total photon number: 52392\n",
      "  > batch 4 : 10000000 macroelectrons\n",
      "   base photon weight : 6.719423516098282\n",
      "   number photons     : 13348\n",
      "   total photon number: 65740\n",
      "  > batch 5 : 10000000 macroelectrons\n",
      "   base photon weight : 7.138228112862701\n",
      "   number photons     : 12675\n",
      "   total photon number: 78415\n",
      "  > batch 6 : 10000000 macroelectrons\n",
      "   base photon weight : 6.754829603288149\n",
      "   number photons     : 13334\n",
      "   total photon number: 91749\n",
      "  > batch 7 : 10000000 macroelectrons\n",
      "   base photon weight : 6.614732883917866\n",
      "   number photons     : 13469\n",
      "   total photon number: 105218\n",
      "  > batch 8 : 10000000 macroelectrons\n",
      "   base photon weight : 7.016576849185209\n",
      "   number photons     : 12667\n",
      "   total photon number: 117885\n",
      "  > batch 9 : 10000000 macroelectrons\n",
      "   base photon weight : 6.987008882758972\n",
      "   number photons     : 12959\n",
      "   total photon number: 130844\n"
     ]
    }
   ],
   "source": [
    "import yaml\n",
    "import numpy as np\n",
    "\n",
    "\n",
    "import luxeics\n",
    "# import matplotlib.pyplot as plt\n",
    "\n",
    "\n",
    "input_filename = 'New.yml'\n",
    "\n",
    "with open( input_filename, 'r' ) as stream:\n",
    "    input_dict = yaml.load(stream, Loader=yaml.SafeLoader)\n",
    "\n",
    "print (input_dict)\n",
    "\n",
    "\n",
    "\n",
    "luxeics.main_program( input_filename )\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Populating the interactive namespace from numpy and matplotlib\n"
     ]
    }
   ],
   "source": [
    "%pylab inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "import h5py\n",
    "import yaml\n",
    "from scipy.interpolate import interp2d,RectBivariateSpline\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "input_filename = 'New'\n",
    "\n",
    "with h5py.File(input_filename + '.h5' ,'r') as ff:\n",
    "#     omega      = ff['final-state/spectrum/omega'][:]/1e9\n",
    "#     theta      = ff['final-state/spectrum/theta'][:]*1e6\n",
    "#     spectrum   = ff['final-state/spectrum/spectrum'][:]\n",
    "    \n",
    "    K0,K1,K2,K3  = ff['final-state/photon/momentum'][:].T\n",
    "    X0,X1,X2,X3  = ff['final-state/photon/position'][:].T\n",
    "    W            = ff['final-state/photon/weight'  ][:]\n",
    "\n",
    "    P0,P1,P2,P3  = ff['final-state/electron/momentum'][:].T\n",
    "#     X0,X1,X2,X3  = ff['final-state/photon/position'][:].T\n",
    "#     We            = ff['final-state/photon/weight'  ][:]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open( input_filename + '.yml', 'r' ) as stream:\n",
    "    input_dict = yaml.load(stream, Loader=yaml.SafeLoader)\n",
    "    \n",
    "    mode             = input_dict['control']['mode']\n",
    "    \n",
    "    \n",
    "    beam_charge      = float( input_dict['beam']['beam_charge'])\n",
    "    number_electrons = int( beam_charge / 1.60217653e-19)\n",
    "\n",
    "#     sampling         = input_dict['control']['sampling']\n",
    "    sampling = mode\n",
    "    \n",
    "    w0               = float(input_dict['laser']['w0'])\n",
    "    omega0           = float(input_dict['laser']['omega0'])\n",
    "    gamma            = float(input_dict['beam']['gamma'])\n",
    "    Xr               = 4*gamma*omega0/511*10**(-3)\n",
    "    energyspread     = float(input_dict['beam']['energyspread'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "beam charge                              : 100.0 pC\n",
      "number of beam electrons                 : 6.242e+08\n",
      "------------------------------------------\n",
      "full sampling:\n",
      "max  single photon weight                : 7.138\n",
      "mean single photon weight                : 6.867\n",
      "total photon weight                      : 8.985e+05\n",
      "total photon weight per incident electron: 0.00144\n",
      "total macro photon number                : 130844\n",
      "------------------------------------------\n",
      " Frequency (Laser) :  4.1\n",
      "Recoil Factor:1.0363011783809037\n"
     ]
    }
   ],
   "source": [
    "print (f'beam charge                              : {beam_charge*1e12:.24} pC')\n",
    "print (f'number of beam electrons                 : {number_electrons:.3e}')\n",
    "print ('-'*42)\n",
    "print (f'{sampling} sampling:')\n",
    "print (f'max  single photon weight                : {amax(W):.4g}')\n",
    "print (f'mean single photon weight                : {mean(W):.4g}')\n",
    "print (f'total photon weight                      : {sum(W):.4g}')\n",
    "print (f'total photon weight per incident electron: {sum(W)/number_electrons:.4g}')\n",
    "print (f'total macro photon number                : {len(W)}')\n",
    "print ('-'*42)\n",
    "print(f' Frequency (Laser) :  {omega0}'  )\n",
    "print(f'Recoil Factor:{Xr}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1440x432 with 3 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "from matplotlib.backends.backend_pdf import PdfPages\n",
    "pp = PdfPages('multipage.pdf')\n",
    "\n",
    "\n",
    "\n",
    "fig,ax=subplots(1,3,figsize=(20,6))\n",
    "\n",
    "\n",
    "ax[0].hist2d(K1/1e6,K2/1e6,bins=(50,50),weights=W,rasterized=True,cmap=cm.magma);\n",
    "\n",
    "ax[0].set_title(f'{sampling} sampling')\n",
    "\n",
    "ax[0].set_xlabel(r'$k_x$ (MeV)')\n",
    "ax[0].set_ylabel(r'$k_y$ (MeV)')\n",
    "\n",
    "\n",
    "\n",
    "bbins=(linspace(-2*w0,2*w0,50),linspace(-2*w0,2*w0,50))\n",
    "\n",
    "\n",
    "ax[1].hist2d(X1,X2,bins=bbins,weights=W,rasterized=True,cmap=cm.magma);\n",
    "\n",
    "\n",
    "ax[1].set_xlabel(r'$x@$source (micron)')\n",
    "ax[1].set_ylabel(r'$y@$source (micron)')\n",
    "ax[1].set_title(f'{sampling} sampling')\n",
    "\n",
    "ax[1].set_xlim(-2*w0,2*w0)\n",
    "ax[1].set_ylim(-2*w0,2*w0)\n",
    "beta=(1-gamma**(-2))**0.5\n",
    "theta=sqrt(K1**2+K2**2)/K3\n",
    "\n",
    "N=( omega0 *((1+beta)* gamma)**2)\n",
    "A=((gamma**2)*(1-beta*np.cos(theta)))\n",
    "B=(0.25*Xr*(1+np.cos(theta)))\n",
    "Omega = N/(A+B)/(1+beta)\n",
    "\n",
    "\n",
    "bbins=(linspace(6,9,50),linspace(0,15,50))\n",
    "\n",
    "\n",
    "ax[2].hist2d(K0/1e9,sqrt(K1**2+K2**2)/K3*1e6,bins=bbins,weights=W/sqrt(K1**2+K2**2),rasterized=True,cmap=cm.magma);\n",
    "ax[2].scatter( Omega/1e9 , theta*1e6,c='r',s=0.02 )\n",
    "\n",
    "ax[2].set_xlabel(r'$\\omega$ (GeV)')\n",
    "ax[2].set_ylabel(r'$\\theta$ $  [Scattering$ $Angle]$ ($\\mu$rad)');\n",
    "ax[2].set_title(rf'{sampling} sampling')\n",
    "plt.savefig(pp, format='pdf')\n",
    "pp.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "thetax=K1/K3\n",
    "thetay=K2/K3\n",
    "\n",
    "baseline = 7.5e6 \n",
    "\n",
    "xoffset = thetax * baseline\n",
    "yoffset = thetay * baseline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "photons in spot, full sampling:\n",
      "macrophoton weight               : 7.138\n",
      "macrophotons, zero   source size : 109\n",
      "macrophotons, finite source size : 123\n",
      "photon weight, zero   source size: 747.3132707791631\n",
      "photon weight, finite source size: 845.1125737357152\n",
      "Photon Density, zero   source size : 26.43080024059464   γ /(μ)^2\n",
      "Photon Density, Finite   source size : 29.88974301758954   γ /(μ)^2\n"
     ]
    }
   ],
   "source": [
    "spotsize = 3 # micron\n",
    "\n",
    "\n",
    "\n",
    "def Photon_Density( xoffset,yoffset,X1,X2,spotsize ):\n",
    "\n",
    "    selector1 = sqrt(xoffset**2+yoffset**2) < spotsize\n",
    "    selector2 = sqrt((xoffset+X1)**2+(yoffset+X2)**2) < spotsize\n",
    "    {amax(W):.4g}\n",
    "    sum( selector1 )\n",
    "    sum( selector2 )\n",
    "    sum(W[selector1 ] )\n",
    "    sum(W[selector2 ] )\n",
    "    sum((W[selector1 ] ))/np.pi/spotsize**2\n",
    "    print (f'macrophoton weight               :')\n",
    "    print ( 'macrophotons, zero   source size :', )\n",
    "    print ( 'macrophotons, finite source size :',sum( selector2 ) )\n",
    "    print ( 'photon weight, zero   source size:', )\n",
    "    print ( 'photon weight, finite source size:', )\n",
    "    print ( 'Photon Density, zero   source size :', ,'  \\u03B3','/(\\u03BC)^2')\n",
    "    print ( 'Photon Density, Finite   source size :',sum((W[selector2 ] ))/np.pi/spotsize**2 ,'  \\u03B3','/(\\u03BC)^2')\n",
    "\n",
    "\n",
    "Photon_Density( xoffset,yoffset,X1,X2,spotsize )\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "hide_input": false,
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
