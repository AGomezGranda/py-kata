def past(h, m, s):
    h_2_ms = h * 3600
    m_2_s = m * 60
    total_sec = h_2_ms + m_2_s + s
    return total_sec * 1000