import requests
import json
import io

class OCRException(Exception): pass

class SpaceOcr(object):
    API_KEY = 'j/F,qkdZEXR.!,H'
    url_api = "https://api.ocr.space/parse/image"

    def image_to_string(self, image, **kwargs):
        language = kwargs["lang"] if hasattr(kwargs, "lang") else "eng"

        files = {image.filename: self.__getImgData(image)}
        params = {
            "apikey": self.__getKey(),
            "language": language,
            "detectOrientation": True,
            "scale": True
        }

        result = requests.post(SpaceOcr.url_api, files = files, data = params)
        data = json.loads(result.content.decode())

        if data["OCRExitCode"] != 1:
            raise OCRException(data["ErrorMessage"][0])
        
        return data["ParsedResults"][0]["ParsedText"]

    def __getImgData(self, img):
        MAX_FILE_SIZE = 1024*1024

        format = img.format
        img = img.convert('L')

        image_data = io.BytesIO()
        img.save(image_data, format=format)
        file_size = image_data.tell()
 
        if file_size > MAX_FILE_SIZE:
            new_size = tuple(item * (MAX_FILE_SIZE / file_size) for
                                 item in img.size)
            img.thumbnail(new_size)

            image_data = io.BytesIO()
            img.save(image_data, format=format)

        image_data.seek(0)
        return image_data

    def __getKey(self):
        m = '\x0eL%\x1aF^Thv:j\x16\x18\x19\x7f'
        return "".join(map((lambda x,y: chr(ord(x)^ord(y))),
                           m, SpaceOcr.API_KEY))