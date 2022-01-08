{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2331f738",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "\n",
    "with open('time_series_covid19_deaths_US.csv') as f:\n",
    "    data = list(f)[1:]\n",
    "    \n",
    "\n",
    "d_dict = {}\n",
    "t = 1\n",
    "for d in data:\n",
    "    l = d.strip('\\n').split(',')\n",
    "    if l[1] != 'US':\n",
    "        continue\n",
    "    if l[2] != 'USA':\n",
    "        continue\n",
    "    if l[6] == 'District of Columbia':\n",
    "        continue\n",
    "    if l[13] == '0':\n",
    "        continue\n",
    "    c = l[6]  # state    \n",
    "    a = l[14:]\n",
    "    if c in d_dict:\n",
    "        lt1 = d_dict[c]\n",
    "        lt2 = [int(x) for x in a] \n",
    "        res_lt = [ lt1[x] + lt2[x] for x in range (len (lt1))] \n",
    "        d_dict[c] = res_lt\n",
    "    else:\n",
    "        d_dict[c] = [int(x) for x in a]        \n",
    "        \n",
    "outF = open(\"#1 cumulative_time_series.txt\", \"w\")\n",
    "for i in range(len(d_dict['Wisconsin'])):\n",
    "    outF.write(str(d_dict['Wisconsin'][i]))\n",
    "    if i == len(d_dict['Wisconsin']) - 1:\n",
    "        break\n",
    "    outF.write(\",\")\n",
    "outF.write(\"\\n\")\n",
    "for i in range(len(d_dict['California'])):\n",
    "    outF.write(str(d_dict['California'][i]))\n",
    "    if i == len(d_dict['California']) - 1:\n",
    "        break\n",
    "    outF.write(\",\")\n",
    "outF.close()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4fdc93db",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "a = d_dict['Wisconsin']\n",
    "lt1 = [int(x) for x in a]\n",
    "d_time_WI = [ lt1[x] - lt1[x-1] for x in range(1, len(lt1))] \n",
    "\n",
    "\n",
    "b = d_dict['California']\n",
    "lt1 = [int(x) for x in b]\n",
    "d_time_CA = [ lt1[x] - lt1[x-1] for x in range(1, len(lt1))]\n",
    "\n",
    "\n",
    "outF = open(\"#2 differenced_time_series.txt\", \"w\")\n",
    "for i in range(len(d_time_WI)):\n",
    "    outF.write(str(d_time_WI[i]))\n",
    "    if i == len(d_time_WI) - 1:\n",
    "        break\n",
    "    outF.write(\",\")\n",
    "outF.write(\"\\n\")\n",
    "for i in range(len(d_time_CA)):\n",
    "    outF.write(str(d_time_CA[i]))\n",
    "    if i == len(d_time_CA) - 1:\n",
    "        break\n",
    "    outF.write(\",\")  \n",
    "outF.close()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2f559043",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "50\n",
      "[[20.6829, 1514.2862, 38.9138, 8.0, 309, 217, 291, 386], [0.7178, 5.0423, 2.2455, 0.0, 23, 229, 271, 328], [32.2369, 2574.1982, 50.7366, 14.0, 335, 226, 365, 401], [11.4373, 276.6189, 16.6319, 7.0, 158, 241, 308, 351], [112.9704, 22547.419, 150.158, 65.0, 1093, 216, 317, 392], [12.2909, 425.2864, 20.6225, 6.0, 267, 253, 393, 471], [14.4704, 688.9251, 26.2474, 3.0, 204, 433, 478, 488], [3.2213, 42.7716, 6.54, 2.0, 130, 246, 450, 474], [64.4129, 3848.9323, 62.0398, 51.0, 276, 263, 369, 399], [37.2439, 1962.3133, 44.298, 26.0, 449, 226, 356, 420], [0.9599, 8.5541, 2.9247, 0.0, 59, 246, 322, 353], [3.9721, 38.041, 6.1677, 1.0, 35, 251, 299, 365], [41.2648, 1960.8915, 44.282, 25.0, 236, 266, 437, 470], [23.9861, 900.8779, 30.0146, 14.0, 192, 254, 335, 456], [10.8467, 687.4051, 26.2184, 5.0, 469, 251, 303, 399], [9.4077, 663.6073, 25.7606, 2.0, 359, 230, 269, 321], [13.0105, 699.0243, 26.4391, 8.0, 448, 200, 265, 352], [20.5453, 536.6138, 23.1649, 14.0, 244, 276, 428, 483], [1.5836, 12.8841, 3.5894, 0.0, 41, 217, 254, 403], [17.2021, 790.2135, 28.1107, 10.0, 549, 252, 445, 472], [31.6237, 2745.9246, 52.4016, 16.0, 764, 349, 469, 481], [36.8972, 2647.6427, 51.4552, 16.0, 286, 253, 455, 485], [13.4878, 323.1418, 17.9761, 8.0, 140, 257, 336, 447], [13.7909, 259.2281, 16.1006, 9.0, 98, 256, 372, 421], [18.4808, 1227.0963, 35.0299, 8.0, 266, 240, 302, 377], [3.047, 33.5605, 5.7931, 1.0, 54, 241, 285, 309], [3.885, 73.4641, 8.5711, 0.0, 64, 260, 303, 413], [10.885, 183.8579, 13.5594, 6.0, 71, 230, 329, 385], [2.4303, 35.1336, 5.9274, 0.0, 66, 236, 420, 447], [46.5523, 10512.6828, 102.5314, 16.0, 1796, 420, 477, 490], [7.7683, 164.4742, 12.8247, 4.0, 123, 239, 284, 399], [93.4634, 54434.9804, 233.3131, 28.0, 4448, 458, 490, 499], [24.3066, 879.3102, 29.6532, 16.0, 178, 226, 324, 392], [2.6969, 30.6468, 5.536, 1.0, 58, 274, 307, 331], [35.9617, 2193.3017, 46.8327, 20.0, 211, 249, 295, 416], [13.3728, 5553.0108, 74.5185, 3.0, 1716, 191, 254, 331], [5.1829, 60.484, 7.7771, 3.0, 54, 229, 280, 372], [48.8118, 4600.8148, 67.8293, 24.0, 387, 240, 398, 469], [4.7718, 346.2284, 18.6072, 0.0, 152, 253, 445, 476], [17.6655, 565.1634, 23.7732, 10.0, 241, 236, 358, 393], [3.5854, 63.173, 7.9481, 0.0, 54, 259, 285, 316], [22.3711, 987.1776, 31.4194, 10.0, 195, 234, 294, 358], [95.2178, 10463.7069, 102.2923, 55.0, 630, 233, 349, 387], [3.0174, 14.8812, 3.8576, 2.0, 25, 239, 307, 391], [0.4652, 1.4021, 1.1841, 0.0, 18, 232, 265, 489], [20.2648, 1081.9647, 32.8932, 11.0, 383, 211, 336, 439], [10.9652, 250.7409, 15.8348, 8.0, 174, 239, 386, 480], [5.2213, 162.0887, 12.7314, 2.0, 173, 224, 261, 316], [14.5523, 456.7246, 21.3711, 7.0, 135, 252, 297, 375], [1.4094, 26.7923, 5.1761, 0.0, 40, 234, 267, 288]]\n"
     ]
    }
   ],
   "source": [
    "states = []\n",
    "for k,v in d_dict.items():\n",
    "    cum_ts = d_dict[k]\n",
    "    current_num = cum_ts[-1]\n",
    "    half_num = current_num/2\n",
    "    quarter_num = current_num/4\n",
    "    eigth_num = current_num/8\n",
    "    \n",
    "    half_ind = 0\n",
    "    quarter_ind = 0\n",
    "    eigth_ind = 0\n",
    "    cur_ind = len(cum_ts) - 1\n",
    "    for i in range(len(cum_ts) - 1):\n",
    "        if cum_ts[i] <= eigth_num and cum_ts[i+1] > eigth_num:\n",
    "            eigth_ind = i\n",
    "        if cum_ts[i] <= quarter_num and cum_ts[i+1] > quarter_num:\n",
    "            quarter_ind = i\n",
    "        if cum_ts[i] <= half_num and cum_ts[i+1] > half_num:\n",
    "            half_ind = i\n",
    "    x6 = cur_ind - half_ind\n",
    "    x7 = cur_ind - quarter_ind\n",
    "    x8 = cur_ind - eigth_ind\n",
    "    lt = [int(x) for x in v]\n",
    "    d_dict[k] = [lt[x] - lt[x-1] for x in range(1, len(lt))]\n",
    "    one_state = []\n",
    "    avg = sum(d_dict[k]) / len(d_dict[k])\n",
    "    x1 =  avg\n",
    "    one_state.append(round(x1, 4))\n",
    "    \n",
    "    var = sum((x-avg)**2 for x in d_dict[k]) / len(d_dict[k])\n",
    "    x2 = var\n",
    "    one_state.append(round(x2, 4))\n",
    "    \n",
    "    std = var**0.5\n",
    "    x3 = std\n",
    "    one_state.append(round(x3, 4))\n",
    "    \n",
    "    # attribute to : https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/ \n",
    "    n_num = d_dict[k]\n",
    "    n = len(n_num)\n",
    "    n_num.sort()\n",
    "    if n % 2 == 0:\n",
    "        median1 = n_num[n//2]\n",
    "        median2 = n_num[n//2 - 1]\n",
    "        median = (median1 + median2)/2\n",
    "    else:\n",
    "        median = n_num[n//2]\n",
    "    x4 = median\n",
    "    one_state.append(round(x4, 4))\n",
    "    \n",
    "    max_value = max(d_dict[k])\n",
    "    x5 = max_value\n",
    "    one_state.append(round(x5, 4))\n",
    "    \n",
    "    one_state.append(round(x6, 4))\n",
    "    one_state.append(round(x7, 4))\n",
    "    one_state.append(round(x8, 4))\n",
    "    states.append(one_state)\n",
    "\n",
    "print(len(states))\n",
    "print(states)\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a19e4180",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "50\n",
      "[[17.97, 2.78, 16.25, 12.31, 6.57, 9.74, 15.68, 46.45], [0.22, 0.01, 0.46, 0.0, 0.11, 14.23, 7.2, 18.96], [28.24, 4.73, 21.35, 21.54, 7.16, 13.11, 47.03, 53.55], [9.75, 0.51, 6.65, 10.77, 3.16, 18.73, 22.88, 29.86], [100.0, 41.42, 64.18, 100.0, 24.27, 9.36, 26.69, 49.29], [10.51, 0.78, 8.37, 9.23, 5.62, 23.22, 58.9, 86.73], [12.45, 1.26, 10.8, 4.62, 4.2, 90.64, 94.92, 94.79], [2.45, 0.08, 2.31, 3.08, 2.53, 20.6, 83.05, 88.15], [56.84, 7.07, 26.22, 78.46, 5.82, 26.97, 48.73, 52.61], [32.69, 3.6, 18.57, 40.0, 9.73, 13.11, 43.22, 62.56], [0.44, 0.01, 0.75, 0.0, 0.93, 20.6, 28.81, 30.81], [3.12, 0.07, 2.15, 1.54, 0.38, 22.47, 19.07, 36.49], [36.26, 3.6, 18.57, 38.46, 4.92, 28.09, 77.54, 86.26], [20.91, 1.65, 12.42, 21.54, 3.93, 23.6, 34.32, 79.62], [9.23, 1.26, 10.78, 7.69, 10.18, 22.47, 20.76, 52.61], [7.95, 1.22, 10.59, 3.08, 7.7, 14.61, 6.36, 15.64], [11.15, 1.28, 10.88, 12.31, 9.71, 3.37, 4.66, 30.33], [17.85, 0.98, 9.47, 21.54, 5.1, 31.84, 73.73, 92.42], [0.99, 0.02, 1.04, 0.0, 0.52, 9.74, 0.0, 54.5], [14.88, 1.45, 11.6, 15.38, 11.99, 22.85, 80.93, 87.2], [27.7, 5.04, 22.06, 24.62, 16.84, 59.18, 91.1, 91.47], [32.38, 4.86, 21.66, 24.62, 6.05, 23.22, 85.17, 93.36], [11.58, 0.59, 7.23, 12.31, 2.75, 24.72, 34.75, 75.36], [11.84, 0.47, 6.43, 13.85, 1.81, 24.34, 50.0, 63.03], [16.01, 2.25, 14.58, 12.31, 5.6, 18.35, 20.34, 42.18], [2.29, 0.06, 1.99, 1.54, 0.81, 18.73, 13.14, 9.95], [3.04, 0.13, 3.18, 0.0, 1.04, 25.84, 20.76, 59.24], [9.26, 0.34, 5.33, 9.23, 1.2, 14.61, 31.78, 45.97], [1.75, 0.06, 2.04, 0.0, 1.08, 16.85, 70.34, 75.36], [40.96, 19.31, 43.66, 24.62, 40.14, 85.77, 94.49, 95.73], [6.49, 0.3, 5.01, 6.15, 2.37, 17.98, 12.71, 52.61], [82.66, 100.0, 100.0, 43.08, 100.0, 100.0, 100.0, 100.0], [21.19, 1.61, 12.26, 24.62, 3.61, 13.11, 29.66, 49.29], [1.98, 0.05, 1.87, 1.54, 0.9, 31.09, 22.46, 20.38], [31.55, 4.03, 19.67, 30.77, 4.36, 21.72, 17.37, 60.66], [11.47, 10.2, 31.59, 4.62, 38.33, 0.0, 0.0, 20.38], [4.19, 0.11, 2.84, 4.62, 0.81, 14.23, 11.02, 39.81], [42.97, 8.45, 28.71, 36.92, 8.33, 18.35, 61.02, 85.78], [3.83, 0.63, 7.51, 0.0, 3.02, 23.22, 80.93, 89.1], [15.29, 1.04, 9.73, 15.38, 5.03, 16.85, 44.07, 49.76], [2.77, 0.11, 2.91, 0.0, 0.81, 25.47, 13.14, 13.27], [19.47, 1.81, 13.03, 15.38, 4.0, 16.1, 16.95, 33.18], [84.22, 19.22, 43.56, 84.62, 13.81, 15.73, 40.25, 46.92], [2.27, 0.02, 1.15, 3.08, 0.16, 17.98, 22.46, 48.82], [0.0, 0.0, 0.0, 0.0, 0.0, 15.36, 4.66, 95.26], [17.6, 1.99, 13.66, 16.92, 8.24, 7.49, 34.75, 71.56], [9.33, 0.46, 6.31, 12.31, 3.52, 17.98, 55.93, 91.0], [4.23, 0.3, 4.97, 3.08, 3.5, 12.36, 2.97, 13.27], [12.52, 0.84, 8.7, 10.77, 2.64, 22.85, 18.22, 41.23], [0.84, 0.05, 1.72, 0.0, 0.5, 16.1, 5.51, 0.0]]\n"
     ]
    }
   ],
   "source": [
    "max_x1 = 0\n",
    "min_x1 = 10000\n",
    "max_x2 = 0\n",
    "min_x2 = 10000\n",
    "max_x3 = 0\n",
    "min_x3 = 10000\n",
    "max_x4 = 0\n",
    "min_x4 = 10000\n",
    "max_x5 = 0\n",
    "min_x5 = 10000\n",
    "max_x6 = 0\n",
    "min_x6 = 10000\n",
    "max_x7 = 0\n",
    "min_x7 = 10000\n",
    "max_x8 = 0\n",
    "min_x8 = 10000\n",
    "\n",
    "for state in states:\n",
    "    if state[0] > max_x1:\n",
    "        max_x1 = state[0]\n",
    "    if state[0] < min_x1: \n",
    "        min_x1 = state[0]\n",
    "    if state[1] > max_x2:\n",
    "        max_x2 = state[1]\n",
    "    if state[1] < min_x2: \n",
    "        min_x2 = state[1]\n",
    "    if state[2] > max_x3:\n",
    "        max_x3 = state[2]\n",
    "    if state[2] < min_x3: \n",
    "        min_x3 = state[2]\n",
    "    if state[3] > max_x4:\n",
    "        max_x4 = state[3]\n",
    "    if state[3] < min_x4: \n",
    "        min_x4 = state[3]\n",
    "    if state[4] > max_x5:\n",
    "        max_x5 = state[4]\n",
    "    if state[4] < min_x5: \n",
    "        min_x5 = state[4]\n",
    "    if state[5] > max_x6:\n",
    "        max_x6 = state[5]\n",
    "    if state[5] < min_x6: \n",
    "        min_x6 = state[5]\n",
    "    if state[6] > max_x7:\n",
    "        max_x7 = state[6]\n",
    "    if state[6] < min_x7: \n",
    "        min_x7 = state[6]\n",
    "    if state[7] > max_x8:\n",
    "        max_x8 = state[7]\n",
    "    if state[7] < min_x8: \n",
    "        min_x8 = state[7]\n",
    "\n",
    "states_scaled = []\n",
    "for state in states:\n",
    "    x1 = state[0]\n",
    "    x1_sca = ((x1 - min_x1)/(max_x1 - min_x1))*100\n",
    "    x2 = state[1]\n",
    "    x2_sca = ((x2 - min_x2)/(max_x2 - min_x2))*100\n",
    "    x3 = state[2]\n",
    "    x3_sca = ((x3 - min_x3)/(max_x3 - min_x3))*100\n",
    "    x4 = state[3]\n",
    "    x4_sca = ((x4 - min_x4)/(max_x4 - min_x4))*100\n",
    "    x5 = state[4]\n",
    "    x5_sca = ((x5 - min_x5)/(max_x5 - min_x5))*100\n",
    "    x6 = state[5]\n",
    "    x6_sca = ((x6 - min_x6)/(max_x6 - min_x6))*100\n",
    "    x7 = state[6]\n",
    "    x7_sca = ((x7 - min_x7)/(max_x7 - min_x7))*100\n",
    "    x8 = state[7]\n",
    "    x8_sca = ((x8 - min_x8)/(max_x8 - min_x8))*100\n",
    "    state_scaled = [round(x1_sca,2),round(x2_sca,2),round(x3_sca,2),round(x4_sca,2),round(x5_sca,2),round(x6_sca,2),round(x7_sca,2),round(x8_sca,2)]\n",
    "    states_scaled.append(state_scaled)\n",
    "    \n",
    "print(len(states_scaled))\n",
    "print(states_scaled)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "902db9c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "outF = open(\"#4 parameter_estimates.txt\", \"w\")\n",
    "counter = 1\n",
    "for state in states_scaled:\n",
    "    for i in range(len(state)):\n",
    "        outF.write(str(state[i]))\n",
    "        if i == len(state)-1:\n",
    "            break\n",
    "        outF.write(\",\")\n",
    "    if counter == 50:\n",
    "        break\n",
    "    outF.write(\"\\n\")\n",
    "    counter += 1\n",
    "outF.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b8f0a9b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'6'}, {'29'}, {'31'}, {'49', '32', '38', '10', '30', '41', '19', '27', '28', '11', '43', '16', '21', '34', '39', '37', '5', '20', '25', '44', '0', '2', '1', '13', '48', '35', '9', '33', '7', '40', '46', '18', '36', '47', '12', '3', '23', '15', '26', '24', '17', '45', '14', '22'}, {'8', '4', '42'}]\n",
      "[3, 3, 3, 3, 4, 3, 0, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3]\n"
     ]
    }
   ],
   "source": [
    "ind_dict = {}\n",
    "ind = 0\n",
    "for state in states_scaled:\n",
    "    ind_dict[str(ind)] = state\n",
    "    ind += 1\n",
    "\n",
    "\n",
    "def Euclidean(a,b):\n",
    "    a = np.array(a)\n",
    "    b = np.array(b)\n",
    "\n",
    "    dist = np.linalg.norm(a-b)\n",
    "    return dist\n",
    "\n",
    "\n",
    " # single linkage distance\n",
    "def sld(cluster1, cluster2): \n",
    "    res = float('inf')\n",
    "    # c1, c2 each is a country in the corresponding cluster\n",
    "    for c1 in cluster1:\n",
    "        for c2 in cluster2:\n",
    "            dist = Euclidean(ind_dict[c1], ind_dict[c2])\n",
    "            if dist < res:\n",
    "                res = dist\n",
    "    return res\n",
    "\n",
    "# complete linkage distance\n",
    "def cld(cluster1, cluster2): \n",
    "    res = float(0)\n",
    "    # c1, c2 each is a country in the corresponding cluster\n",
    "    for c1 in cluster1:\n",
    "        for c2 in cluster2:\n",
    "            dist = Euclidean(ind_dict[c1], ind_dict[c2])\n",
    "            if dist > res:\n",
    "                res = dist\n",
    "    return res\n",
    "\n",
    "k = 5\n",
    "\n",
    "\n",
    "# hierarchical clustering (sld, 'Euclidean')\n",
    "n = len(ind_dict)\n",
    "clusters = [{d} for d in ind_dict.keys()]\n",
    "for _ in range(n-k):\n",
    "    dist = float('inf')\n",
    "    best_pair = (None, None)\n",
    "    for i in range(len(clusters)-1):\n",
    "        for j in range(i+1, len(clusters)):\n",
    "            if sld(clusters[i], clusters[j]) < dist:\n",
    "                dist = sld(clusters[i], clusters[j])\n",
    "                best_pair = (i,j)\n",
    "    new_clu = clusters[best_pair[0]] | clusters[best_pair[1]]\n",
    "    clusters = [clusters[i] for i in range(len(clusters)) if i not in best_pair]\n",
    "    clusters.append(new_clu)\n",
    "print(clusters)\n",
    "\n",
    "\n",
    "clu_lst = [None]*50\n",
    "for i in clusters[0]:\n",
    "    clu_lst[int(i)] = 0\n",
    "for i in clusters[1]:\n",
    "    clu_lst[int(i)] = 1\n",
    "for i in clusters[2]:\n",
    "    clu_lst[int(i)] = 2\n",
    "for i in clusters[3]:\n",
    "    clu_lst[int(i)] = 3\n",
    "for i in clusters[4]:\n",
    "    clu_lst[int(i)] = 4\n",
    "print(clu_lst)\n",
    "\n",
    "outF = open(\"#5 clusters_from_single_linkage.txt\", \"w\")\n",
    "for i in range(len(clu_lst)):\n",
    "    outF.write(str(clu_lst[i]))\n",
    "    if i == len(clu_lst) - 1:\n",
    "        break\n",
    "    outF.write(\",\")\n",
    "outF.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ed591a99",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'31'}, {'6', '20', '29'}, {'49', '33', '10', '30', '41', '40', '11', '18', '43', '36', '16', '47', '3', '25', '15', '26', '24', '1', '48', '14', '35'}, {'8', '4', '42'}, {'32', '7', '38', '19', '28', '46', '27', '21', '5', '12', '37', '39', '34', '23', '44', '0', '2', '17', '13', '45', '22', '9'}]\n",
      "[4, 2, 4, 2, 3, 4, 1, 4, 3, 4, 2, 2, 4, 4, 2, 2, 2, 4, 2, 4, 1, 4, 4, 4, 2, 2, 2, 4, 4, 1, 2, 0, 4, 2, 4, 2, 2, 4, 4, 4, 2, 2, 3, 2, 4, 4, 4, 2, 2, 2]\n"
     ]
    }
   ],
   "source": [
    "# hierarchical clustering (cld, 'Euclidean')\n",
    "n = len(ind_dict)\n",
    "clusters = [{d} for d in ind_dict.keys()]\n",
    "for _ in range(n-k):\n",
    "    dist = float('inf')\n",
    "    best_pair = (None, None)\n",
    "    for i in range(len(clusters)-1):\n",
    "        for j in range(i+1, len(clusters)):\n",
    "            if cld(clusters[i], clusters[j]) < dist:\n",
    "                dist = cld(clusters[i], clusters[j])\n",
    "                best_pair = (i,j)\n",
    "    new_clu = clusters[best_pair[0]] | clusters[best_pair[1]]\n",
    "    clusters = [clusters[i] for i in range(len(clusters)) if i not in best_pair]\n",
    "    clusters.append(new_clu)\n",
    "print(clusters)\n",
    "\n",
    "\n",
    "clu_lst = [None]*50\n",
    "for i in clusters[0]:\n",
    "    clu_lst[int(i)] = 0\n",
    "for i in clusters[1]:\n",
    "    clu_lst[int(i)] = 1\n",
    "for i in clusters[2]:\n",
    "    clu_lst[int(i)] = 2\n",
    "for i in clusters[3]:\n",
    "    clu_lst[int(i)] = 3\n",
    "for i in clusters[4]:\n",
    "    clu_lst[int(i)] = 4\n",
    "print(clu_lst)\n",
    "\n",
    "outF = open(\"#6 clusters_from_complete_linkage.txt\", \"w\")\n",
    "for i in range(len(clu_lst)):\n",
    "    outF.write(str(clu_lst[i]))\n",
    "    if i == len(clu_lst) - 1:\n",
    "        break\n",
    "    outF.write(\",\")\n",
    "outF.close()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "63d155a5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49']\n",
      "[{'11'}, {'15'}, {'39'}, {'0'}, {'4'}]\n",
      "[{'3', '0', '10', '30', '26', '41', '24', '11', '27', '48', '18', '14', '43', '36'}, {'49', '25', '33', '15', '40', '1', '16', '35', '47'}, {'12', '5', '20', '38', '7', '19', '29', '17', '28', '46', '6', '21', '37'}, {'39', '32', '9', '23', '44', '2', '13', '45', '22', '34'}, {'8', '31', '4', '42'}]\n"
     ]
    }
   ],
   "source": [
    "states = [d for d in ind_dict.keys()]\n",
    "print(states)\n",
    "## k-means (Euclidean)\n",
    "import copy\n",
    "def center(cluster):\n",
    "    return np.average([ind_dict[c] for c in cluster], axis=0)\n",
    "init_num = np.random.choice(len(states) - 1, k)\n",
    "clusters = [{states[i]} for i in init_num]\n",
    "print(clusters)\n",
    "t = 1\n",
    "while True:\n",
    "    new_clusters = [set() for _ in range(k)]\n",
    "    centers = [center(cluster) for cluster in clusters]\n",
    "    if t == 1:\n",
    "        t = 2\n",
    "    for c in states:\n",
    "        clu_ind = np.argmin([Euclidean(ind_dict[c], centers[i]) for i in range(k)])\n",
    "        new_clusters[clu_ind].add(c)\n",
    "    if all(new_clusters[i] == clusters[i] for i in range(k)):\n",
    "        break\n",
    "    else:\n",
    "        clusters = copy.deepcopy(new_clusters)\n",
    "    \n",
    "print(clusters)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "04735f53",
   "metadata": {},
   "outputs": [],
   "source": [
    "clu_lst = [None]*50\n",
    "for i in clusters[0]:\n",
    "    clu_lst[int(i)] = 0\n",
    "for i in clusters[1]:\n",
    "    clu_lst[int(i)] = 1\n",
    "for i in clusters[2]:\n",
    "    clu_lst[int(i)] = 2\n",
    "for i in clusters[3]:\n",
    "    clu_lst[int(i)] = 3\n",
    "for i in clusters[4]:\n",
    "    clu_lst[int(i)] = 4\n",
    "\n",
    "\n",
    "outF = open(\"#7 clusters_from_k_means_clustering.txt\", \"w\")\n",
    "for i in range(len(clu_lst)):\n",
    "    outF.write(str(clu_lst[i]))\n",
    "    if i == len(clu_lst) - 1:\n",
    "        break\n",
    "    outF.write(\",\")\n",
    "outF.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "3e2140e6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'3', '0', '10', '30', '26', '41', '24', '11', '27', '48', '18', '14', '43', '36'}, {'49', '25', '33', '15', '40', '1', '16', '35', '47'}, {'12', '5', '20', '38', '7', '19', '29', '17', '28', '46', '6', '21', '37'}, {'39', '32', '9', '23', '44', '2', '13', '45', '22', '34'}, {'8', '31', '4', '42'}]\n",
      "[array([ 8.19642857,  0.74642857,  6.53142857,  6.70357143,  2.82571429,\n",
      "       17.97785714, 18.67428571, 43.84      ]), array([ 4.76666667,  1.47555556,  7.44222222,  2.90777778,  6.93      ,\n",
      "       15.10666667,  8.38222222, 15.79777778]), array([19.48615385,  3.61230769, 14.85153846, 16.56923077,  8.71846154,\n",
      "       35.52384615, 77.54230769, 89.02692308]), array([19.089,  1.971, 12.132, 19.693,  4.662, 17.341, 33.983, 66.065]), array([80.93  , 41.9275, 58.49  , 76.54  , 35.975 , 38.015 , 53.9175,\n",
      "       62.205 ])]\n"
     ]
    }
   ],
   "source": [
    "print(clusters)\n",
    "centers = [center(cluster) for cluster in clusters]\n",
    "print(centers)\n",
    "\n",
    "outF = open(\"#8 cluster_centers.txt\", \"w\")\n",
    "for i in range(len(centers)):\n",
    "    for j in range(len(centers[i])):\n",
    "        outF.write(str(round(centers[i][j], 4)))\n",
    "        if j == len(centers[i]) - 1:\n",
    "            break\n",
    "        outF.write(\",\")\n",
    "    if i == len(centers) - 1:\n",
    "        break\n",
    "    outF.write(\"\\n\")\n",
    "outF.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "fabcbfd7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "total distortion =  59132.806596449984\n"
     ]
    }
   ],
   "source": [
    "cens = []\n",
    "total_dis = 0\n",
    "for c in centers:\n",
    "    cen = []\n",
    "    for par in c:\n",
    "        cen.append(round(par, 4))\n",
    "    cens.append(cen)\n",
    "\n",
    "for i in range(len(clusters)):\n",
    "    center = cens[i]\n",
    "    for state in clusters[i]:\n",
    "        params = ind_dict[state]\n",
    "        for j in range(len(params)):\n",
    "            total_dis += (params[j] - center[j])**2\n",
    "print(\"total distortion = \", total_dis)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4276bbc0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
