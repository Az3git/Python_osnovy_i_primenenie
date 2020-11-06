{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " [{\"name\": \"I\", \"parents\": [\"Q\"]}, {\"name\": \"N\", \"parents\": [\"Q\"]}, {\"name\": \"Q\", \"parents\": [\"A\", \"G\"]}, {\"name\": \"A\", \"parents\": [\"W\", \"T\"]}, {\"name\": \"G\", \"parents\": [\"T\", \"F\"]}, {\"name\": \"W\", \"parents\": []}, {\"name\": \"T\", \"parents\": []}, {\"name\": \"F\", \"parents\": []}]\n",
      "A  :  4\n",
      "F  :  5\n",
      "G  :  4\n",
      "I  :  1\n",
      "N  :  1\n",
      "Q  :  3\n",
      "T  :  6\n",
      "W  :  5\n"
     ]
    }
   ],
   "source": [
    "import json\n",
    "dictu = {}\n",
    "listo = []\n",
    "i = 0\n",
    "data = input()\n",
    "data_json = json.loads(data)\n",
    "bul = False\n",
    "def search_parents(child, prohod):\n",
    "    global listo\n",
    "    global i\n",
    "    global bul\n",
    "    i += 1\n",
    "    for el in data_json:\n",
    "        if prohod in el['parents']:\n",
    "            bul = True\n",
    "            if el['name'] in listo:\n",
    "                pass\n",
    "            else:\n",
    "                listo.append(el['name'])\n",
    "            dictu[child] = listo\n",
    "            search_parents(child, el['name'])\n",
    "\n",
    "for el in data_json:\n",
    "    child = el['name']\n",
    "    search_parents(child, child)\n",
    "    if bul == False:\n",
    "        dictu[child] = []\n",
    "    bul = False\n",
    "    i = 0\n",
    "    listo = []\n",
    "\n",
    "n = sorted(dictu)\n",
    "for el in n:\n",
    "    print(el, ' : ', len(dictu[el]) + 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
