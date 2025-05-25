from setuptools import find_packages, setup

package_name = 'wall_distance_publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'rclpy', 'pyserial'],
    zip_safe=True,
    maintainer='mustaza',
    maintainer_email='mustaza@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor_publisher = wall_distance_publisher.sensor_publisher:main',
            'visualizer_node = wall_distance_publisher.visualize_node:main',
        ],
    },
)
