from ctypes import CFUNCTYPE, c_int

import llvmlite.ir as ir
import llvmlite.binding as llvm


def main():
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()

    i64 = ir.IntType(64)

    # int func(int, int)
    ftype_main = ir.FunctionType(i64, [])
    module = ir.Module(name='sokoide_module')
    fn_main = ir.Function(module, ftype_main, name="main")
    block = fn_main.append_basic_block(name='entrypoint')

    ftype_write = ir.FunctionType(ir.VoidType(), [i64])
    fn_write = ir.Function(module, ftype_write, name="write")

    builder = ir.IRBuilder(block)
    builder.call(fn_write, (ir.Constant(i64, 42),), name="write")
    builder.ret(ir.Constant(i64, 42))

    llvm_ir = str(module)
    llvm_ir_parsed = llvm.parse_assembly(llvm_ir)
    with open("out.ll", "w") as f:
        f.write(str(llvm_ir_parsed))
    # print(llvm_ir_parsed)

if __name__ == '__main__':
    main()
