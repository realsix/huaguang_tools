import paddlelite.lite as lite

a=lite.Opt()
# 非 combined 形式
a.set_model_dir("./")

a.set_optimize_out("./football")
a.set_valid_places("arm")
a.set_model_type("naive_buffer")
a.run()
