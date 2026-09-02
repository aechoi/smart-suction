import numpy as np
import trimesh as tm


class Probe:
    def __init__(
        self,
        position: np.ndarray = np.zeros(3),
        orientation: np.ndarray = np.array([0, 0, -1]),
        radius: float = 0.02,
        num_rays: int = 8,
        cup_height: float = 0.02,
    ):
        self._radius = radius
        self._num_rays = num_rays

        self._position = position
        self._orientation = orientation / np.linalg.norm(orientation)
        self._meas_points = self._make_ring()
        self._cup_height = cup_height

    def _make_ring(self) -> np.ndarray:
        angles = np.linspace(0, 2 * np.pi, self._num_rays, endpoint=False)
        x = self._radius * np.cos(angles)
        y = self._radius * np.sin(angles)
        z = np.zeros_like(x)
        ring = np.vstack((x, y, z)).T
        return ring

    def transform(self, T) -> None:
        """Transform the probe's position and orientation by a given homogeneous transform T."""
        R = T[:3, :3]
        t = T[:3, 3]

        self._position = t
        self._orientation = R @ self._orientation
        self._meas_points = (R @ self._meas_points.T).T + self._position

    def sense(self, mesh: tm.base.Trimesh):
        directions = np.tile(self._orientation, (self._num_rays, 1))

        locs, ray_ids, tri_ids = mesh.ray.intersects_location(
            self._meas_points, directions, multiple_hits=False
        )

        distances = np.full(self._num_rays, np.inf)
        normals = np.zeros((self._num_rays, 3))
        if np.any(mesh.contains(self._meas_points)):
            return distances, normals

        for loc, r, t in zip(locs, ray_ids, tri_ids):
            distances[r] = np.dot(loc - self._meas_points[r], self._orientation)
            normals[r] = mesh.face_normals[t]

        capacitance = np.clip(self._cup_height - distances, 0, None)

        return capacitance, normals

    def make_ray_lines(self, length=None):
        """
        Convert ray origins/directions into line segments for trimesh visualization.

        Args:
            length: a float or numpy array of shape (num_rays,) indicating the length of each ray.
        """
        lines = []
        if length is None:
            length = np.full(self._num_rays, 0.05)
        if isinstance(length, (float, int)):
            length = np.full(self._num_rays, length)

        for meas_point, l in zip(self._meas_points, length):
            line = np.vstack([meas_point, meas_point + self._orientation * l])
            lines.append(tm.load_path(line))

        return lines

    def make_probe(self):
        # Close the loop
        points = np.vstack([self._meas_points, self._meas_points[0], self._position])

        # Convert to Path3D
        path = tm.load_path(points)

        return path


def sample_translation(bounds):
    return np.array(
        [
            np.random.uniform(*bounds[0]),
            np.random.uniform(*bounds[1]),
            np.random.uniform(*bounds[2]),
        ]
    )


def sample_small_rotation():
    axis = np.random.normal(size=3)
    axis /= np.linalg.norm(axis)
    # axis[2] = np.abs(axis[2])  # Prefer rotations about x/y axes
    angle = np.random.uniform(0, np.pi / 4)

    return tm.transformations.rotation_matrix(angle, axis)[:3, :3]


def sample_pose(T_nominal, trans_bounds):
    T = np.eye(4)
    T[:3, :3] = T_nominal[:3, :3] @ sample_small_rotation()
    T[:3, 3] = T_nominal[:3, 3] + sample_translation(trans_bounds)
    return T
