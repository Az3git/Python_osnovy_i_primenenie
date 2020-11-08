{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import json\n",
    "dicto = {}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "headers = {\"X-Xapp-Token\" : 'eyJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6ImFydHN5Iiwic3ViamVjdF9hcHBsaWNhdGlvbiI6IjVkNDA5OTZlNmU2MDQ5MDAwNzQ5MGZhMiIsImV4cCI6MTYwNTM1OTAyMCwiaWF0IjoxNjA0NzU0MjIwLCJhdWQiOiI1ZDQwOTk2ZTZlNjA0OTAwMDc0OTBmYTIiLCJpc3MiOiJHcmF2aXR5IiwianRpIjoiNWZhNjliMmMwYTZiMjcwMDBkZWQyMmJhIn0.KRM6xcj0gMq5XZ7zW914dcYyuGmjqbj_dzK89ZQBSbA'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('dataset_24476_4.txt') as f:\n",
    "    for line in f:\n",
    "        api_url = \"https://api.artsy.net/api/artists/\" + line\n",
    "        api_url = api_url[0:-1]\n",
    "        r = requests.get(api_url, headers=headers)\n",
    "        \n",
    "        j = json.loads(r.text)\n",
    "        \n",
    "        birthday = j['birthday']\n",
    "\n",
    "        \n",
    "        sortable_name = j['sortable_name']\n",
    "        \n",
    "        dicto.update({sortable_name : birthday})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "ki = sorted(dicto.items(), key=lambda x: (x[1], x[0]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Abraham de Verwer\n",
      "Abildgaard Nicolai\n",
      "Abastenia St. Leger Eberle\n",
      "Abbott Berenice\n",
      "Abercrombie Gertrude\n",
      "Abell Jenny\n",
      "Abrams Michael\n",
      "Abergel Etti\n",
      "A'Court Angela\n",
      "23 Rigo\n",
      "A. Westerhuis Ronald\n",
      "Aberle Christian\n",
      "Syed Abdullah  M. I.\n",
      "Acosta Pavel\n",
      "Aboudia\n"
     ]
    }
   ],
   "source": [
    "for el in ki:\n",
    "    try:\n",
    "        int(el[0])\n",
    "    except ValueError:\n",
    "        print(el[0])"
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
