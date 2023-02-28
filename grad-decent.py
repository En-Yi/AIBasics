

# The following symbol is for VSCode interactive plot test
# %%
import matplotlib.pyplot as plot
import numpy as np
import plotly.io as pio

# %%
#define function z=F1(x,y)= xy-(yx**3+xy**3)/6
def F1(x,y):
    try:
        a=0
        a=x*y -  (y*x**3+x*y**3)/6
    except Exception as e:
        print('x=%.3f, y=%.3f, a=%.3f exception= %s'%(x, y, a, e))
    return a
def PF1x(x,y):
    try:
        a=0
        a=y-(3*y*x**2+y**3)/6
    except Exception as e:
        print('x=%.3f, y=%.3f, a=%.3f exception= %s'%(x, y, a, e))
    return a
def PF1y(x,y):
    try:
        a=0
        a=x -(x**3+3*x*y**2)/6
    except Exception as e:
        print('x=%.3f, y=%.3f, a=%.3f exception= %s'%(x, y, a, e))

    return a
        
step_x, step_y, step_z = [], [], []
x_point, y_point, lr = 4.1, -4.1, 0.01
i = 0
while i<1000 and (abs(PF1x(x_point, y_point))>0.00001 or abs(PF1y(x_point, y_point))>0.00001):
    i += 1
    print("i=", i)
    step_x.append(x_point)
    step_y.append(y_point)
    step_z.append(F1(x_point, y_point))
    
    x_point = x_point - lr*PF1x(x_point, y_point)
    y_point = y_point - lr*PF1y(x_point, y_point)

#figure is the most top object which contains Axes    
#not giving figsiz, plot will find a fittable size
fig = plot.figure()
#get current Axes instance
ax=fig.add_subplot(projection='3d')
ax.set_zlim(-150,150)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_zlabel('z', fontsize=12)

x=np.arange(-5, 5, 0.1)
y=np.arange(-5, 5, 0.1)
#meshgrid Return coordinate matrices from coordinate vectors.
x,y=np.meshgrid(x,y)
#cmap color map https://matplotlib.org/stable/gallery/color/colormap_reference.html
surf= ax.plot_surface(x, y, F1(x,y), cmap='cool', linewidth=0, alpha=0.2, antialiased=False)

#Plot y versus x as lines and/or markers. with 'g:o' green circle marker
ax.plot(step_x, step_y, step_z, 'g:o') #the gradient decent curve
#https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure.colorbar
#shrink: Fraction by which to multiply the size of the colorbar.
#aspect: Ratio of long to short dimensions
fig.colorbar(surf, shrink=0.5, aspect=5)
#https://matplotlib.org/devdocs/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.view_init.html
#in degree
ax.view_init(elev=30, azim=10)
plot.show()
input("Press Enter to continue...")

import plotly.graph_objects as go

figgo = go.Figure(data=[go.Surface(z=F1(x,y), x=x, y=y)])
x_eye = -1.25
y_eye = 2
z_eye = 0.5
figgo.update_layout(title='Gradient Decent', autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90),
                  scene_camera_eye=dict(x=x_eye, y=y_eye, z=z_eye),
            updatemenus=[dict(type='buttons',
                  showactive=False,
                  y=1,
                  x=0.8,
                  xanchor='left',
                  yanchor='bottom',
                  pad=dict(t=45, r=10),
                  buttons=[dict(label='Play',
                                 method='animate',
                                 args=[None, dict(frame=dict(duration=5, redraw=True), 
                                                             transition=dict(duration=0),
                                                             fromcurrent=True,
                                                             mode='immediate'
                                                            )]
                                            )
                                      ]
                              )
                        ]
                  )
line_marker = dict(color='#101010', width=4)
#for xx, yy, zz in zip(step_x, step_y, step_z):
#figgo.add_scatter3d(x=xx, y=yy, z=zz, mode='lines', line=line_marker, name='')    
figgo.add_scatter3d(x=step_x, y=step_y, z=step_z, mode='markers', 
                    marker=dict(
                            size=[1, 1, 1],
                            sizemode='diameter'),
                    line=line_marker, name='')      
def rotate_z(x, y, z, theta):
    w = x+1j*y
    return np.real(np.exp(1j*theta)*w), np.imag(np.exp(1j*theta)*w), z

frames=[]
for t in np.arange(0, 6.26, 0.1):
    xe, ye, ze = rotate_z(x_eye, y_eye, z_eye, -t)
    frames.append(go.Frame(layout=dict(scene_camera_eye=dict(x=xe, y=ye, z=ze))))
figgo.frames=frames

figgo.show()
pio.write_html(figgo, './goplot-3degree.html', auto_play=True)
input("Press Enter to continue...")






# %%
