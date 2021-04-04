{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "CRR_trinomial.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNS6Ixu0VudZulwNZUiQcM9",
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
        "<a href=\"https://colab.research.google.com/github/williamcarp/Cox_Ross_Rubenstein_Model/blob/main/CRR_trinomial.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3_H7u559qog_"
      },
      "source": [
        "###################################################################\n",
        "# COX-ROSS-RUBENSTEIN (CRR) Trinomial Tree Implementation \n",
        "###################################################################\n",
        "\n",
        "# Author      : Will Carpenter \n",
        "# Date Created: April 1st, 2021  \n",
        "\n",
        "# Description: Trinomial tree implementation that prices European and \n",
        "# American calls/puts. With increasing tree step size (dt), the tree\n",
        "# prices converge to Black-Scholes formulaic prices. Option data for \n",
        "# pricing Euro calls/puts can be obtained from Yahoo Finance. See the \n",
        "# PDF document labeled \"CRR_Trinomial_Tree_Documentation\" for a detailed\n",
        "# discussion of the model and underlying asset-pricing theory. \n",
        "\n",
        "import math \n",
        "import numpy as np \n",
        "from scipy.stats import norm # cumulative normal distribution"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0OWt6t1LqulM"
      },
      "source": [
        "def crr_trinomial_tree(S, K, r, T, t, v, x):\n",
        "\n",
        "    # S: initial asset price\n",
        "    # K: strike price \n",
        "    # r: riskless rate \n",
        "    # T: time to maturity (in yrs.)\n",
        "    # t: number of steps \n",
        "    # v: annualized volatility\n",
        "    # x: euro call (= 1) euro put (= -1)\n",
        "\n",
        "    # Calculate time increment \n",
        "    dt = T / t\n",
        "    # Initialize tree  \n",
        "    crrTree        = np.empty((2*t-1,t))\n",
        "    crrTree[:]     = np.nan\n",
        "\n",
        "    # Initialize tree parameters \n",
        "    u = math.exp(v*math.sqrt(2*dt))\n",
        "    d = 1/u\n",
        "    m = 1\n",
        "    # Probability-up\n",
        "    pu = ((math.exp(r*dt/2) - math.exp(-1*v*math.sqrt(dt/2))) / \n",
        "         (math.exp(v*math.sqrt(dt/2)) - math.exp(-1*v*math.sqrt(dt/2))))**2\n",
        "    # Probability-down\n",
        "    pd = ((math.exp(v*math.sqrt(dt/2)) - math.exp(r*dt/2)) /\n",
        "         (math.exp(v*math.sqrt(dt/2)) - math.exp(-1*v*math.sqrt(dt/2))))**2\n",
        "    # Probability-middle\n",
        "    pm = 1 - (pu + pd)\n",
        "\n",
        "    lastCol = crrTree.shape[1]-1\n",
        "    mid     = len(crrTree)//2\n",
        "\n",
        "    # Set price at middle of tree \n",
        "    crrTree[mid, lastCol] = max(x*S-x*K, 0)\n",
        "\n",
        "    for i in range(1, mid+1):\n",
        "        crrTree[mid-i, lastCol] = max(x*S*u**i - x*K, 0)\n",
        "        crrTree[mid+i, lastCol] = max(x*S*d**i - x*K, 0)\n",
        "\n",
        "    for col in range(lastCol-1, -1, -1):\n",
        "        for row in range(0, col*2+1):\n",
        "            # move backwards from previous prices \n",
        "            Su = crrTree[row,   col+1]\n",
        "            Sm = crrTree[row+1, col+1]\n",
        "            Sd = crrTree[row+2, col+1]\n",
        "            # Calcuate price on tree\n",
        "            crrTree[row, col] = math.exp(-r*dt)*(pu*Su + pm*Sm + pd*Sd)\n",
        "\n",
        "    # print(\"u parameter: \" \"{:6.4f}\".format(u))\n",
        "    # print(\"d parameter: \" \"{:6.4f}\".format(d))\n",
        "    # print(\"pu parameter: \" \"{:5.3f}\".format(pu))\n",
        "    # print(\"pd parameter: \" \"{:5.3f}\".format(pd))\n",
        "    # print(\"pm parameter: \" \"{:5.3f}\".format(pm))\n",
        "    # print(\"pm+pu+pd: \" \"{:9.3f}\".format(pm+pu+pd))\n",
        "\n",
        "    # print(\"\\nCRR Stock Price Tree:\\n\")\n",
        "    # for i in crrTree:\n",
        "    #     for j in i:\n",
        "    #         print(\"{:7.2f}\".format(j), end=\" \")\n",
        "    #     print() \n",
        "    # print(\"\\n\")\n",
        "\n",
        "    return crrTree[0,0]\n",
        "\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DyzbWee1E30l"
      },
      "source": [
        "# Black-Scholes Model\n",
        "\n",
        "def black_scholes(S, K, r, T, t, v, x):\n",
        "\n",
        "    d1 = (math.log(S/K) + (v**2/2 + r)*T)/(v*math.sqrt(T))\n",
        "    d2 = d1 - v*math.sqrt(T)\n",
        "\n",
        "    return x*S*norm.cdf(d1) - x*K*math.exp(-r*T)*norm.cdf(d2)\n",
        "    "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ggbx2akuTw7M"
      },
      "source": [
        "# Testing for parameters and tree structure (see commented code above)\n",
        "\n",
        "crr_price = crr_trinomial_tree(91.36, 95.00, 0.007, 15/252, n, 0.8218, 1)\n"
      ],
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zPJVBLQwq21S",
        "outputId": "87913c94-0e71-4629-dcad-57a36d5be7e9"
      },
      "source": [
        "# Calculating Option Prices for various securities and compare results to \n",
        "# Black-Scholes (B-S) analytical pricing. \n",
        "\n",
        "# Relevant option data (current price, strike, term, and volatility) can be \n",
        "# obtained from Yahoo finance for a variety of different calls and puts. \n",
        "\n",
        "n = 300 # number of steps\n",
        "\n",
        "# Monster Beverage \n",
        "crr_price = crr_trinomial_tree(91.36, 95.00, 0.007, 15/252, n, 0.8218, 1)\n",
        "bs_price  =     black_scholes(91.36, 95.00, 0.007, 15/252, n, 0.8218, 1)\n",
        "print(\"________________________________________________________________\\n\")\n",
        "print(\"Monster Beverage Corp.\")\n",
        "print(\"Expiry: June 18th\")\n",
        "print(\"CRR European Call Price: $\" + \"{:3.2f}\".format(crr_price))\n",
        "print(\"B-S European Call Price: $\" + \"{:3.2f}\".format(bs_price))\n",
        "\n",
        "# Carvana \n",
        "crr_price = crr_trinomial_tree(265.32, 267.50, 0.00063, 15/252, n, 0.6065, 1)\n",
        "bs_price  =     black_scholes(265.32, 267.50, 0.00063, 15/252, n, 0.6065, 1)\n",
        "print(\"________________________________________________________________\\n\")\n",
        "print(\"Carvana Co.\")\n",
        "print(\"Expiry: April 16th\")\n",
        "print(\"CRR European Call Price: $\" + \"{:3.2f}\".format(crr_price))\n",
        "print(\"B-S European Call Price: $\" + \"{:3.2f}\".format(bs_price))\n",
        "\n",
        "# American Airlines\n",
        "crr_price = crr_trinomial_tree(23.86, 24.00, 0.006, 15/252, n, 0.5234, 1)\n",
        "bs_price  =     black_scholes(23.86, 24.00, 0.006, 15/252, n, 0.5234, 1)\n",
        "print(\"________________________________________________________________\\n\")\n",
        "print(\"American Airlines Group Inc.\")\n",
        "print(\"Expiry: April 23rd (15 days)\")\n",
        "print(\"European Call Price: $\" + \"{:3.2f}\".format(crr_price))\n",
        "print(\"B-S European Call Price: $\" + \"{:3.2f}\".format(bs_price))\n",
        "print(\"________________________________________________________________\\n\")\n",
        "\n",
        "# Spotify\n",
        "crr_price = crr_trinomial_tree(273.10, 298.00, 0.006, 100/252, n, 0.5093, 1)\n",
        "bs_price  =     black_scholes(273.10, 298.00, 0.006, 100/252, n, 0.5093, 1)\n",
        "print(\"Spotify\")\n",
        "print(\"Expiry: April 23rd (15 days)\")\n",
        "print(\"European Call Price: $\" + \"{:3.2f}\".format(crr_price))\n",
        "print(\"B-S European Call Price: $\" + \"{:3.2f}\".format(bs_price))\n",
        "print(\"________________________________________________________________\\n\")\n",
        "\n",
        "\n",
        "print(\"American Airlines:\\n\")\n",
        "print(\"Steps  CRR    B-S\")\n",
        "for steps in range(25, 300, 25):\n",
        "    crr_price = crr_trinomial_tree(23.86, 24.00, 0.006, 15/252, steps, 0.5234, 1)\n",
        "    bs_price  =      black_scholes(23.86, 24.00, 0.006, 15/252, steps, 0.5234, 1)\n",
        "    print(\"{:4.0f}\".format(steps), \"{:6.3f}\".format(crr_price), \"{:6.3f}\".format(bs_price))\n",
        "    \n"
      ],
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "________________________________________________________________\n",
            "\n",
            "Monster Beverage Corp.\n",
            "Expiry: June 18th\n",
            "CRR European Call Price: $5.77\n",
            "B-S European Call Price: $5.78\n",
            "________________________________________________________________\n",
            "\n",
            "Carvana Co.\n",
            "Expiry: April 16th\n",
            "CRR European Call Price: $14.63\n",
            "B-S European Call Price: $14.65\n",
            "________________________________________________________________\n",
            "\n",
            "American Airlines Group Inc.\n",
            "Expiry: April 23rd (15 days)\n",
            "European Call Price: $1.15\n",
            "B-S European Call Price: $1.15\n",
            "________________________________________________________________\n",
            "\n",
            "Spotify\n",
            "Expiry: April 23rd (15 days)\n",
            "European Call Price: $25.46\n",
            "B-S European Call Price: $25.50\n",
            "________________________________________________________________\n",
            "\n",
            "American Airlines:\n",
            "\n",
            "Steps  CRR    B-S\n",
            "  25  1.129  1.153\n",
            "  50  1.142  1.153\n",
            "  75  1.147  1.153\n",
            " 100  1.148  1.153\n",
            " 125  1.150  1.153\n",
            " 150  1.150  1.153\n",
            " 175  1.151  1.153\n",
            " 200  1.151  1.153\n",
            " 225  1.151  1.153\n",
            " 250  1.152  1.153\n",
            " 275  1.152  1.153\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}