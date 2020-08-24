from ctypes import CFUNCTYPE, c_int

import llvmlite.ir as ir
import llvmlite.binding as llvm


def main():
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()

    i64 = ir.IntType(64)

    # int64_t main()
    ftype_main = ir.FunctionType(i64, [])
    module = ir.Module(name='sokoide_module')
    fn_main = ir.Function(module, ftype_main, name="main")
    block = fn_main.append_basic_block(name='entrypoint')

    # function prototype (external linkage implemented in builtin.c) for
    # void write(int64_t)
    ftype_write = ir.FunctionType(ir.VoidType(), [i64])
    fn_write = ir.Function(module, ftype_write, name="write")

    # make a block for main (entrypoint)
    builder = ir.IRBuilder(block)
    # call write(42)
    builder.call(fn_write, (ir.Constant(i64, 42),), name="write")
    # return 42
    builder.ret(ir.Constant(i64, 42))

    llvm_ir = str(module)
    llvm_ir_parsed = llvm.parse_assembly(llvm_ir)
    with open("out.ll", "w") as f:
        f.write(str(llvm_ir_parsed))
    # print(llvm_ir_parsed)


if __name__ == '__main__':
    main()
