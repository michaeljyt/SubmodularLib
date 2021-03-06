package me.xmerge.core.submodularFunctions;

import me.xmerge.core.SubmodularBuffer;
import me.xmerge.util.UtilFunctions;


import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Set;

/**
 * Class for set cover
 */
public class SetCover<T extends Set & Serializable> extends SubmodularBuffer<T>{

    private T currentUnion;

    public SetCover(T emptySet) {
        assert emptySet.size() == 0;
        currentUnion = emptySet;
    }

    @Override
    @SuppressWarnings("unchecked")
    public double eval(ArrayList<T> A) {
        if (A.size() < 1)
            return 0.;
        T a = (T) UtilFunctions.deepClone(A.get(0));
        for (int i = 1; i < A.size(); ++i)
            a.addAll(A.get(i));
        return a.size();
    }

    @Override
    @SuppressWarnings("unchecked")
    public void addToSolution(T elem) {
        S.add(elem);
        currentUnion.addAll(elem);
        currentValue = currentUnion.size();
    }


}
