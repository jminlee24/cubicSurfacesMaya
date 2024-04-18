from traits.api import HasTraits, Range, Instance, \
    on_trait_change
from traitsui.api import View, Item, HGroup
from tvtk.pyface.scene_editor import SceneEditor
from mayavi.tools.mlab_scene_model import \
    MlabSceneModel
from mayavi.core.ui.mayavi_scene import MayaviScene

from mayavi import mlab
from numpy import linspace, pi, cos, sin
import numpy as np


def curve(n_mer, n_long):
  phi = linspace(0, 2 * pi, 2000)
  return [cos(phi * n_mer) * (1 + 0.5 * cos(n_long * phi)),
          sin(phi * n_mer) * (1 + 0.5 * cos(n_long * phi)),
          0.5 * sin(n_long * phi),
          sin(phi * n_mer)]


def F(x, y, z, k):
  return x**2 + y**2 + z**2 - x * y * z - k - 2


class Visualization(HasTraits):
  k = Range(-8, 18, 3)
  opacity = Range(0, 100, 100)
  scene = Instance(MlabSceneModel, ())
  axis = {"x": None, "y": None, "z": None}
  lines = []
  intersection_points = []

  def __init__(self):
    # Do not forget to call the parent's __init__
    HasTraits.__init__(self)
    mesh = self.__get_mesh__()
    self.plot = self.scene.mlab.contour3d(
      mesh, colormap='Spectral', contours=[0], extent=[-10, 10, -10, 10, -10, 10])
    xx = yy = zz = np.arange(-10, 10, 0.1)
    xy = xz = yx = yz = zx = zy = np.zeros_like(xx)
    self.axis["y"] = mlab.plot3d(
      yx, yy, yz, line_width=0.1, tube_radius=0.125, color=(1, 0, 0))
    self.axis["z"] = mlab.plot3d(
      zx, zy, zz, line_width=0.1, tube_radius=0.125, color=(0, 1, 0))
    self.axis["x"] = mlab.plot3d(
      xx, xy, xz, line_width=0.1, tube_radius=0.125, color=(0, 0, 1))

    # 24 lines
    self.lines = get24Lines()

  def __get_mesh__(self):
    k = self.k
    x, y, z = np.ogrid[-10: 10: 100j, -10: 10: 100j, -10: 10: 100j]
    return F(x, y, z, k)

  @ on_trait_change('k')
  def update_plot(self):
    new_mesh = self.__get_mesh__()
    self.plot.mlab_source.set(scalars=new_mesh)

  @ on_trait_change("opacity")
  def update_opacity(self):
    print("hello")
    self.plot.mlab_source.set(opacity=self.opacity / 100)
  # the layout of the dialog created
  view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                   height=500, width=700, show_label=False),
              HGroup(
      '_', 'k', 'opacity',
  ),
  )


visualization = Visualization()
visualization.configure_traits()
