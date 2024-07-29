{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNF4WAT3qh5fB+p/ByJEi59",
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
        "<a href=\"https://colab.research.google.com/github/dlrjrlaudwn/dlrj_rlaudwn/blob/main/day2_subwayfee_02.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 224
        },
        "id": "3hWRqeVv7vn0",
        "outputId": "aa80a1fe-b6bc-4595-d63d-d40b5cd97a2b"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "ZeroDivisionError",
          "evalue": "division by zero",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-3-946c0c903c46>\u001b[0m in \u001b[0;36m<cell line: 8>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      9\u001b[0m   \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m8\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     10\u001b[0m     \u001b[0mrow\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrow\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 11\u001b[0;31m   \u001b[0mrate\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mrow\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m/\u001b[0m\u001b[0mrow\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m6\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     12\u001b[0m   \u001b[0;32mif\u001b[0m \u001b[0mrate\u001b[0m\u001b[0;34m>\u001b[0m\u001b[0mmax_rate\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     13\u001b[0m     \u001b[0mmax_rate\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mrate\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mZeroDivisionError\u001b[0m: division by zero"
          ]
        }
      ],
      "source": [
        "import csv\n",
        "f=open('subwayfee.csv',encoding='utf-8-sig')\n",
        "data=csv.reader(f)\n",
        "header=next(data)\n",
        "max_rate=0\n",
        "rate=0\n",
        "\n",
        "for row in data:\n",
        "  for i in range(4,8):\n",
        "    row[i]=int(row[i])\n",
        "  rate=row[4]/row[6]\n",
        "  if rate>max_rate:\n",
        "    max_rate=rate\n",
        "print(max_rate)\n",
        "f.close()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import csv\n",
        "\n",
        "f=open('subwayfee.csv',encoding='utf-8-sig')\n",
        "data=csv.reader(f)\n",
        "header=next(data)\n",
        "rate=0\n",
        "\n",
        "for row in data:\n",
        "  for i in range(4,8):\n",
        "    row[i]=int(row[i])\n",
        "  rate=row[4]/(row[4]+row[6])\n",
        "\n",
        "  if row[6]==0:\n",
        "    print(row)\n",
        "f.close()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6RqeQ3Y69cct",
        "outputId": "2ec9d03a-a604-43b8-c69c-a2e9665a8380"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Jun.24', '일산선', '1949', '지축', 61, 0, 0, 0]\n",
            "['Jun.24', '경의선', '1296', '계양', 2, 0, 0, 0]\n",
            "['Jun.24', '6호선', '2649', '신내', 10, 0, 0, 0]\n",
            "['Jun.24', '7호선', '2756', '신중동', 1, 0, 0, 0]\n",
            "['Jun.24', '7호선', '2761', '부평구청', 2, 0, 0, 0]\n"
          ]
        }
      ]
    }
  ]
}