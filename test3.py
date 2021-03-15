import numpy as np
import open3d as o3d
import mayavi.mlab as mlab
from plyfile import PlyData, PlyElement


figure_id = 101

# Read .ply file
input_file = f'LiDAR_PointCloud{figure_id}/LiDAR_PointCloud.ply'

plydata = PlyData.read(input_file)

pts_x = plydata.elements[0].data['x']
pts_y = plydata.elements[0].data['y']
pts_z = plydata.elements[0].data['z']

fig = mlab.figure(bgcolor=(0, 0, 0), size=(1280, 720))

#given a set of points pts [N,3] and a set of intensities [N,]
mlab.points3d(pts_x, pts_y, pts_z, mode='point', figure=fig)
mlab.view(azimuth=-90, elevation=60, distance=100, focalpoint=(0,0,0))

mlab.show()