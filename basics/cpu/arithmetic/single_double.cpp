/***
* File: single_double.cpp
* Description: Timings of arithmetic calculations for single/double precision.
* Author: Bruno R. de Abreu  |  babreu at illinois dot edu
* National Center for Supercomputing Applications (NCSA)
*  
* Creation Date: Wednesday, 2nd June 2021, 11:26:25 am
* Last Modified: Thursday, 3rd June 2021, 6:55:07 am
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
#include <cstdint>

typedef std::chrono::high_resolution_clock Clock;

int main(void)
{
    std::chrono::duration<double> duration;

    // single precision block
    int n = 1000000000;
    float a = 1.0, b = 1.0;
    printf("SINGLE PRECISION TIMINGS\n");
    printf("i has size %d, a and b have size %d\n", sizeof(int), sizeof(float));
    auto t1 = Clock::now();
    for (int j = 0; j < n; j++)
    {
        a = a + b;
    }
    auto t2 = Clock::now();
    duration = t2 - t1;
    printf("Addition loop took %.12e s, or %.3e s per operation.\n", duration.count(), duration.count() / n);

    a = 1.0;
    b = 1.0;
    auto t3 = Clock::now();
    for (int j = 0; j < n; j++)
    {
        a = a * b;
    }
    auto t4 = Clock::now();
    duration = t4 - t3;
    printf("Muliplication loop took %.12e s, or %.3e s per operation.\n", duration.count(), duration.count() / n);

    a = 1.0;
    b = 1.0;
    auto t5 = Clock::now();
    for (int j = 0; j < n; j++)
    {
        a = a / b;
    }
    auto t6 = Clock::now();
    duration = t6 - t5;
    printf("Division loop took %.12e s, or %.3e s per operation.\n", duration.count(), duration.count() / n);

    // double precision block
    long nn = 1000000000;
    double aa = 1.0, bb = 1.0;
    printf("\nDOUBLE PRECISION TIMINGS\n");
    printf("i has size %d, a and b have size %d\n", sizeof(long), sizeof(double));
    auto t7 = Clock::now();
    for (long j = 0; j < nn; j++)
    {
        aa = aa + bb;
    }
    auto t8 = Clock::now();
    duration = t8 - t7;
    printf("Addition loop took %.12e s, or %.3e s per operation.\n", duration.count(), duration.count() / n);

    aa = 1.0;
    bb = 1.0;
    auto t9 = Clock::now();
    for (long j = 0; j < nn; j++)
    {
        aa = aa * bb;
    }
    auto t10 = Clock::now();
    duration = t10 - t9;
    printf("Multiplication loop took %.12e s, or %.3e s per operation.\n", duration.count(), duration.count() / n);

    aa = 1.0;
    bb = 1.0;
    auto t11 = Clock::now();
    for (long j = 0; j < nn; j++)
    {
        aa = aa / bb;
    }
    auto t12 = Clock::now();
    duration = t12 - t11;
    printf("Division loop took %.12e s, or %.3e s per operation.\n", duration.count(), duration.count() / n);

    return 0;
}