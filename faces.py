from functools import reduce
import face_recognition
from numpy import ndarray as NDArray

def get_image_data(image: NDArray):
    locations = face_recognition.face_locations(image)
    encodings = face_recognition.face_encodings(image, locations)
    return (encodings, locations)

def compare_faces(known_encoding: NDArray, unknown_encodings: list[NDArray]):
    map_combinator = lambda known: lambda unknown: face_recognition.compare_faces([known], unknown)
    results = reduce(lambda x, y: x.extend(y) or x, list(map(map_combinator(known_encoding), unknown_encodings)), [])
    return results

def compare_faces2(known_image: NDArray, unknown_image: NDArray):
    known_encoding, _ = get_image_data(known_image)
    unknown_encoding, _ = get_image_data(unknown_image)
    return compare_faces(known_encoding[0], unknown_encoding)

def draw_faces(image: NDArray, locations: list[tuple[int, int, int, int]]):
    from PIL import Image, ImageDraw
    image = Image.fromarray(image)
    draw = ImageDraw.Draw(image)
    for top, right, bottom, left in locations:
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255), width=3)
    return image