package org.shashank.basics.behavioral_patterns.iterator.iterators;

import org.shashank.basics.behavioral_patterns.iterator.app.Application;

public interface AppIterator {
    boolean hasNext();

    Application getNext();

    void reset();
}
