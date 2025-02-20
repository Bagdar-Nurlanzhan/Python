{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Interface status\n",
      "================================================================================\n",
      "DN                                                 Description           Speed    MTU  \n",
      "-------------------------------------------------- --------------------  ------  ------\n",
      "topology/pod-1/node-201/sys/phys-[eth1/33]                               inherit 9150\n",
      "topology/pod-1/node-201/sys/phys-[eth1/34]                               inherit 9150\n",
      "topology/pod-1/node-201/sys/phys-[eth1/35]                               inherit 9150\n",
      "topology/pod-1/node-201/sys/phys-[eth1/36]                               inherit 9150\n",
      "topology/pod-1/node-201/sys/phys-[eth1/1]                               inherit 9150\n",
      "topology/pod-1/node-201/sys/phys-[eth1/2]                               inherit 9150\n",
      "topology/pod-1/node-201/sys/phys-[eth1/3]                               inherit 9150\n",
      "topology/pod-1/node-201/sys/phys-[eth1/4]                               inherit 9150\n",
      "topology/pod-1/node-201/sys/phys-[eth1/5]                               inherit 9150\n",
      "topology/pod-1/node-201/sys/phys-[eth1/6]                               inherit 9150\n",
      "topology/pod-1/node-201/sys/phys-[eth1/7]                               inherit 9150\n",
      "topology/pod-1/node-201/sys/phys-[eth1/8]                               inherit 9150\n",
      "topology/pod-1/node-201/sys/phys-[eth1/9]                               inherit 9150\n",
      "topology/pod-1/node-201/sys/phys-[eth1/10]                               inherit 9150\n",
      "topology/pod-1/node-201/sys/phys-[eth1/11]                               inherit 9150\n",
      "topology/pod-1/node-201/sys/phys-[eth1/12]                               inherit 9150\n",
      "topology/pod-1/node-201/sys/phys-[eth1/13]                               inherit 9150\n",
      "topology/pod-1/node-201/sys/phys-[eth1/14]                               inherit 9150\n"
     ]
    }
   ],
   "source": [
    "import json\n",
    "\n",
    "print(\"Interface status\")\n",
    "print(\"================================================================================\")\n",
    "print(\"DN                                                 Description           Speed    MTU  \")\n",
    "print(\"-------------------------------------------------- --------------------  ------  ------\")\n",
    "\n",
    "with open('sample-data.json') as file:\n",
    "    data = json.load(file)\n",
    "\n",
    "if isinstance(data, dict) and \"imdata\" in data:\n",
    "    for item in data[\"imdata\"]:\n",
    "        attributes = item[\"l1PhysIf\"][\"attributes\"]\n",
    "        dn = attributes.get(\"dn\", \"N/A\")\n",
    "        speed = attributes.get(\"speed\", \"N/A\")\n",
    "        mtu = attributes.get(\"mtu\", \"N/A\")\n",
    "        print(dn,\"                             \",speed, mtu) "
   ]
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
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}