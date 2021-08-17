/***
* File: matrix.cpp
* Description: 
* Author: Bruno R. de Abreu  |  babreu at illinois dot edu
* National Center for Supercomputing Applications (NCSA)
*  
* Creation Date: Wednesday, 2nd June 2021, 4:11:27 pm
* Last Modified: Thursday, 3rd June 2021, 7:13:08 am
*  
* Copyright (c) 2021, Bruno R. de Abreu, National Center for Supercomputing Applications.
* All rights reserved.
* License: This program and the accompanying materials are made available to any individual
*          under the citation condition that follows: On the event that the software is
*          used to generate data that is used implicitly or explicitly for research
*          purposes, proper acknowledgment must be provided in the citations section of
*          publications. This includes both the author's name and the National Center
*          for Supercomputing Applications. If you are uncertain about how to do
*          so, please check this page: https://github.com/babreu-ncsa/cite-me.
*          This software cannot be used for commercial purposes in any way whatsoever.
*          Omitting this license when redistributing the code is strongly disencouraged.
*          The software is provided without warranty of any kind. In no event shall the
*          author or copyright holders be liable for any kind of claim in connection to
*          the software and its usage.
***/

#include <iostream>
#include <chrono>
#include <vector>

using namespace std;
typedef chrono::high_resolution_clock Clock;

int main(void)
{
    chrono::duration<double> duration;
    const double w = 1.0;
    double r;
    int n = 1 << 13;

    // using vector lib
    vector<double> v;
    vector<vector<double>> m;
    for (int i = 0; i < n; i++)
        v.push_back(0.0);
    for (int i = 0; i < n; i++)
        m.push_back(v);

    printf("ROW MAJOR: i-j loop\n");
    // write
    auto t1 = Clock::now();
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            m[i][j] = w;
        }
    }
    auto t2 = Clock::now();
    duration = t2 - t1;
    printf("Writing to matrix time: %.12e s.", duration.count());
    printf(" Each operation took %.3e s\n", duration.count() / (n * n));
    // write
    auto t3 = Clock::now();
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            r = m[i][j];
        }
    }
    auto t4 = Clock::now();
    duration = t4 - t3;
    printf("Reading from matrix time: %.12e s.", duration.count());
    printf(" Each operation took %.3e s\n", duration.count() / (n * n));

    printf("\nCOLUMN MAJOR: j-i loop\n");
    // write
    auto t5 = Clock::now();
    for (int j = 0; j < n; j++)
    {
        for (int i = 0; i < n; i++)
        {
            m[i][j] = w;
        }
    }
    auto t6 = Clock::now();
    duration = t6 - t5;
    printf("Writing to matrix time: %.12e s.", duration.count());
    printf(" Each operation took %.3e s\n", duration.count() / (n * n));
    // write
    auto t7 = Clock::now();
    for (int j = 0; j < n; j++)
    {
        for (int i = 0; i < n; i++)
        {
            r = m[i][j];
        }
    }
    auto t8 = Clock::now();
    duration = t8 - t7;
    printf("Reading from matrix time: %.12e s.", duration.count());
    printf(" Each operation took %.3e s\n", duration.count() / (n * n));

    return 0;
}