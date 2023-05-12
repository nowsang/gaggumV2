from setuptools import setup

package_name = 'gaggum_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sangwon',
    maintainer_email='sangwon@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'image_capture = gaggum_python.image_capture:main',
            'yolov5 = gaggum_python.yolov5:main',
            'scan_read = gaggum_python.scan_read:main',
            'run_mapping = gaggum_python.run_mapping:main',
            'a_star = gaggum_python.a_star:main',
            'a_star_local_path = gaggum_python.a_star_local_path:main',
            'odom = gaggum_python.odom:main',
            'path_tracking = gaggum_python.path_tracking:main',
            'wall_tracking = gaggum_python.wall_tracking:main',
            'utils = gaggum_python.utils:main',
            'load_map = gaggum_python.load_map:main',
        ],
    },
)
