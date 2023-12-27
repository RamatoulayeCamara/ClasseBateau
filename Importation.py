import sqlite3
import tkinter as tk
import csv
from tkinter import *
from tkinter import filedialog
import pandas as pd
from math import sqrt, sin, cos
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from PIL import Image, ImageTk
import itertools
from random import randint
from statistics import mean
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import numpy as np

conn = sqlite3.connect("stabilisateur.db")
cursor = conn.cursor()
