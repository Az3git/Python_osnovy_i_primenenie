{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "lis = []\n",
    "n = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "962\n",
      "930\n",
      "933\n",
      "968\n",
      "937\n",
      "938\n",
      "970\n",
      "909\n",
      "942\n",
      "978\n",
      "914\n",
      "950\n",
      "921\n",
      "988\n",
      "926\n",
      "aads\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    try:\n",
    "        n = int(input())\n",
    "        lis.append(n)\n",
    "    except ValueError:\n",
    "        break\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[962, 930, 933, 968, 937, 938, 970, 909, 942, 978, 914, 950, 921, 988, 926]\n"
     ]
    }
   ],
   "source": [
    "print(lis)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Boring\n",
      "Interesting\n",
      "Boring\n",
      "Boring\n",
      "Boring\n",
      "Interesting\n",
      "Interesting\n",
      "Interesting\n",
      "Interesting\n",
      "Boring\n",
      "Interesting\n",
      "Interesting\n",
      "Boring\n",
      "Interesting\n",
      "Interesting\n"
     ]
    }
   ],
   "source": [
    "for el in lis:\n",
    "    api_url = \"http://numbersapi.com/\" + str(el) +'/math?json=true'\n",
    "    res = requests.get(api_url)\n",
    "    dict_1 = res.json()\n",
    "    if dict_1[\"found\"] == True:\n",
    "        print(\"Interesting\")\n",
    "    else:\n",
    "        print(\"Boring\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "http://numbersapi.com/999/math?json=true\n"
     ]
    }
   ],
   "source": [
    "print(api_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "res = requests.get(api_url)\n",
    "dict_1 = res.json()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'text': '999 is an uninteresting number.', 'number': 999, 'found': False, 'type': 'math'}\n"
     ]
    }
   ],
   "source": [
    "print(res.json())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'dict'>\n"
     ]
    }
   ],
   "source": [
    "print(type(res.json()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Boring\n"
     ]
    }
   ],
   "source": [
    "if dict_1[\"found\"] == True:\n",
    "    print(\"Interesting\")\n",
    "else:\n",
    "    print(\"Boring\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print(dict_1[\"found\"])"
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
