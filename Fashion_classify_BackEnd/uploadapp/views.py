from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import numpy as np
import PIL.Image as pil_img
import tensorflow as tf

# Create your views here.
from uploadapp.models import File
from uploadapp.serializer import FileSerializer


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()

            uploaded_image_name = request.data.get("file")
            image_arrays = []
            x = []
            size = (400, 533)
            img_thumb_size = (90, 120)
            right_shape = (533, 400, 3)

            file_name = "00b8048d-635e-4e56-b182-071fb24eea32.jpg"
            # image = pil_img.open('media/' + uploaded_image_name)  # Concat directory and filename to open file
            image = pil_img.open('media/' + str(uploaded_image_name))  # Concat directory and filename to open file
            if np.shape(image) != right_shape:
                image = image.resize(size)
            image.save('media/' + str(uploaded_image_name))
            image.thumbnail(img_thumb_size)
            x = np.array(image)

            x = np.expand_dims(x, axis=0)
            x = x / 255.0
            image_arrays.append(x)

            x = np.concatenate([x for x in image_arrays])
            model = tf.keras.models.load_model("ml_model/Run-1")
            predictions = model.predict(x)
            classes_lst = ["dress", "hat", "longsleeve", "outwear", "pants", "shirt", "shoes", "shorts", "skirt",
                           "t-shirt"]
            probabilities = tf.nn.softmax(predictions).numpy()
            # Convert the probabilities into percentages
            probabilities = probabilities * 100
            max_proba = np.amax(probabilities)
            a, pred_class = np.where(probabilities == max_proba)
            pred_class = pred_class.tolist()
            pred_class = pred_class[0]
            prediction_class = classes_lst[pred_class]

            probabilities_tolist = probabilities.tolist()
            print("probabilities_tolist", probabilities_tolist)

            return Response(
                {"res_serialized": file_serializer.data, "max_proba": max_proba, "prediction_class": prediction_class},
                status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImagesView(APIView):
    def post(self, request):
        fashion_images = File.objects.all().order_by("-id")
        serializer = FileSerializer(fashion_images, many=True)
        return Response({"fashion_images": serializer.data})
