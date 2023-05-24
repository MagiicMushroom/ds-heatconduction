# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 22:41:22 2019

@author: RickFu
"""
import postprocessing as pp
import heatConduction as hc
import pandas as pd


def main():
    """ Generate parameter
    
    1. Generate system-level parameters
    2. Generate material properties, grid, time, bcs
    
    Return: a Pandas series
    """
    
    column = 'values'
    df = pd.Series(name = column)
    df = df.astype('object')
    
    # System-level 
    df.at['problem'] = 'HeatConduction'
    df.at['SpatialDiscretize'] = 'CenteredDifferencing'
    df.at['TimeDiscretize'] = 'BackwardEular'
    df.at['ODEsolver'] = 'NewtonIteration'
    df.at['linearSolver'] = 'numpy linalg'
    df.at['CPU'] = 1
    
    # Material
    df.at['material'] = 'aluminum'
    df.at['material function'] = 'constant'
    df.at['density'] = 2710 #2710
    df.at['conductivity'] = 235 # Not real 173.2443
    df.at['heatCapacity'] = 900 #900
    
    # Grid
    df.at['length'] = 0.3
    df.at['numberOfNode'] = 101
    
    # Solution
    df.at['numberOfTimeStep'] = 90#400
    df.at['deltaTime'] = 2
    df.at['maxIteration'] = 20
    df.at['convergence'] = 1E-10
    df.at['relaxation'] = 1 # value in [0-1] Very sensitive!!!
    
    # Initial conditions
    df.at['IC value'] = 20.
    
    # Boundary conditions
    df.at['x=0 type'] = 'fixedTemperature'#'heatFlux' or 'fixedTemperature'
    df.at['x=0 value'] = 200
    df.at['x=L type'] = 'heatFlux'#'heatFlux' or 'fixedTemperature'
    df.at['x=L value'] = -100000.
    return df



if __name__ == "__main__":
    parameter = main()
    results, cache = hc.solve(parameter)
    T = pp.preprocess(parameter, results)
    pp.evolutionField(T)
    positions = [0, 0.002, 0.004, 0.006, 0.008, 0.01]
    pp.thermalCouplePlot(T, positions)
    times = [0, 2, 4, 6, 8, 10]
    pp.temperatureDistribution(T, times)
    
    
    
    
    