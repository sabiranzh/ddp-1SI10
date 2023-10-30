{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPX2kDkc7PEZA5s8Ou27jGa",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sabiranzh/ddp-1SI10/blob/main/tugas%206.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mpOMDr7Iyekx",
        "outputId": "e50f0bfe-4bf2-41a1-95ac-ffc8b6f89f39"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[951, 651, 69, 319, 601, 485, 507, 725, 547, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 105, 941, 47, 907, 375, 823, 597, 615, 953, 345, 399, 219, 237, 949, 687, 217, 815, 67, 767]\n"
          ]
        }
      ],
      "source": [
        "\n",
        "\n",
        "numbers = [\n",
        "951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,  615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,  386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,  399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527\n",
        "]\n",
        "\n",
        "index=0\n",
        "nilai_ganjil=[]\n",
        "while index<len(numbers):\n",
        "    if numbers[index] == 553:\n",
        "        break\n",
        "    else:\n",
        "        if numbers[index] % 2 !=0:\n",
        "            nilai_ganjil.append(numbers [index])\n",
        "    index += 1\n",
        "\n",
        "print(nilai_ganjil)\n",
        "\n",
        "\n",
        "baris = int(input(\"masukan baris\"))\n",
        "for baris in range(1, baris + 1):\n",
        "  for kolom in range(baris):\n",
        "    print(\"* \", end=\"\")\n",
        "  print()"
      ]
    }
  ]
}