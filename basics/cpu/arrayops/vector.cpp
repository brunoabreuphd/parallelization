/***
* File: vector.cpp
* Description: 
* Author: Bruno R. de Abreu  |  babreu at illinois dot edu
* National Center for Supercomputing Applications (NCSA)
*  
* Creation Date: Wednesday, 2nd June 2021, 11:56:23 am
* Last Modified: Thursday, 3rd June 2021, 7:13:42 am
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
    int n = 1 << 19;

    // standard array call
    printf("STANDARD ARRAY DECLARATION double foo[n]\n");
    // writing to array
    double foo[n];
    auto t1 = Clock::now();
    for (int i = 0; i < n; i++)
    {
        foo[i] = w;
    }
    auto t2 = Clock::now();
    duration = t2 - t1;
    printf("Writing to array time: %.12e s.", duration.count());
    printf(" Each operation took %.3e s\n", duration.count() / n);
    // reading from array
    auto t3 = Clock::now();
    for (int i = 0; i < n; i++)
    {
        r = foo[i];
    }
    auto t4 = Clock::now();
    duration = t4 - t3;
    printf("Reading from array time: %.12e s.", duration.count());
    printf(" Each operation took %.3e s\n", duration.count() / n);

    // using vector lib
    printf("\nUSING STD VECTOR LIBRARY\n");
    vector<double> v(n);
    // write
    auto t5 = Clock::now();
    for (int i = 0; i < n; i++)
    {
        v[i] = w;
    }
    auto t6 = Clock::now();
    duration = t6 - t5;
    printf("Writing to array time: %.12e s.", duration.count());
    printf(" Each operation took %.3e s\n", duration.count() / n);
    // read
    auto t7 = Clock::now();
    for (int i = 0; i < n; i++)
    {
        r = v[i];
    }
    auto t8 = Clock::now();
    duration = t8 - t7;
    printf("Read from array time: %.12e s.", duration.count());
    printf(" Each operation took %.3e s\n", duration.count() / n);

    // using vector lib
    printf("\nUSING STD VECTOR LIBRARY + ITERATORS\n");
    auto t9 = Clock::now();
    for (auto it = begin(v); it != end(v); ++it)
    {
        *it = w;
    }
    auto t10 = Clock::now();
    duration = t10 - t9;
    printf("Writing to array time: %.12e s.", duration.count());
    printf(" Each operation took %.3e s\n", duration.count() / n);
    // read
    auto t11 = Clock::now();
    for (auto it = begin(v); it != end(v); ++it)
    {
        r = *it;
    }
    auto t12 = Clock::now();
    duration = t12 - t11;
    printf("Read from array time: %.12e s.", duration.count());
    printf(" Each operation took %.3e s\n", duration.count() / n);

    return 0;
}